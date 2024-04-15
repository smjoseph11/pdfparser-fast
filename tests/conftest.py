import pytest
from pdfparser import model, config as my_config
from sqlmodel import SQLModel, Session

from pdfparser.create_tables import create_tables

def pytest_configure(config):
    my_config.get_postgres_uri = lambda: "sqlite://"

# Creating an in-memory sqlite db for testing
@pytest.fixture(scope="function")
def session(engine):
    session = Session(engine)
    try:
        yield session
    finally:
        SQLModel.metadata.drop_all(engine)
@pytest.fixture(scope="function")
def engine():
    engine = create_tables()
    yield engine