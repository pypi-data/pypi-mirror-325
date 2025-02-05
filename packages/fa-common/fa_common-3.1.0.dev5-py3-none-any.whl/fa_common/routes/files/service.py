from io import BytesIO
from typing import Any, Literal

import pandas as pd
from bson import ObjectId
from fastapi import UploadFile
from pydantic import EmailStr

from fa_common.config import get_settings
from fa_common.exceptions import (
    BadRequestError,
    ForbiddenError,
    InternalServerError,
    NotFoundError,
    StorageError,
)
from fa_common.routes.project.models import ProjectDB
from fa_common.routes.shared.models import TableSort
from fa_common.routes.user.models import UserDB
from fa_common.storage import get_storage_client
from fa_common.utils import get_logger, validate_id

from .models import FileDB, UpdateFile
from .utils import get_data_frame_from_file, get_unique_filename, safe_join_path

LOG = get_logger()


async def delete_files_for_user(user: UserDB):
    files = await get_files_for_user(user, owner_only=True)
    for file in files:
        await delete_file(file)
    return True


async def get_file_bytes(file: FileDB) -> BytesIO:
    client = get_storage_client()
    try:
        if file.file_ref.bucket is not None and file.file_ref.id is not None:
            file_bytes = await client.get_file(file.file_ref.bucket, file.file_ref.id)

            if file_bytes is None:
                raise NotFoundError(f"No file content returned from {file.file_ref.id}")
        else:
            raise InternalServerError("File ref is incomplete.")
    except StorageError as err:
        raise NotFoundError(f"Referenced file is missing from {file.file_ref.id}") from err

    return file_bytes


async def get_table_from_file(
    file: FileDB,
    offset: int = 0,
    limit: int = 100,
    sort: TableSort | None = None,
    separator: str | None = None,
    sheet: str | None = None,
    return_format: Literal["csv", "json"] = "json",
) -> str | list[dict]:
    # Rename Duplicate columns
    file_bytes = await get_file_bytes(file)

    try:
        df = await get_data_frame_from_file(
            file_bytes,
            file.file_ref.name,
            header_row=None,
            can_be_single_col=True,
            separator=separator,
            sheet=sheet,
        )
    except Exception as e:
        raise BadRequestError(f"Error creating table from file, is this fail a valid table format?: {e}") from e

    if sort is not None:
        try:
            df = df.sort_values(by=sort.column, ascending=sort.ascending)
        except KeyError as e:
            LOG.warning(f"Unable to sort by {sort.column}, column not found in file: {file.file_ref.name}: {e}")

    if return_format == "json":
        return df.iloc[offset : offset + limit].to_dict("records")
    else:
        return df.iloc[offset : offset + limit].to_csv(index=False)


async def upload_file(
    file: UploadFile,
    user: UserDB,
    project_id: str | ObjectId | None = None,
    sub_path: str = "",
    tags: list[str] = [],
    file_users: list[EmailStr] = [],
    allow_duplicates: bool = False,
) -> FileDB:
    settings = get_settings()
    client = get_storage_client()
    if project_id is not None:
        valid_proj_id = validate_id(project_id)
        project = await ProjectDB.find_one(ProjectDB.id == valid_proj_id)
        if project is None:
            raise NotFoundError(f"Project with id {project_id} does not exist.")

        storage = project.get_storage()
    else:
        storage = user.get_storage_location(settings.PROJECT_NAME)

    storage_path = safe_join_path([storage.path_prefix, sub_path])

    file.filename = await get_unique_filename(storage.bucket_name, storage_path, file.filename, allow_duplicates)

    sheets = None
    if file.filename is not None and (file.filename.lower().endswith(".xlsx")):
        try:
            excel_file = BytesIO(file.file.read())

            wb = pd.ExcelFile(excel_file, engine="openpyxl")
            sheets = wb.sheet_names
            file.file.seek(0)  # be kind, rewind
        except Exception as e:
            raise InternalServerError(f"Unable to read excel file: {file.filename}") from e

        file.file.seek(0)

    file_ref = await client.upload_file(
        file,
        storage.bucket_name,
        storage_path,
    )

    file_model = FileDB(
        owner_id=user.sub,
        project_id=str(project_id) if project_id is not None else None,
        file_ref=file_ref,
        tags=tags,
        file_users=file_users,
        sheets=sheets,
    )
    await file_model.save()

    return file_model


