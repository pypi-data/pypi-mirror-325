from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from ..config import settings
from ..models.models import Base


class Database:
    def __init__(self):
        self.engine = create_engine(
            f"sqlite:///{settings.DATA_DIR}/listings.db", echo=settings.DB_ECHO
        )
        self.SessionLocal = sessionmaker(bind=self.engine)

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    @contextmanager
    def get_session(self):
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()


db = Database()
db.create_tables()
