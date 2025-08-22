import streamlit as st
from utils.connecteur_db import ConnectDatabase
from utils.ingestion import Ingestion
from pathlib import Path

"""
# SQL Query App
"""

connector = ConnectDatabase()
ingestion = Ingestion()

uploaded_file = st.file_uploader("Sélectionnez un fichier CSV", type=["csv"])

if uploaded_file is not None:
    table_name = Path(uploaded_file.name).stem
    try:
        ingestion.ingest_csv(connector=connector, file_path=uploaded_file, table_name=table_name)
        st.success("Fichier ingéré avec succès !")

    except Exception as e :
        st.error(f"Erreur : {e}")
