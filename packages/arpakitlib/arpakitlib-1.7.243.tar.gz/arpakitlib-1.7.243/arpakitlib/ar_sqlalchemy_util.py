# arpakit
import asyncio
import logging
from datetime import timedelta, datetime
from typing import Any
from uuid import uuid4

from sqlalchemy import create_engine, QueuePool, text, func, inspect, AsyncAdaptedQueuePool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.orm.session import Session

from arpakitlib.ar_datetime_util import now_utc_dt
from arpakitlib.ar_sqlalchemy_model_util import BaseDBM

_ARPAKIT_LIB_MODULE_VERSION = "3.0"


def get_string_info_from_declarative_base(class_: type[DeclarativeBase]):
    res = f"Models: {len(class_.__subclasses__())}"
    for i, cls in enumerate(class_.__subclasses__()):
        res += f"\n{i + 1}. {cls.__name__}"
    return res


class SQLAlchemyDB:
    def __init__(
            self,
            *,
            db_url: str = "postgresql://arpakitlib:arpakitlib@localhost:50517/arpakitlib",
            async_db_url: str = "postgresql+asyncpg://arpakitlib:arpakitlib@localhost:50517/arpakitlib",
            db_echo: bool = False,
            base_dbm: type[BaseDBM] | None = None,
            db_models: list[Any] | None = None,
    ):
        self._logger = logging.getLogger(self.__class__.__name__)
        self.engine = create_engine(
            url=db_url,
            echo=db_echo,
            pool_size=10,
            max_overflow=10,
            poolclass=QueuePool,
            pool_timeout=timedelta(seconds=30).total_seconds(),
        )
        self.sessionmaker = sessionmaker(bind=self.engine)
        self.func_new_session_counter = 0
        self.async_engine = create_async_engine(
            url=async_db_url,
            echo=db_echo,
            pool_size=10,
            max_overflow=10,
            poolclass=AsyncAdaptedQueuePool,
            pool_timeout=timedelta(seconds=30).total_seconds()
        )
        self.async_sessionmaker = async_sessionmaker(bind=self.async_engine)
        self.func_new_async_session_counter = 0
        self.base_dbm = base_dbm

    def is_table_exists(self, table_name: str) -> bool:
        with self.engine.connect() as connection:
            inspector = inspect(connection)
            return table_name in inspector.get_table_names()

    def drop_celery_tables(self):
        with self.engine.connect() as connection:
            connection.execute(text("DROP TABLE IF EXISTS celery_tasksetmeta CASCADE;"))
            connection.execute(text("DROP TABLE IF EXISTS celery_taskmeta CASCADE;"))
            connection.commit()
            self._logger.info("celery tables were dropped")

    def remove_celery_tables_data(self):
        if not self.is_table_exists("celery_tasksetmeta"):
            self._logger.info("table celery_tasksetmeta not exists")
            return
        with self.engine.connect() as connection:
            connection.execute(text("DELETE FROM celery_tasksetmeta;"))
            connection.execute(text("DELETE FROM celery_taskmeta;"))
            connection.commit()
            self._logger.info("celery tables data were removed")

    def drop_alembic_tables(self):
        with self.engine.connect() as connection:
            connection.execute(text("DROP TABLE IF EXISTS alembic_version CASCADE;"))
            connection.execute(text("DROP TABLE IF EXISTS alembic_version CASCADE;"))
            connection.commit()
            self._logger.info("alembic_version tables were dropped")

    def remove_alembic_tables_data(self):
        if not self.is_table_exists("alembic_version"):
            self._logger.info("table alembic_version not exists")
            return
        with self.engine.connect() as connection:
            connection.execute(text("DELETE FROM alembic_version;"))
            connection.commit()
            self._logger.info("alembic tables data were removed")

    def init(self):
        self.base_dbm.metadata.create_all(bind=self.engine, checkfirst=True)
        self._logger.info("db was inited")

    def drop(self):
        self.base_dbm.metadata.drop_all(bind=self.engine, checkfirst=True)
        self._logger.info("db was dropped")

    def reinit(self):
        self.base_dbm.metadata.drop_all(bind=self.engine, checkfirst=True)
        self.base_dbm.metadata.create_all(bind=self.engine, checkfirst=True)
        self._logger.info("db was reinited")

    def check_conn(self):
        self.engine.connect()
        self._logger.info("db conn is good")

    def new_session(self, **kwargs) -> Session:
        self.func_new_session_counter += 1
        return self.sessionmaker(**kwargs)

    def new_async_session(self, **kwargs) -> AsyncSession:
        self.func_new_async_session_counter += 1
        return self.async_sessionmaker(**kwargs)

    def is_conn_good(self) -> bool:
        try:
            self.check_conn()
        except Exception as e:
            self._logger.error(e)
            return False
        return True

    def generate_unique_id(self, *, class_dbm: Any):
        with self.new_session() as session:
            res: int = session.query(func.max(class_dbm.id)).scalar()
            while session.query(class_dbm).filter(class_dbm.id == res).first() is not None:
                res += 1
        return res

    def generate_unique_long_id(self, *, class_dbm: Any):
        with self.new_session() as session:
            res: str = str(uuid4())
            while session.query(class_dbm).filter(class_dbm.long_id == res).first() is not None:
                res = str(uuid4())
        return res

    def generate_creation_dt(self) -> datetime:
        return now_utc_dt()


def __example():
    pass


async def __async_example():
    pass


if __name__ == '__main__':
    __example()
    asyncio.run(__async_example())
