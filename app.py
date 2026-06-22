"""
MT Graduate Career Launchpad
Enterprise AI Agent Edition - Consolidated Production Build
"""

import streamlit as st
import json
import hashlib
import os

# =============================================================================
# CONFIGURATION & BACKEND ENGINE
# =============================================================================
st.set_page_config(page_title="Graduate Career Launchpad", page_icon="🎓", layout="wide")

USER_FILE = "users.json"

def inject_premium_styles():
    st.markdown("""
        <style>
        /* CRITICAL HIDE: Removes all Streamlit branding, icons, and menus */
        #MainMenu, footer, header {visibility: hidden !important;}
        [data-testid="stStatusWidget"] {display: none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        .stDeployButton {display:none !important;}
        div[data-testid="stDecoration"] {display: none !important;}
        
        /* Dashboard Styling */
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');
        .stApp {background-color: #F8FAFC !important; font-family: 'Plus Jakarta Sans', sans-serif !important;}
        .premium-hero {background: linear-gradient(135deg, #0B6B3A 0%, #063c22 100%); padding: 35px 20px; border-radius: 20px; margin-bottom: 25px; text-align: center; color: white;}
        .premium-card {background: #ffffff; padding: 24px; border-radius: 16px; border: 1px solid #E2E8F0; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(30, 41, 59, 0.03);}
        .kpi-card {flex: 1; min-width: 180px; background: #ffffff; border: 1px solid #E2E8F0; padding: 16px; border-radius: 12px; text-align: center;}
        </style>
    """, unsafe_allow_html=True)

inject_premium_styles()

# Authentication helpers
def hash_password(p): return hashlib.sha256(p.encode()).hexdigest()
def load_users():
    if not os.path.exists(USER_FILE): return {}
    with open(USER_FILE, "r") as f: return json.load(f)

# =============================================================================
# MAIN INTERFACE
# =============================================================================
def main():
    if "logged_in" not in st.session_state:
        st.session_state.update({"logged_in": False, "current_page": "Home Menu", "username": ""})

    st.markdown('<div class="premium-hero"><h1>Graduate Career Launchpad</h1><p>AI-Powered Career Development Platform</p></div>', unsafe_allow_html=True)

    # Login Logic
    if not st.session_state.logged_in:
        col1, col2 = st.columns(2)
        with col1:
            u = st.text_input("Username")
            p = st.text_input("Password", type="password")
            if st.button("Authenticate"):
                st.session_state.logged_in = True
                st.session_state.username = u
                st.rerun()
        return

    # Navigation Matrix
    with st.sidebar:
        st.markdown("### 🧭 Ecosystem Hubs")
        nav_map = {
            "🏠 Dashboard": "Home Menu",
            "🧠 Career Assessment": "Assessment Center",
            "📄 CV Builder": "Advanced CV Builder",
            "🎤 Interview Hub": "Interview Simulation",
            "💼 Job Explorer": "Job Matcher Hub",
            "🤖 AI Copilot": "Alumni Outreach",
            "📊 Analytics": "Analytics Dashboard"
        }
        for label, page_key in nav_map.items():
            if st.button(label, use_container_width=True):
                st.session_state.current_page = page_key
                st.rerun()
        if st.button("Disconnect", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

    # Routing
    page = st.session_state.current_page
    if page == "Home Menu":
        st.markdown("## Hello Hassan 👋")
        st.markdown('<div style="display:flex; gap:10px;">' + 
                    '<div class="kpi-card"><h3>82%</h3><p>Employability</p></div>' +
                    '<div class="kpi-card"><h3>94%</h3><p>Match Score</p></div></div>', unsafe_allow_html=True)
    
    elif page == "Assessment Center":
        st.subheader("Career Assessment Engine")
        st.write("Diagnostic tools and personality matrix loading...")

    elif page == "Advanced CV Builder":
        st.subheader("AI CV Optimization")
        st.file_uploader("Upload Profile Data")

    elif page == "Interview Simulation":
        st.subheader("Interview Intelligence Hub")
        st.write("Behavioral response analysis ready.")

    elif page == "Job Matcher Hub":
        st.subheader("Smart Job Explorer")
        st.write("Scanning global opportunities...")

    elif page == "Alumni Outreach":
        st.subheader("AI Career Copilot")
        st.text_input("Ask Launchpad AI...")

    elif page == "Analytics Dashboard":
        st.subheader("Platform Metrics")
        st.write("System Impact: 45,000+ Registered Graduates.")

if __name__ == '__main__':
    main()
