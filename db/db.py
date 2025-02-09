from typing import Generator
from sqlmodel import Session, SQLModel, create_engine
from settings import settings

# We need to import the model to create the tables
from models import SensorData  # noqa

engine = create_engine(settings.sqlite_cloud_url)


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    try:
        SQLModel.metadata.create_all(engine)
    except Exception as e:
        print(
            "Creating tables automatically failed, try running `alembic upgrade head`."
        )
        raise e


if __name__ == "__main__":
    create_db_and_tables()
    print("Success")
