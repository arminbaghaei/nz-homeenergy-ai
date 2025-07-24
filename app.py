import streamlit as st
import home  # This assumes your file is named home.py

def main():
    st.set_page_config(page_title="NZ HomeEnergy AI", layout="wide")

    # Optional: sidebar navigation if you plan to add more pages later
    st.sidebar.title("📂 Navigation")
    page = st.sidebar.radio("Select a page", ["Home"])

    if page == "Home":
        home.show()

if __name__ == "__main__":
    main()
