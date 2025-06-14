
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import pandas as pd

def show():
    st.header("⚙️ Train a Model")
    if "df" not in st.session_state:
        st.warning("Please upload data first.")
        return
    df = st.session_state["df"]
    target = st.selectbox("Select target variable", df.columns)
    features = st.multiselect("Select features", [col for col in df.columns if col != target])
    if st.button("Train Model"):
        X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)
        model = RandomForestRegressor(n_estimators=100)
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        st.success(f"MAE: {mean_absolute_error(y_test, preds):.2f}")
        st.success(f"R²: {r2_score(y_test, preds):.2f}")
        st.session_state["model"] = model
