import streamlit as st

def show():
    st.set_page_config(page_title="NZ HomeEnergy AI", layout="wide")

    # Header with logo (optional: replace logo file path)
    col1, col2 = st.columns([1, 6])
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/3/3c/Flag_of_New_Zealand.svg", width=70)
    with col2:
        st.title("🏡 NZ HomeEnergy AI")

    st.markdown("""
Welcome to **NZ HomeEnergy AI** – an advanced ML-powered tool to help understand and predict **household energy use in New Zealand**.

---

🔍 **What you can do**:
- 📤 Upload your household energy data
- 🤖 Train machine learning models
- 📊 Evaluate energy performance
- 🌿 Get recommendations for savings and sustainability

---

### 🌱 Aligned with UN Sustainable Development Goals (SDGs)

This tool supports:
- **SDG 7**: Affordable and Clean Energy  
- **SDG 11**: Sustainable Cities and Communities  
- **SDG 12**: Responsible Consumption and Production  
- **SDG 13**: Climate Action  

---

💡 *By using this tool, you’ll gain insights into energy usage and learn how to reduce carbon footprints at the household level.*

---
""")
