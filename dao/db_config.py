
import os
import psycopg2


def _pegar_url():
    nomes = (
        "POSTGRES_URL",
        "DATABASE_URL",
        "STORAGE_POSTGRES_URL",
        "STORAGE_DATABASE_URL",
    )

    for nome in nomes:
        url = os.environ.get(nome)

        if url:
            return url

    raise RuntimeError(
        "URL do PostgreSQL não encontrada. "
        "Configure POSTGRES_URL ou DATABASE_URL."
    )


def get_connection():
    url = _pegar_url()
    return psycopg2.connect(url)