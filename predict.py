
import streamlit as st
import pandas as pd

def show():
    st.header("📈 Predict Energy Use")
    if "model" not in st.session_state:
        st.warning("Please train a model first.")
        return
    model = st.session_state["model"]
    st.subheader("Input data")
    input_data = {}
    for feature in model.feature_names_in_:
        input_data[feature] = st.number_input(f"{feature}", value=0.0)
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Energy Use: {prediction:.2f}")
