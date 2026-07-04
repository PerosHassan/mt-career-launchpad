import streamlit as st
import requests

# Set page to wide to match your reference design
st.set_page_config(page_title="MT Graduate Career Launchpad", layout="wide")

# Sidebar navigation
with st.sidebar:
    st.header("⏱️ Ecosystem Hubs")
    # Using buttons for navigation
    st.button("🏠 Dashboard")
    st.button("🧠 Career Assessment")
    st.button("📄 CV Builder & Optimizer")

# Main Dashboard Content
st.title("Graduate Career Launchpad")

# Input Section - Using a form for faster interaction
with st.form(key='analysis_form'):
    user_input = st.text_area("Paste your resume or job description here")
    submit_button = st.form_submit_button(label='Analyze with AI')

# Backend Interaction Logic
if submit_button and user_input:
    with st.spinner('Analyzing...'): # Keeps the UI responsive while waiting
        try:
            # Connects to your FastAPI backend container
            response = requests.post("http://backend:8000/analyze", json={"text": user_input})
            if response.status_code == 200:
                result = response.json()
                st.success("Analysis Complete!")
                st.write(result.get("feedback"))
            else:
                st.error("Backend error: Could not connect.")
        except Exception as e:
            st.error(f"Connection error: {e}")

# Metrics Section (Modern Look)
col1, col2, col3 = st.columns(3)
col1.metric("Employability Score", "82%")
col2.metric("ATS Match", "88%")
col3.metric("Badges", "11")

