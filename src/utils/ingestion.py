import pandas as pd

class Ingestion : 

    def __init__(self) :
        pass

    def ingest_csv(self, connector, file_path, table_name, schema="public"):
        df = pd.read_csv(file_path)
        with connector.engine.begin() as conn :
            df.to_sql(
                    table_name,
                    con=conn,
                    if_exists="replace",
                    index=False,
                    schema=schema,
                )
        pass
