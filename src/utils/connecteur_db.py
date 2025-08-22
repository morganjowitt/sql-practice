from sqlalchemy import create_engine, inspect, text

import os
from dotenv import load_dotenv

import pandas as pd

load_dotenv(override=False)

class ConnectDatabase :

    def __init__(self) -> None:

        self.db_url = os.getenv("DATABASE_URL")
        self.engine = create_engine(
            self.db_url,
            future=True,
            pool_pre_ping=True
        )
    
    def tables(self, schema="public"):
        return inspect(self.engine).get_table_names(schema=schema)

    def query_df(self, sql: str, params=None):
        return pd.read_sql_query(text(sql), self.engine, params=params or {})
