import streamlit as st
import requests

st.set_page_config(page_title="MT Graduate Career Launchpad", layout="wide")

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'Dashboard'

# Sidebar Navigation
with st.sidebar:
    st.header("⏱️ Ecosystem Hubs")
    if st.button("🏠 Dashboard"): st.session_state.page = 'Dashboard'
    if st.button("🧠 Career Assessment"): st.session_state.page = 'Career Assessment'
    if st.button("📄 CV Builder & Optimizer"): st.session_state.page = 'CV Builder'

# Main Page Logic
if st.session_state.page == 'Dashboard':
    st.title("Graduate Career Launchpad - Dashboard")
    
    with st.form(key='analysis_form'):
        user_input = st.text_area("Paste your resume here")
        submit_button = st.form_submit_button(label='Analyze with AI')

    if submit_button and user_input:
        with st.spinner('Analyzing...'):
            try:
                response = requests.post("http://backend:8000/analyze", json={"text": user_input})
                if response.status_code == 200:
                    st.success("Analysis Complete!")
                    st.write(response.json().get("feedback"))
            except Exception as e:
                st.error(f"Connection Error: {e}")
                
    # Metrics display
    col1, col2, col3 = st.columns(3)
    col1.metric("Employability Score", "82%")
    col2.metric("ATS Match", "88%")
    col3.metric("Badges", "11")

elif st.session_state.page == 'Career Assessment':
    st.title("🧠 Career Assessment")
    st.write("Assessment content goes here...")

elif st.session_state.page == 'CV Builder':
    st.title("📄 CV Builder & Optimizer")
    st.write("Optimization tools coming soon.")