async def replace_file(
    filedb: FileDB,
    file: UploadFile,
    allow_duplicates: bool = False,
) -> FileDB:
    client = get_storage_client()

    bucket = filedb.file_ref.bucket
    path = filedb.file_ref.path if filedb.file_ref.path is not None else ""

    if filedb.file_ref.bucket is not None and filedb.file_ref.id is not None:
        await client.delete_file(filedb.file_ref.bucket, filedb.file_ref.id)
    else:
        raise InternalServerError(f"Unable to delete file due to incomplete File ref {filedb.file_ref.id} ID: {filedb.id}.")

    file.filename = await get_unique_filename(bucket, path, file.filename, allow_duplicates=allow_duplicates)

    file_ref = await client.upload_file(
        file,
        bucket,
        path,
    )

    filedb.file_ref = file_ref
    await filedb.save()

    return filedb


async def get_files_for_user(
    user: UserDB,
    owner_only=False,
    offset: int = 0,
    limit: int = 10,
    sort: list[str] = [],
    project_ids: list[str] | None = None,
    path: str | None = None,
    extensions: list[str] | None = None,
    mime_type: str | None = None,
    start_with: str | None = None,
    exact_name: str | None = None,
) -> list[FileDB]:
    """
    Get files for a user.

    Parameters
    ----------
    user : UserDB
        The user object representing the user.
    owner_only : bool, optional
        If True, only return files owned by the user. Default is False.
    offset : int, optional
        The number of files to skip before returning results. Default is 0.
    limit : int, optional
        The maximum number of files to return. Default is 10.
    sort : list[str], optional
        The list of fields to sort the files by using the syntax `['+fieldName', '-secondField']`.
        See https://beanie-odm.dev/tutorial/finding-documents/
        Default is an empty list.
    project_ids : list[str] | None, optional
        A list of project IDs to filter the files by. Default is None.
    path : str | None, optional
        The exact file path to filter the files by. Default is None.
    extension : str | None, optional
        The file extension to filter the files by. Default is None.
    mime_type : str | None, optional
        The MIME type to filter the files by. Default is None.
    start_with : str | None, optional
        The prefix to filter the files by. Default is None.
    exact_name : str | None, optional
        The exact name to filter the files by. Will take priority over 'start_with' if both are provided. Default is None.

    Returns
    -------
    list[FileDB]
        A list of files belonging to the user.
    """
    user_query: dict[str, Any] = {}

    if owner_only:
        user_query = {"ownerId": user.sub}
    else:
        # First $or query for user ownership and file users
        user_query = {
            "$or": [
                {"ownerId": user.sub},
                {"fileUsers": {"$elemMatch": {"$regex": f"^{user.email}$", "$options": "i"}}},
            ]
        }

    # Second $or query for file extensions
    extension_query = []
    if extensions:
        extension_query = [{"fileRef.name": {"$regex": f".*\\.{ext}$", "$options": "i"}} for ext in extensions]

    # Combine both $or queries using $and
    combined_query: dict[str, Any] = {"$and": [user_query]}
    if extension_query:
        combined_query["$and"].append({"$or": extension_query})

    if project_ids:
        combined_query["projectId"] = {"$in": project_ids}

    if path:
        combined_query["fileRef.path"] = {"$regex": f"^{path}$", "$options": "i"}

    if exact_name:
        combined_query["fileRef.name"] = {"$regex": f"^{exact_name}$", "$options": "i"}
    elif start_with:
        combined_query["fileRef.name"] = {"$regex": f"^{start_with}", "$options": "i"}

    if mime_type:
        combined_query["fileRef.contentType"] = mime_type

    query = FileDB.find(combined_query)
    if sort:
        query = query.sort(*sort)

    return await query.skip(offset).limit(limit).to_list()


async def get_file(file_id: str | ObjectId, user: UserDB) -> FileDB:
    valid_file_id = validate_id(file_id)
    file = await FileDB.find_one(FileDB.id == valid_file_id)

    if file is None:
        raise NotFoundError(f"File {file_id} not found.")

    if file.owner_id != user.sub and user.email not in file.file_users:
        raise ForbiddenError(detail="You do not have access to this file")

    return file


async def delete_file(file: FileDB):
    client = get_storage_client()

    if file.file_ref.bucket is not None and file.file_ref.id is not None:
        await client.delete_file(file.file_ref.bucket, file.file_ref.id)
    else:
        raise InternalServerError(f"Unable to delete file due to incomplete File ref {file.file_ref.id} ID: {file.id}.")
    await file.delete()
    return True


async def update_file_metadata(
    file: FileDB,
    update: UpdateFile,
) -> FileDB:
    if file is None or file.id is None:
        raise NotFoundError("File does not exist")

    update_file = file.model_copy(update=update.get_update_dict())
    if update.add_tags is not None:
        update_file.tags.extend(update.add_tags)
    if update.add_file_users is not None:
        update_file.file_users.extend(update.add_file_users)
    await update_file.save()

    return update_file
