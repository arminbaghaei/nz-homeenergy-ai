
import streamlit as st
from app import home, upload_data, model_train, predict

st.set_page_config(page_title="NZ HomeEnergy AI", layout="wide")
st.sidebar.title("🏠 NZ HomeEnergy AI")
page = st.sidebar.radio("Navigate", ["Home", "Upload Data", "Train Model", "Predict"])

if page == "Home":
    home.show()
elif page == "Upload Data":
    upload_data.show()
elif page == "Train Model":
    model_train.show()
elif page == "Predict":
    predict.show()
