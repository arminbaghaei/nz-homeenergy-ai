import streamlit as st
import home
import upload_data
import model_train
import predict

PAGES = {
    "🏠 Home": home,
    "📤 Upload Data": upload_data,
    "🧠 Train Model": model_train,
    "📈 Predict": predict
}

def main():
    st.set_page_config(page_title="NZ HomeEnergy AI", layout="wide")
    st.sidebar.title("📂 Navigation")
    selection = st.sidebar.radio("Select a page", list(PAGES.keys()))
    page = PAGES[selection]
    page.show()

if __name__ == "__main__":
    main()
