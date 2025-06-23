import os


def get_database_url() -> str:
    """Construct the database URL from environment variables."""
    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "root")
    host = os.getenv("DB_HOST", "mysql")
    port = os.getenv("DB_PORT", "3306")
    db_name = os.getenv("DB_NAME", "appdb")
    return f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}"
