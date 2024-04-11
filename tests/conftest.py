import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pdfparser.orm import Base


# Creating an in-memory sqlite db for testing
@pytest.fixture(scope="function")
def session():

    engine = create_engine("sqlite://")
    Session = sessionmaker(bind=engine, expire_on_commit=False)
    Base.metadata.create_all(engine)
    try:
        with Session() as session:
            yield session
    finally:
        Base.metadata.drop_all(engine)
