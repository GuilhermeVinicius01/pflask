import os
import psycopg2


def _pegar_url():
    for nome in ("POSTGRES_URL", "DATABASE_URL",
                 "STORAGE_POSTGRES_URL", "STORAGE_DATABASE_URL"):
        url = os.environ.get(nome)
        if url:
            return url
    return None


def get_connection():
    return psycopg2.connect(_pegar_url())