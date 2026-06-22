import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Graduate Career Launchpad", layout="wide")

# --- CSS TO HIDE ICONS AND MANAGE APP ---
def inject_clean_styles():
    st.markdown("""
        <style>
        /* Hide Streamlit UI Chrome */
        #MainMenu, footer, header {visibility: hidden !important;}
        [data-testid="stStatusWidget"] {display: none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        .stDeployButton {display:none !important;}
        
        /* Dashboard Styling */
        .header-box { background: #0B6B3A; color: white; padding: 25px; border-radius: 15px; margin-bottom: 20px; }
        .job-card { background: white; border: 1px solid #E2E8F0; padding: 15px; border-radius: 10px; margin-bottom: 10px; }
        </style>
    """, unsafe_allow_html=True)

inject_clean_styles()

# --- HEADER ---
st.markdown("""
    <div class="header-box">
        <h1>🎓 Graduate Career Launchpad</h1>
        <p>AI-Powered Employability Ecosystem | Welcome Back, Hassan</p>
        <h3>Career Readiness Score: 82%</h3>
    </div>
""", unsafe_allow_html=True)

# --- METRICS (Using simple columns instead of charts to avoid TypeError) ---
c1, c2, c3 = st.columns(3)
c1.metric("Graduates", "1,250", "12%")
c2.metric("CVs Optimized", "3,800", "45%")
c3.metric("Interviews", "940", "8%")

st.subheader("Recommended Jobs")

# --- JOB CARDS ---
jobs = [("Project Coordinator", "94%"), ("Business Analyst", "89%")]
for title, score in jobs:
    st.markdown(f"""
    <div class="job-card">
        <h4>{title}</h4>
        <p>Match Score: <b>{score}</b></p>
        <button>Apply</button> <button>Save</button>
    </div>
    """, unsafe_allow_html=True)
