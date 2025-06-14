
import streamlit as st
import home
import upload_data
import model_train
import predict

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
st.markdown("### 🌱 Aligned with UN Sustainable Development Goals (SDGs)")
st.markdown("""
This tool supports:
- **SDG 7**: Affordable and Clean Energy  
- **SDG 11**: Sustainable Cities and Communities  
- **SDG 12**: Responsible Consumption and Production  
- **SDG 13**: Climate Action  

By using this tool, users gain insights into energy usage and learn how to reduce carbon footprints at the household level.
""")
