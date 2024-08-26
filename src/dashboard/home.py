from pathlib import Path

import pandas as pd
import streamlit as st
from loguru import logger

st.set_page_config(page_title="Company info", layout="wide", page_icon=":bar_chart:")
st.title("Company info")

# TODO: cleanup code, constants etc
file = Path("data/raw/company_info.jsonl").resolve()

logger.info(f"File exists {file.exists()}")

if not file.exists():
   logger.info(f"File not exists {file.exists()}")
else:
    df = pd.read_json(file, lines=True)
    df.columns = df.iloc[0]

    # Verwijder de eerste rij (die nu als kolomnamen is ingesteld)
    df = df[1:]

    # Herstel de index van de DataFrame
    df = df.reset_index(drop=True)
    df = df.dropna()

    if "dataframe" not in st.session_state:
        st.session_state.dataframe = df

    st.data_editor(df)