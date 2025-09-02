from src.utils.connecteur_db import ConnectDatabase
from src.utils.ingestion import Ingestion

from sqlalchemy import inspect 


def test_ingestion(tmp_path):

    connector = ConnectDatabase()
    ingestion = Ingestion()

    csv_file = tmp_path / "test.csv"
    csv_file.write_text("id,name,age\n1,Alice,30\n2,Bob,25\n")
    ingestion.ingest_csv(connector, csv_file, "test", schema="public")
    
    table_names = inspect(connector.engine).get_table_names(schema="public")
    assert "test" in table_names
    