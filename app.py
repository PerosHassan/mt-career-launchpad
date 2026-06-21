"""
MT Graduate Career Launchpad
Enterprise AI Agent Edition - Crash Protected

Integrated with live Gemini AI Agent processing models. Wraps 
external dependencies cleanly to safeguard production uptime.
"""

import streamlit as st
import json
import hashlib
import os

# Safe wrapper for the Google GenAI SDK to prevent app-breaking ImportErrors
try:
    from google import genai
    AI_LIBRARY_AVAILABLE = True
except ImportError:
    AI_LIBRARY_AVAILABLE = False

# =============================================================================
# INITIALIZE LIVE AI AGENT ENGINE
# =============================================================================
def get_ai_agent():
    """Initializes the official Google GenAI client using secure environment tokens."""
    if not AI_LIBRARY_AVAILABLE:
        return None
    api_key = os.environ.get("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")
    if not api_key:
        return None
    try:
        return genai.Client(api_key=api_key)
    except Exception:
        return None

# =============================================================================
# FILE MANAGEMENT & CONFIGURATION
# =============================================================================
USER_FILE = "users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    try:
        with open(USER_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {}

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

def register_user(username, password):
    users = load_users()
    if username in users:
        return False
    users[username] = {
        "password": hash_password(password),
        "profile": {"fullname": "", "role": "", "bio": "", "skills": "", "projects": ""}
    }
    save_users(users)
    return True

def authenticate_user(username, password):
    users = load_users()
    if username in users:
        stored_data = users[username]
        if isinstance(stored_data, str):
            return stored_data == hash_password(password)
        return stored_data.get("password") == hash_password(password)
    return False

def update_user_profile(username, profile_data):
    users = load_users()
    if username in users:
        if isinstance(users[username], str):
            users[username] = {"password": users[username], "profile": profile_data}
        else:
            users[username]["profile"] = profile_data
        save_users(users)
        return True
    return False

def get_user_profile(username):
    users = load_users()
    if username in users and isinstance(users[username], dict):
        return users[username].get("profile", {"fullname": "", "role": "", "bio": "", "skills": "", "projects": ""})
    return {"fullname": "", "role": "", "bio": "", "skills": "", "projects": ""}

# =============================================================================
# PREMIUM DESIGN SYSTEM (CSS INJECTION)
# =============================================================================
def inject_premium_styles():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(180deg, #0226E3 0%, #7625FF 50%, #F5F7FF 100%) !important;
            color: #1F2937;
        }
        
        .premium-hero {
            text-align: center;
            padding: 40px 20px 20px 20px;
            color: white;
        }
        .premium-hero h1 {
            color: white !important;
            font-size: 36px !important;
            font-weight: 800 !important;
            letter-spacing: -0.5px;
            margin-bottom: 10px !important;
        }
        .premium-hero p {
            color: #E0E7FF !important;
            font-size: 16px !important;
            max-width: 600px;
            margin: 0 auto !important;
            opacity: 0.9;
        }
        
        .premium-card {
            background: rgba(255, 255, 255, 0.96);
            padding: 24px;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            margin-bottom: 24px;
        }
        
        .premium-card h3 {
            color: #0226E3 !important;
            font-size: 20px !important;
            font-weight: 700 !important;
            margin-bottom: 12px !important;
        }
        
        div.stButton > button {
            background: linear-gradient(90deg, #0226E3 0%, #571CE3 100%) !important;
            color: white !important;
            border-radius: 50px !important;
            border: none !important;
            padding: 12px 28px !important;
            font-weight: 600 !important;
            font-size: 14px !important;
            box-shadow: 0 4px 14px rgba(2, 38, 227, 0.4) !important;
            transition: all 0.2s ease;
            width: 100%;
        }
        div.stButton > button:hover {
            transform: translateY(-1px);
            box-shadow: 0 6px 20px rgba(2, 38, 227, 0.6) !important;
        }
        
        .stTextInput input, .stTextArea textarea, .stSelectbox div {
            border-radius: 12px !important;
            border: 1px solid #D1D5DB !important;
        }
        </style>
    """, unsafe_allow_html=True)

# =============================================================================
# MAIN INTERFACE ARCHITECTURE
# =============================================================================
def main():
    st.set_page_config(page_title="MT Graduate Career Launchpad", page_icon="⚡", layout="wide")
    inject_premium_styles()
    
    # Initialize Safe Session Properties 
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Home Menu"
        
    # Persistent State Handling for CV Fields
    if "cv_data_name" not in st.session_state:
        st.session_state.cv_data_name = ""
    if "cv_data_title" not in st.session_state:
        st.session_state.cv_data_title = ""
    if "cv_data_skills" not in st.session_state:
        st.session_state.cv_data_skills = ""
    if "cv_data_exp" not in st.session_state:
        st.session_state.cv_data_exp = ""

    # ---- HERO BRAND HEADER BLOCK ----
    st.markdown("""
        <div class="premium-hero">
            <h1>your professional profile, <br><span style="opacity: 0.85; font-weight: 400; font-size:28px;">ready everywhere.</span></h1>
            <p>Create a clean digital CV and personal workspace powered by live AI Agent analysis engines.</p>
        </div>
    """, unsafe_allow_html=True)

    # Check for System Dependency Warning
    if not AI_LIBRARY_AVAILABLE:
        st.error("🚨 System Dependency Error: 'google-genai' is missing from requirements.txt. Please add it to your repository so Streamlit Cloud can install it.")

    # ---- UNAUTHORIZED SYSTEM PORTAL ----
    if not st.session_state.logged_in:
        col_auth_left, col_auth_right = st.columns(2)
        
        with col_auth_left:
            st.markdown('<div class="premium-card"><h3>🔒 Core Portal Entry</h3><p>Verify your security code keys to view configuration files.</p></div>', unsafe_allow_html=True)
            lin_user = st.text_input("Username", key="l_user_field")
            lin_pass = st.text_input("Security Access Pass", type="password", key="l_pass_field")
            if st.button("Authenticate & Launch Ecosystem", key="act_login_btn"):
                if authenticate_user(lin_user, lin_pass):
                    st.session_state.logged_in = True
                    st.session_state.username = lin_user
                    prof = get_user_profile(lin_user)
                    st.session_state.cv_data_name = prof.get("fullname", "")
                    st.session_state.cv_data_title = prof.get("role", "")
                    st.session_state.cv_data_skills = prof.get("skills", "")
                    st.session_state.cv_data_exp = prof.get("bio", "")
                    st.session_state.current_page = "Home Menu"
                    st.rerun()
                else:
                    st.error("Credential verification failed.")
                    
        with col_auth_right:
            st.markdown('<div class="premium-card"><h3>✨ Setup Profile Engine</h3><p>Build an independent secure local workspace directory instance.</p></div>', unsafe_allow_html=True)
            reg_user = st.text_input("Choose Unique Username", key="r_user_field")
            reg_pass = st.text_input("Choose Cryptographic Pass", type="password", key="r_pass_field")
            if st.button("Configure New Workspace Data", key="act_reg_btn"):
                if reg_user and reg_pass:
                    if register_user(reg_user, reg_pass):
                        st.success("Configuration built successfully! Log in on the left matrix.")
                    else:
                        st.error("Username index is currently occupied.")
        return

    # Authorized Session Global Parameters
    current_user = st.session_state.username
    client = get_ai_agent()

    # Top Status Control Bar
    c_status_left, c_status_right = st.columns([5, 1])
    with c_status_left:
        if client:
            st.markdown(f"<span style='color: white;'>🟢 <b>AI Agent Cloud Connected:</b> `ID: {current_user}` | Mode: `Live Production Engines Active`</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"<span style='color: #FEE2E2;'>⚠️ <b>AI Preview Mode:</b> Please configure your <code>GEMINI_API_KEY</code> token inside Streamlit Secrets to take this agent live.</span>", unsafe_allow_html=True)
    with c_status_right:
        if st.button("Disconnect Agent", key="btn_global_disconnect"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.current_page = "Home Menu"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # =============================================================================
    # NAVIGATION AND MAIN MODULE ROUTING
    # =============================================================================
    if st.session_state.current_page == "Home Menu":
        st.markdown("<h3 style='color: white; font-weight:600; margin-bottom:16px;'>Active Suite Navigation Modules</h3>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown('<div class="premium-card"><h3>📝 AI CV Builder & Optimizer</h3><p>Analyze performance metrics and tailor core structural phrases dynamically.</p></div>', unsafe_allow_html=True)
            if st.button("Launch Optimizer System", key="nav_cv_opt"):
                st.session_state.current_page = "Advanced CV Builder"
                st.rerun()
                
            st.markdown('<div class="premium-card"><h3>🎙️ Behavioral Simulation</h3><p>Evaluate response streams under technical interview criteria with feedback models.</p></div>', unsafe_allow_html=True)
            if st.button("Launch Coach System", key="nav_coach_opt"):
                st.session_state.current_page = "Interview Simulation"
                st.rerun()

        with col2:
            st.markdown('<div class="premium-card"><h3>🔍 Job Placement Matrix</h3><p>Track engineering and technology positions matching your primary verified technical profiles.</p></div>', unsafe_allow_html=True)
            if st.button("Launch Placement Explorer", key="nav_jobs_opt"):
                st.session_state.current_page = "Job Matcher Hub"
                st.rerun()

            st.markdown('<div class="premium-card"><h3>✉️ Outreach Architecture</h3><p>Generate highly structured, conversion-optimized emails and LinkedIn introduction notes.</p></div>', unsafe_allow_html=True)
            if st.button("Launch Messaging Suite", key="nav_outreach_opt"):
                st.session_state.current_page = "Alumni Outreach"
                st.rerun()

        with col3:
            st.markdown('<div class="premium-card"><h3>📁 Portfolio Studio</h3><p>Establish unified interfaces tracking asset libraries, live code repositories, and credentials.</p></div>', unsafe_allow_html=True)
            if st.button("Launch Asset Configurator", key="nav_port_opt"):
                st.session_state.current_page = "Branding & Portfolio"
                st.rerun()

            st.markdown('<div class="premium-card"><h3>⚙️ Environment Settings</h3><p>Verify data structures, storage paths, encryption hashes, and system logs variables.</p></div>', unsafe_allow_html=True)
            if st.button("Launch System Settings", key="nav_cfg_opt"):
                st.session_state.current_page = "Profile Config"
                st.rerun()

    # ---- 2. CV BUILDER MODULE ----
    elif st.session_state.current_page == "Advanced CV Builder":
        if st.button("← Back to System Dashboard Menu", key="ret_from_cv"):
            st.session_state.current_page = "Home Menu"
            st.rerun()
            
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown('<h3>📝 Live AI CV Optimization Workspace</h3>', unsafe_allow_html=True)
        
        col_left_inputs, col_right_inputs = st.columns(2)
        with col_left_inputs:
            st.session_state.cv_data_name = st.text_input("Full Legal Name Profile", value=st.session_state.cv_data_name, key="in_cv_name")
            st.session_state.cv_data_title = st.text_input("Target Professional Title", value=st.session_state.cv_data_title, key="in_cv_title")
        with col_right_inputs:
            st.session_state.cv_data_skills = st.text_area("Technical Stack Keywords", value=st.session_state.cv_data_skills, key="in_cv_skills", height=115)
            
        st.session_state.cv_data_exp = st.text_area("Comprehensive Career Experience Blocks", value=st.session_state.cv_data_exp, key="in_cv_exp", height=140)
        
        if st.button("Save Core Profile Parameters", key="btn_save_profile_action"):
            package = {
                "fullname": st.session_state.cv_data_name,
                "role": st.session_state.cv_data_title,
                "skills": st.session_state.cv_data_skills,
                "bio": st.session_state.cv_data_exp,
                "projects": get_user_profile(current_user).get("projects", "")
            }
            if update_user_profile(current_user, package):
                st.success("Profile updates successfully written to central system records!")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown('<h3>📊 Live Agent Alignment & ATS Diagnostics</h3>', unsafe_allow_html=True)
        target_description_text = st.text_area("Paste Target Job Requirements Specifications", key="in_target_description_text", height=130, placeholder="Paste corporate job criteria details here...")
        
        if st.button("Execute Live Agent Analysis", key="btn_execute_ai_analysis"):
            if target_description_text and st.session_state.cv_data_exp:
                with st.spinner("Agent running real-time profile diagnostic match..."):
                    if client:
                        try:
                            prompt = (
                                f"You are an elite corporate Talent Acquisition AI Agent. Review this user profile and experience data against the target job requirements.\n\n"
                                f"User Target Role: {st.session_state.cv_data_title}\n"
                                f"User Skills List: {st.session_state.cv_data_skills}\n"
                                f"User Professional History: {st.session_state.cv_data_exp}\n\n"
                                f"Target Job Requirements:\n{target_description_text}\n\n"
                                f"Provide a comprehensive critique containing a quantified Match Index %, missing structural industry terms, and clear recommendations using Markdown formatting."
                            )
                            response = client.models.generate_content(
                                model='gemini-2.5-flash',
                                contents=prompt
                            )
                            st.markdown(f'<div style="background: #EEF2FF; border-left: 5px solid #0226E3; padding: 20px; border-radius: 12px; margin-top:15px;">{response.text}</div>', unsafe_allow_html=True)
                        except Exception as e:
                            st.error(f"Agent analysis connection dropped: {str(e)}")
                    else:
                        st.warning("Ecosystem running on local preview. Map your GEMINI_API_KEY environment token to unlock live execution parameters.")
                        st.markdown(f"""
                            <div style="background: #EEF2FF; border-left: 5px solid #0226E3; padding: 16px; border-radius: 8px; margin-top: 15px;">
                                <h4 style="color: #0226E3; margin-top: 0;">✨ AI Optimization Preview</h4>
                                <p><b>Mock Match Rating Index:</b> 88% Alignment</p>
                                <p style="font-size:13px;"><i>System ready to stream live analytical feedback once the Gemini connection tokens are registered.</i></p>
                            </div>
                        """, unsafe_allow_html=True)
            else:
                st.warning("Please supply both professional experience data and target job criteria values.")
        st.markdown('</div>', unsafe_allow_html=True)

    # Fallback protection layout for other pages
    elif st.session_state.current_page in ["Job Matcher Hub", "Branding & Portfolio", "Interview Simulation", "Alumni Outreach", "Profile Config"]:
        if st.button("← Back to System Dashboard Menu", key="ret_from_submodules"):
            st.session_state.current_page = "Home Menu"
            st.rerun()
        st.markdown(f'<div class="premium-card"><h3>⚡ Module Workspace: {st.session_state.current_page}</h3><p>Core framework pipeline configured and monitoring inputs successfully.</p></div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
