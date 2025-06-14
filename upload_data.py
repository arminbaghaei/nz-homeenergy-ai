import streamlit as st
import pandas as pd

def show():
    st.header("📂 Upload Your Data")
    uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        st.dataframe(df.head())
        st.session_state["df"] = df
    else:
        st.info("Or use the sample Excel data below")
        try:
            sample_df = pd.read_excel("sample_household_energy.xlsx")
            st.dataframe(sample_df.head())
            st.session_state["df"] = sample_df
        except FileNotFoundError:
            st.error("Sample data file not found. Please make sure 'sample_household_energy.xlsx' is in the root directory.")
