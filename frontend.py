import streamlit as st
import requests

# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="MT Graduate Career Launchpad",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------
# Custom CSS
# ---------------------------------------

st.markdown("""
<style>

.main {
    background-color:#F8FAFC;
}

h1,h2,h3{
    color:#0F172A;
}

.metric-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}

.stButton>button{
    width:100%;
    border-radius:10px;
    height:45px;
    background:#2563EB;
    color:white;
    border:none;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1D4ED8;
}

.sidebar-title{
    text-align:center;
    font-size:24px;
    font-weight:bold;
    color:#2563EB;
}

.small-text{
    text-align:center;
    color:gray;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------
# Session State
# ---------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# ---------------------------------------
# Sidebar
# ---------------------------------------

with st.sidebar:

    st.markdown(
        "<div class='sidebar-title'>🚀 MT Career Launchpad</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='small-text'>Launch Your Career With AI</div>",
        unsafe_allow_html=True
    )

    st.divider()

    if st.button("🏠 Dashboard"):
        st.session_state.page = "Dashboard"

    if st.button("🤖 AI Resume Analyzer"):
        st.session_state.page = "Resume"

    if st.button("🧠 Career Assessment"):
        st.session_state.page = "Assessment"

    if st.button("📄 CV Builder"):
        st.session_state.page = "CV"

    if st.button("🎯 Career Roadmap"):
        st.session_state.page = "Roadmap"

    if st.button("💼 Job Recommendations"):
        st.session_state.page = "Jobs"

    if st.button("📚 Learning Hub"):
        st.session_state.page = "Learning"

    if st.button("⚙️ Settings"):
        st.session_state.page = "Settings"

    st.divider()

    st.success("🟢 System Online")

# ---------------------------------------
# Dashboard Header
# ---------------------------------------

st.title("🚀 MT Graduate Career Launchpad")

st.caption("Powered by Google Gemini AI")

st.markdown("---")
