import streamlit as st
import requests

st.set_page_config(page_title="MT Graduate Career Launchpad", layout="wide")
st.title("MT Graduate Career Launchpad")

user_input = st.text_area("Paste your resume or job description here")

if st.button("Analyze with AI"):
    try:
        # Calls your backend service container
        response = requests.post("http://backend:8000/analyze", json={"text": user_input})
        if response.status_code == 200:
            st.write(response.json()['feedback'])
        else:
            st.error("Error connecting to the AI backend.")
    except Exception as e:
        st.error(f"System Error: {e}")
