import importlib
import itertools
import random
from pathlib import Path
from typing import List

from fastapi import FastAPI

from fa_common import DatabaseType, get_settings, logger
from fa_common.db.utils_sqlite import SqliteKVS
from fa_common.utils import get_current_app


def default_id_generator(bit_size: int = 32) -> int:
    """
    Generator of IDs for newly created MongoDB rows.

    :return: `bit_size` long int
    """
    return random.getrandbits(bit_size)


def get_next_id() -> int:
    """
    Retrieves ID generator function from the path, specified in project's conf.
    :return: newly generated ID.
    """
    return default_id_generator()


async def setup_db(app: FastAPI) -> None:
    """
    Helper function to setup MongoDB connection & `motor` client during setup.
    Use during app startup as follows:

    .. code-block:: python

        app = FastAPI()

        @app.on_event('startup')
        async def startup():
            setup_mongodb(app)

    :param app: app object, instance of FastAPI
    :return: None
    """
    settings = get_settings()
    if settings.DATABASE_TYPE == DatabaseType.MONGODB:
        # Only import mongo deps if we are using mongo
        import motor.motor_asyncio

        client = motor.motor_asyncio.AsyncIOMotorClient(
            settings.MONGODB_DSN,
            tz_aware=True,
            connect=settings.MONGO_AUTO_CONNECT,
            minPoolSize=settings.mongodb_min_pool_size,
            maxPoolSize=settings.mongodb_max_pool_size,
        )

        app.mongodb = client[settings.MONGODB_DBNAME]  # type: ignore
        logger.info("Mongo Database has been set")
        if settings.USE_BEANIE:
            from beanie import Document, init_beanie

            logger.info("Initialising Beanie ODM")
            models = set(get_models(Document))
            for model in models:
                model.model_rebuild()
            await init_beanie(app.mongodb, document_models=list(models))  # type: ignore

    elif settings.DATABASE_TYPE == DatabaseType.GCP_FIRESTORE:
        from firebase_admin import firestore

        app.firestore = firestore.client()  # type: ignore
        logger.info("Firestore client has been set")
    elif settings.DATABASE_TYPE == DatabaseType.SQLITEDB:
        app.sqlitedb = SqliteKVS(settings.SQLITEDB_PATH)
        logger.info("Sqlite created. Adderss: {}", hex(id(app.sqlitedb)))
        await app.sqlitedb.start()
        logger.info("Sqlite Database has been set")
    elif settings.DATABASE_TYPE == DatabaseType.NONE:
        logger.info("Database is set to NONE and cannot be used")
        return
    else:
        raise ValueError("DATABASE_TYPE Setting is not a valid database option.")


async def cleanup_db(app: FastAPI) -> None:
    """
    Helper function to clean up the sqlite database connection when the
    application is stopped.
    """
    settings = get_settings()
    if settings.DATABASE_TYPE == DatabaseType.SQLITEDB and hasattr(app, "sqlitedb") and app.sqlitedb is not None:
        await app.sqlitedb.close()


def get_db_client():
    """
    Gets instance of BaseClient client for you to make DB queries.
    :return: BaseClient.
    """
    settings = get_settings()
    if settings.DATABASE_TYPE == DatabaseType.MONGODB:
        if settings.USE_BEANIE:
            return get_current_app().mongodb  # type: ignore
        else:
            from .mongo_client import MongoDBClient

            client = MongoDBClient()
            return client
    elif settings.DATABASE_TYPE == DatabaseType.GCP_FIRESTORE:
        from .firestore_client import FirestoreClient

        client = FirestoreClient()
        return client
    elif settings.DATABASE_TYPE == DatabaseType.SQLITEDB:
        from .sqlite_db_client import SQLiteDBClient

        client = SQLiteDBClient()
        return client

    raise ValueError("DATABASE_TYPE Setting is not a valid database option.")


def fullname(obj):
    module = obj.__module__
    name = obj.__qualname__
    if module is not None and module != "__builtin__":
        name = module + "." + name
    return name


def all_subclasses(cls):
    sub_classes = set()
    for c in cls.__subclasses__():
        if "pydantic.main" not in fullname(c):
            for s in all_subclasses(c):
                if "pydantic.main" not in fullname(s):
                    sub_classes.add(s)
    return set(cls.__subclasses__()).union(sub_classes)


def get_models(type) -> list:  # noqa: A002
    """
    Scans `settings.APP_PATH`.
    Find `models` modules in each of them and get all attributes there.
    Last step is to filter attributes to return only those,
    subclassed from DocumentDBModel (or timestamped version).

    Used internally only by `create_indexes` function.

    :return: list of user-defined models (subclassed from DocumentDBModel) in apps
    """

    models = Path(get_settings().APP_PATH).glob("**/models.py")
    models_extras = Path(get_settings().APP_PATH).glob("**/models/*.py")
    for m in itertools.chain(models, models_extras):
        mod_string = str(m).replace("/", ".").replace("\\", ".").replace(".py", "")
        importlib.import_module(mod_string)

    return list(all_subclasses(type))


async def create_indexes() -> List[str]:
    """
    Gets all models in project and then creates indexes for each one of them.
    :return: list of indexes that has been invoked to create
             (could've been created earlier, it doesn't raise in this case).
    """
    from .models import DocumentDBModel

    models = get_models(DocumentDBModel)
    indexes = []
    for model in models:
        indexes.append(await model.create_indexes())
    return list(filter(None, indexes))
