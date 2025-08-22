from sqlalchemy.sql import text
import pandas as pd

from src.utils.connecteur_db import ConnectDatabase


def test_connect_db():
    connector = ConnectDatabase()
    df = pd.read_sql_query(text("SELECT 1"), connector.engine)
    assert df.iloc[0, 0] == 1 
