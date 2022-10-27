import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from src.settings import get_settings


class InitDBCommand:

    def handle(self):
        settings = get_settings()

        con = psycopg2.connect(
            host=settings.postgres_host,
            user=settings.postgres_username,
            password=settings.postgres_password
        );
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
        cursor = con.cursor();
        cursor.execute(f"create database {settings.postgres_database};");