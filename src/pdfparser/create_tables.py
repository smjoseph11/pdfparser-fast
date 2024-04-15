from pdfparser.model import SQLModel
from sqlmodel import create_engine

from pdfparser import config
# Define the database connection URL

# Create a database engine and build tables
def create_tables():
    engine = create_engine(config.get_postgres_uri())
    SQLModel.metadata.create_all(engine)
    print("Tables created successfully!")
    return engine
