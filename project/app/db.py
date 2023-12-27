import os

from sqlmodel import create_engine, SQLModel, Session


DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    # This creates [both db and tables](https://sqlmodel.tiangolo.com/tutorial/fastapi/simple-hero-api/#create-database-and-tables-on-startup)
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
