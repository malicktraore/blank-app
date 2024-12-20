import streamlit as st
import pandas as pd




st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
def load_excel_data(file_path):
    df = pd.read_excel(file_path)
    return df