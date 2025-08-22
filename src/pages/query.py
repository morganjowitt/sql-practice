import streamlit as st
from utils.connecteur_db import ConnectDatabase
from utils.ingestion import Ingestion

"""
# SQL Query App
"""

connector = ConnectDatabase()
ingestion = Ingestion()

engine = connector.engine

st.write("Tables disponibles :", connector.tables())

query = st.text_area("✍️ Entrez votre requête SQL ici :", "SELECT * FROM public.train LIMIT 10;")
result = connector.query_df(sql=query)

st.write(result)
