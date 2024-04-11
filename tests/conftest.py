import pytest
from sqlmodel import create_engine, SQLModel
from pdfparser import sqlmodel
from sqlalchemy.orm import sessionmaker

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
