import pytest
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine

from pdfparser import model


# Creating an in-memory sqlite db for testing
@pytest.fixture(scope="function")
def session():

    engine = create_engine("sqlite://")
    Session = sessionmaker(bind=engine, expire_on_commit=False)
    SQLModel.metadata.create_all(engine)
    try:
        with Session() as session:
            yield session
    finally:
        SQLModel.metadata.drop_all(engine)
