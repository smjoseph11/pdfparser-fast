from sqlalchemy import create_engine

from pdfparser import config
from pdfparser.orm import Base

# Define the database connection URL

# Create a database engine
engine = create_engine(config.get_postgres_uri())

# Create all tables defined in the Base
Base.metadata.create_all(engine)

print("Tables created successfully!")
