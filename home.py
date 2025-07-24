import streamlit as st
import os

def show():
    # ✅ Load logo safely
    logo_path = "logo.png"
    if os.path.exists(logo_path):
        st.image(logo_path, width=100)
    else:
        st.warning("⚠️ Logo image not found. Please ensure 'logo.png' is in the root directory.")

    # ✅ App title and description
    st.title("🏡 NZ HomeEnergy AI")
    st.markdown("""
    Welcome to **NZ HomeEnergy AI** – an advanced ML-powered tool to help understand and predict **household energy use in New Zealand**.

    ---

    🔍 **What you can do:**
    - 📥 Upload your household energy data  
    - ⚙️ Train machine learning models  
    - 📊 Evaluate energy performance  
    - 🌿 Get recommendations for savings and sustainability

    ---

    ### 🌱 Aligned with UN Sustainable Development Goals (SDGs)
    This tool supports:
    - **SDG 7**: Affordable and Clean Energy  
    - **SDG 11**: Sustainable Cities and Communities  
    - **SDG 12**: Responsible Consumption and Production  
    - **SDG 13**: Climate Action  

    💡 *By using this tool, you’ll gain insights into energy usage and learn how to reduce carbon footprints at the household level.*
    """)
