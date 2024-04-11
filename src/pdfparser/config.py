import os


def get_postgres_uri():
    host = "postgres"
    port = 5432
    password = os.environ.get("POSTGRES_PASSWORD", "fake_password")
    user, db_name = os.environ.get("POSTGRES_USER", "fake_user"), os.environ.get("POSTGRES_DB", "docs")
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"
