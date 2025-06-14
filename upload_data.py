
import streamlit as st
import pandas as pd

def show():
    st.header("📂 Upload Your Data")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())
        st.session_state["df"] = df
    else:
        st.info("Or use the sample data below")
sample_df = pd.read_csv("sample_energy_data.csv")
        st.dataframe(sample_df.head())
        st.session_state["df"] = sample_df
