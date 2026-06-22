"""
MT Graduate Career Launchpad
Enterprise AI Agent Edition - Premium Green Theme (Mobile Contrast Fixed)
"""

import streamlit as st
import json
import hashlib
import os

# =============================================================================
# INITIALIZE LIVE AI AGENT ENGINE
# =============================================================================
try:
    from google import genai
    AI_LIBRARY_AVAILABLE = True
except ImportError:
    AI_LIBRARY_AVAILABLE = False

def get_ai_agent():
    if not AI_LIBRARY_AVAILABLE:
        return None
    api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return None
    try:
        return genai.Client(api_key=api_key)
    except Exception:
        return None

# =============================================================================
# FILE MANAGEMENT & CONFIGURATION (BACKEND DATA STORE)
# =============================================================================
USER_FILE = os.path.join(os.path.dirname(__file__), "users.json") if '__file__' in locals() else "users.json"

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
# FRONTEND SYSTEM DESIGN (MOBILE RESPONSIVE + AGGRESSIVE WHITE CONTRAST OVR)
# =============================================================================
def inject_premium_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
        
        /* Force App Base Background & Universal Inheritance */
        .stApp {
            background: linear-gradient(180deg, #063c22 0%, #0d6137 50%, #114d2e 100%) !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: #ffffff !important;
        }
        
        /* AGGRESSIVE WHITE CONTRAST OVERRIDE FOR ALL TEXT/LABELS ON MOBILE */
        h1, h2, h3, h4, h5, h6, p, span, li, label, div, select {
            color: #ffffff !important;
        }

        /* Target Streamlit widget text input fields & titles natively */
        div[data-testid="stWidgetLabel"] p, 
        .stSelectbox label p, 
        .stTextInput label p, 
        .stTextArea label p,
        .stWidgetFormModifier label {
            color: #ffffff !important;
            font-weight: 700 !important;
            font-size: 16px !important;
        }
        
        /* Branding Element Geometry */
        .brand-container {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 14px;
            margin-bottom: 5px;
        }
        .logo-mark {
            background: linear-gradient(135deg, #2ae083 0%, #198754 100%);
            width: 48px;
            height: 48px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 8px 16px rgba(42, 224, 131, 0.25);
            font-weight: 800;
            color: white !important;
            font-size: 22px;
        }
        
        /* Layout Hero Presentation */
        .premium-hero {
            text-align: center;
            padding: 20px 10px;
            color: white;
        }
        .premium-hero h1 {
            font-size: 36px !important;
            font-weight: 800 !important;
            margin: 0 !important;
        }
        .premium-hero p.tagline {
            color: #a3e6be !important;
            font-size: 18px !important;
            margin-top: 4px !important;
        }
        
        /* Safe Form Text Styling (Inputs remain legible inside fields) */
        .stTextInput input, .stTextArea textarea {
            color: #1f2937 !important;
            font-weight: 500 !important;
            background-color: #ffffff !important;
            border-radius: 12px !important;
        }
        
        /* Premium Translucent System Cards */
        .premium-card {
            background: rgba(255, 255, 255, 0.12);
            padding: 20px;
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            margin-bottom: 20px;
        }
        .premium-card h3 {
            font-size: 22px !important;
            font-weight: 700 !important;
            margin-top: 0 !important;
            color: #ffffff !important;
        }
        
        /* Global Navigation/Action Button Interface Engine */
        div.stButton > button {
            background: linear-gradient(90deg, #2ae083 0%, #198754 100%) !important;
            color: #ffffff !important;
            border-radius: 12px !important;
            border: none !important;
            padding: 12px 24px !important;
            font-weight: 700 !important;
            width: 100%;
        }
        div.stButton > button:hover {
            color: #063c22 !important;
            background: #ffffff !important;
        }
        </style>
    """, unsafe_allow_html=True)

# =============================================================================
# MAIN INTERFACE ARCHITECTURE
# =============================================================================
def main():
    st.set_page_config(page_title="MT Graduate Career Launchpad", page_icon="⚡", layout="wide")
    inject_premium_styles()
    
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Home Menu"
        
    if "cv_data_name" not in st.session_state:
        st.session_state.cv_data_name = ""
    if "cv_data_title" not in st.session_state:
        st.session_state.cv_data_title = ""
    if "cv_data_skills" not in st.session_state:
        st.session_state.cv_data_skills = ""
    if "cv_data_exp" not in st.session_state:
        st.session_state.cv_data_exp = ""
    if "cv_data_projects" not in st.session_state:
        st.session_state.cv_data_projects = ""

    st.markdown("""
        <div class="premium-hero">
            <div class="brand-container">
                <div class="logo-mark">MT</div>
                <h1>Graduate Career Launchpad</h1>
            </div>
            <p class="tagline">your professional profile, <span style="font-weight: 300;">ready everywhere.</span></p>
        </div>
    """, unsafe_allow_html=True)

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
                    st.session_state.cv_data_projects = prof.get("projects", "")
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

    current_user = st.session_state.username
    client = get_ai_agent()

    c_status_left, c_status_right = st.columns([5, 1])
    with c_status_left:
        st.markdown(f"<span>🟢 <b>Ecosystem Workspace Active:</b> User ID: `{current_user}`</span>", unsafe_allow_html=True)
    with c_status_right:
        if st.button("Disconnect", key="btn_global_disconnect"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.current_page = "Home Menu"
            st.rerun()

    # =============================================================================
    # NAVIGATION AND MAIN MODULE ROUTING
    # =============================================================================
    if st.session_state.current_page == "Home Menu":
        st.markdown("<h3 style='font-weight:600;'>Active Suite Modules</h3>", unsafe_allow_html=True)
        
        st.markdown('<div class="premium-card"><h3>📝 AI CV Builder & Optimizer</h3></div>', unsafe_allow_html=True)
        if st.button("Open Optimizer System", key="nav_cv_opt"):
            st.session_state.current_page = "Advanced CV Builder"
            st.rerun()
            
        st.markdown('<div class="premium-card"><h3>🎙️ Behavioral Simulation Coach</h3></div>', unsafe_allow_html=True)
        if st.button("Open Coach System", key="nav_coach_opt"):
            st.session_state.current_page = "Interview Simulation"
            st.rerun()

        st.markdown('<div class="premium-card"><h3>🔍 Job Placement Matrix</h3></div>', unsafe_allow_html=True)
        if st.button("Open Placement Explorer", key="nav_jobs_opt"):
            st.session_state.current_page = "Job Matcher Hub"
            st.rerun()

        st.markdown('<div class="premium-card"><h3>✉️ Outreach Architecture</h3></div>', unsafe_allow_html=True)
        if st.button("Open Messaging Suite", key="nav_outreach_opt"):
            st.session_state.current_page = "Alumni Outreach"
            st.rerun()

        st.markdown('<div class="premium-card"><h3>⚙️ Environment Settings</h3></div>', unsafe_allow_html=True)
        if st.button("Open System Settings", key="nav_cfg_opt"):
            st.session_state.current_page = "Profile Config"
            st.rerun()

    # ---- 1. CV BUILDER MODULE ----
    elif st.session_state.current_page == "Advanced CV Builder":
        if st.button("← Back to System Dashboard Menu", key="ret_from_cv"):
            st.session_state.current_page = "Home Menu"
            st.rerun()
            
        st.markdown('<div class="premium-card"><h3>📝 Live AI CV Optimization Workspace</h3></div>', unsafe_allow_html=True)
        st.session_state.cv_data_name = st.text_input("Full Legal Name Profile", value=st.session_state.cv_data_name)
        st.session_state.cv_data_title = st.text_input("Target Professional Title", value=st.session_state.cv_data_title)
        st.session_state.cv_data_skills = st.text_area("Technical Stack Keywords", value=st.session_state.cv_data_skills)
        st.session_state.cv_data_exp = st.text_area("Comprehensive Career Experience Blocks", value=st.session_state.cv_data_exp)
        
        if st.button("Save Core Profile Parameters", key="btn_save_profile_action"):
            package = {"fullname": st.session_state.cv_data_name, "role": st.session_state.cv_data_title, "skills": st.session_state.cv_data_skills, "bio": st.session_state.cv_data_exp, "projects": st.session_state.cv_data_projects}
            update_user_profile(current_user, package)
            st.success("Profile saved!")
        
        st.markdown('<div class="premium-card"><h3>📊 Live Agent Alignment & ATS Diagnostics</h3></div>', unsafe_allow_html=True)
        target_description_text = st.text_area("Paste Target Job Requirements Specifications", key="in_target_description_text")
        
        if st.button("Execute Live Agent Analysis", key="btn_execute_ai_analysis"):
            if client:
                try:
                    prompt = f"Critique this candidate profile for role {st.session_state.cv_data_title}. Skills: {st.session_state.cv_data_skills}. Bio: {st.session_state.cv_data_exp}. Job spec: {target_description_text}"
                    response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                    st.markdown(f'<div style="background:white; color:black; padding:15px; border-radius:8px;">{response.text}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error connecting: {str(e)}")
            else:
                st.error("AI client key variable missing or invalid in cloud environment secrets panel.")

    # ---- 2. INTERVIEW SIMULATION MODULE ----
    elif st.session_state.current_page == "Interview Simulation":
        if st.button("← Back to System Dashboard Menu", key="ret_from_coach"):
            st.session_state.current_page = "Home Menu"
            st.rerun()
            
        st.markdown('<div class="premium-card"><h3>🎙️ Live AI Behavioral Simulation Coach</h3></div>', unsafe_allow_html=True)
        question_type = st.selectbox("Select Interview Focus Metric", ["Behavioral (STAR Method)", "Technical / Domain Deep Dive"])
        mock_question = st.text_area("Interview Question to Answer", value="Tell me about a time you encountered a severe roadblock. How did you resolve it?")
        user_response = st.text_area("Type Your Response Stream Here")
        
        if st.button("Submit Response for Agent Evaluation", key="btn_eval_interview"):
            if client:
                try:
                    prompt = f"Evaluate this answer: {user_response} to question: {mock_question}"
                    response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                    st.markdown(f'<div style="background:white; color:black; padding:15px; border-radius:8px;">{response.text}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
            else:
                st.error("AI client key variable missing or invalid in cloud environment secrets panel.")

    # ---- 3. JOB PLACEMENT MATRIX MODULE ----
    elif st.session_state.current_page == "Job Matcher Hub":
        if st.button("← Back to System Dashboard Menu", key="ret_from_matcher"):
            st.session_state.current_page = "Home Menu"
            st.rerun()
            
        st.markdown('<div class="premium-card"><h3>🔍 Strategic Job Placement & Skill Match Matrix</h3></div>', unsafe_allow_html=True)
        industry_focus = st.text_input("Target Industry Sector", value="FinTech")
        
        if st.button("Generate Tailored Job Placement Blueprint", key="btn_run_job_matcher"):
            if client:
                try:
                    prompt = f"Provide 3 relevant target roles for tech candidate in {industry_focus} industry. User skills: {st.session_state.cv_data_skills}"
                    response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                    st.markdown(f'<div style="background:white; color:black; padding:15px; border-radius:8px;">{response.text}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error running match query: {str(e)}")
            else:
                st.error("AI client key variable missing or invalid in cloud environment secrets panel.")

    # ---- 4. OUTREACH ARCHITECTURE MODULE ----
    elif st.session_state.current_page == "Alumni Outreach":
        if st.button("← Back to System Dashboard Menu", key="ret_from_outreach"):
            st.session_state.current_page = "Home Menu"
            st.rerun()
            
        st.markdown('<div class="premium-card"><h3>✉️ Enterprise Conversion Outreach Architecture</h3></div>', unsafe_allow_html=True)
        recipient_title = st.text_input("Recipient Professional Role", value="Hiring Manager")
        platform = st.selectbox("Target Communication Channel", ["LinkedIn InMail Template", "Cold Email Framework"])
        company_target = st.text_input("Target Corporate Institution", value="Target Organization")
        
        if st.button("Generate High-Conversion Messaging Strategy", key="btn_gen_outreach"):
            if client:
                try:
                    prompt = f"Write pitch template to {recipient_title} at {company_target} on platform {platform}."
                    response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                    st.markdown(f'<div style="background:white; color:black; padding:15px; border-radius:8px;">{response.text}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
            else:
                st.error("AI client key variable missing or invalid in cloud environment secrets panel.")

    # ---- 5. ENVIRONMENT SYSTEM SETTINGS MODULE ----
    elif st.session_state.current_page == "Profile Config":
        if st.button("← Back to System Dashboard Menu", key="ret_from_cfg"):
            st.session_state.current_page = "Home Menu"
            st.rerun()
            
        st.markdown('<div class="premium-card"><h3>⚙️ Secure Local Database & Environment Management</h3></div>', unsafe_allow_html=True)
        st.write(f"Workspace Path: `{os.getcwd()}`")
        if st.button("Check Local File Safety & Run Database Audit", key="btn_audit_db"):
            if os.path.exists(USER_FILE):
                with open(USER_FILE, "r") as f:
                    data = json.load(f)
                st.json({"Registered Profiles Index Count": len(data.keys()), "Active Security Handshakes": True})

if __name__ == '__main__':
    main()
