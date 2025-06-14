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

    # Keep only numeric columns for model training
    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()

    if not numeric_cols:
        st.error("No numeric columns available for training.")
        return

    # Target selection
    target = st.selectbox("Select target variable", numeric_cols)

    # Features selection
    features = st.multiselect("Select features", [col for col in numeric_cols if col != target])

    if st.button("Train Model"):
        if not features:
            st.warning("Please select at least one feature.")
            return
        try:
            X_train, X_test, y_train, y_test = train_test_split(
                df[features], df[target], test_size=0.2, random_state=42
            )
            model = RandomForestRegressor(n_estimators=100)
            model.fit(X_train, y_train)
            preds = model.predict(X_test)
            st.success(f"MAE: {mean_absolute_error(y_test, preds):.2f}")
            st.success(f"R²: {r2_score(y_test, preds):.2f}")
            st.session_state["model"] = model
        except Exception as e:
            st.error(f"Model training failed: {e}")
