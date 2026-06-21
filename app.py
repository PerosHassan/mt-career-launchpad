"""
MT Graduate Career Launchpad
Enterprise AI Agent Edition - Premium Design System (Green Theme)

Integrated with live Gemini AI Agent processing models. Contains upgraded
frontend typography, an inline CSS logo brand identity, and complete feature suites.
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
# FILE MANAGEMENT & CONFIGURATION (BACKEND DATA STORE)
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
# FRONTEND SYSTEM DESIGN (FONTS, LOGO, ACCENTS)
# =============================================================================
def inject_premium_styles():
    st.markdown("""
        <style>
        /* Import Professional Typography */
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
        
        /* Global Canvas Rules */
        .stApp {
            background: linear-gradient(180deg, #063c22 0%, #0d6137 40%, #f4f8f5 100%) !important;
            font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
            color: #1f2937;
        }
        
        /* Premium Branding / Logo Mark Geometry */
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
            letter-spacing: -0.5px;
        }
        
        /* Main Hero Presentation Wrapper */
        .premium-hero {
            text-align: center;
            padding: 30px 20px 20px 20px;
            color: white;
        }
        .premium-hero h1 {
            color: white !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: 42px !important;
            font-weight: 800 !important;
            letter-spacing: -1px;
            margin: 0 !important;
        }
        .premium-hero p.tagline {
            color: #a3e6be !important;
            font-size: 20px !important;
            font-weight: 400;
            margin-top: 4px !important;
            margin-bottom: 16px !important;
            letter-spacing: -0.2px;
        }
        
        /* Cards System */
        .premium-card {
            background: rgba(255, 255, 255, 0.98);
            padding: 24px;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.4);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05), 0 10px 10px -5px rgba(0, 0, 0, 0.02);
            margin-bottom: 24px;
            transition: transform 0.2s ease;
        }
        .premium-card h3 {
            color: #063c22 !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: 20px !important;
            font-weight: 700 !important;
            margin-top: 0 !important;
            margin-bottom: 10px !important;
        }
        .premium-card p {
            font-size: 14px !important;
            line-height: 1.5 !important;
            color: #4b5563 !important;
        }
        
        /* Global Button Layout Matrices */
        div.stButton > button {
            background: linear-gradient(90deg, #063c22 0%, #198754 100%) !important;
            color: white !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            border-radius: 12px !important;
            border: none !important;
            padding: 12px 24px !important;
            font-weight: 600 !important;
            font-size: 14px !important;
            box-shadow: 0 4px 14px rgba(6, 60, 34, 0.3) !important;
            transition: all 0.2s ease-in-out;
            width: 100%;
        }
        div.stButton > button:hover {
            transform: translateY(-1.5px);
            box-shadow: 0 6px 20px rgba(6, 60, 34, 0.45) !important;
            background: linear-gradient(90deg, #0d6137 0%, #1db972 100%) !important;
        }
        
        /* Forms & Interactive Fields */
        .stTextInput input, .stTextArea textarea, .stSelectbox div {
            border-radius: 12px !important;
            border: 1px solid #d1d5db !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
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
    if "cv_data_projects" not in st.session_state:
        st.session_state.cv_data_projects = ""

    # ---- BRAND IDENTITY & HERO HEADER ----
    st.markdown("""
        <div class="premium-hero">
            <div class="brand-container">
                <div class="logo-mark">MT</div>
                <h1>Graduate Career Launchpad</h1>
            </div>
            <p class="tagline">your professional profile, <span style="font-weight: 300; opacity: 0.9;">ready everywhere.</span></p>
            <p style="max-width: 600px; margin: 0 auto; font-size: 14px; opacity: 0.75;">
                Create a clean digital CV and personal workspace powered by live AI Agent analysis engines.
            </p>
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

    # ---- 1. CV BUILDER & OPTIMIZER MODULE ----
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
                "projects": st.session_state.cv_data_projects
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
                            response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                            st.markdown(f'<div style="background: #E8F5E9; border-left: 5px solid #063c22; padding: 20px; border-radius: 12px; margin-top:15px;">{response.text}</div>', unsafe_allow_html=True)
                        except Exception as e:
                            st.error(f"Agent analysis connection dropped: {str(e)}")
                    else:
                        st.warning("Ecosystem running on local preview mode. Add API key for live execution.")
            else:
                st.warning("Please supply both professional experience data and target job criteria values.")
        st.markdown('</div>', unsafe_allow_html=True)

    # ---- 2. INTERVIEW SIMULATION COACH MODULE ----
    elif st.session_state.current_page == "Interview Simulation":
        if st.button("← Back to System Dashboard Menu", key="ret_from_coach"):
            st.session_state.current_page = "Home Menu"
            st.rerun()
            
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown('<h3>🎙️ Live AI Behavioral Simulation Coach</h3>', unsafe_allow_html=True)
        st.write(f"**Target Position:** {st.session_state.cv_data_title if st.session_state.cv_data_title else 'General Candidate'}")
        
        question_type = st.selectbox("Select Interview Focus Metric", ["Behavioral (STAR Method)", "Technical / Domain Deep Dive", "Leadership & Conflict Resolution"])
        mock_question = st.text_area("Interview Question to Answer", value="Tell me about a time you encountered a severe technical roadblock or conflicting timeline challenge. How did you resolve it?", height=70)
        user_response = st.text_area("Type Your Response Stream Here", height=150, placeholder="Using the STAR method (Situation, Task, Action, Result), describe your action steps...")
        
        if st.button("Submit Response for Agent Evaluation", key="btn_eval_interview"):
            if user_response:
                with st.spinner("AI Coach analyzing core delivery structure..."):
                    if client:
                        try:
                            prompt = (
                                f"Act as an expert technical interviewer. Evaluate this candidate's response to the question: '{mock_question}'\n"
                                f"Candidate Target Role: {st.session_state.cv_data_title}\n"
                                f"Candidate Skills: {st.session_state.cv_data_skills}\n"
                                f"Candidate Answer: {user_response}\n\n"
                                f"Analyze if they utilized the STAR method properly. Highlight clear strengths, identify delivery gaps, and provide a perfectly restructured 'Ideal Revision' version of their answer."
                            )
                            response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                            st.markdown(f'<div style="background: #E8F5E9; border-left: 5px solid #063c22; padding: 20px; border-radius: 12px; margin-top:15px;">{response.text}</div>', unsafe_allow_html=True)
                        except Exception as e:
                            st.error(f"Error executing interview assessment: {str(e)}")
                    else:
                        st.warning("API key missing. Connect your token to run live evaluation frameworks.")
            else:
                st.warning("Please type your response before running evaluation parameters.")
        st.markdown('</div>', unsafe_allow_html=True)

    # ---- 3. JOB PLACEMENT MATRIX MODULE ----
    elif st.session_state.current_page == "Job Matcher Hub":
        if st.button("← Back to System Dashboard Menu", key="ret_from_matcher"):
            st.session_state.current_page = "Home Menu"
            st.rerun()
            
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown('<h3>🔍 Strategic Job Placement & Skill Match Matrix</h3>', unsafe_allow_html=True)
        st.write("Scan your core skill tokens against competitive market roles to map open gaps.")
        
        industry_focus = st.text_input("Target Industry Sector (e.g., FinTech, Healthcare, Enterprise AI, Agritech)", value="Technology")
        
        if st.button("Generate Tailored Job Placement Blueprint", key="btn_run_job_matcher"):
            with st.spinner("Mapping dynamic roles matrix pipelines..."):
                if client:
                    try:
                        prompt = (
                            f"Based on the following profile, map out 3 premium job descriptions/titles currently relevant in the {industry_focus} industry.\n"
                            f"Verified Title: {st.session_state.cv_data_title}\n"
                            f"Core Technical Stack: {st.session_state.cv_data_skills}\n"
                            f"Experience Block: {st.session_state.cv_data_exp}\n\n"
                            f"Format as an itemized breakdown. For each title provide: 1. Core Responsibilities, 2. Critical Skill gaps the user needs to study next, and 3. Suggested pipeline strategy."
                        )
                        response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                        st.markdown(f'<div style="background: #E8F5E9; border-left: 5px solid #063c22; padding: 20px; border-radius: 12px; margin-top:15px;">{response.text}</div>', unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Error searching match engine blueprints: {str(e)}")
                else:
                    st.warning("Ecosystem running on preview mode. Live API client required.")
        st.markdown('</div>', unsafe_allow_html=True)

    # ---- 4. OUTREACH ARCHITECTURE MODULE ----
    elif st.session_state.current_page == "Alumni Outreach":
        if st.button("← Back to System Dashboard Menu", key="ret_from_outreach"):
            st.session_state.current_page = "Home Menu"
            st.rerun()
            
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown('<h3>✉️ Enterprise Conversion Outreach Architecture</h3>', unsafe_allow_html=True)
        
        col_out1, col_out2 = st.columns(2)
        with col_out1:
            recipient_title = st.text_input("Recipient Professional Role (e.g., Talent Partner, Engineering Manager)", value="Hiring Manager")
            platform = st.selectbox("Target Communication Channel", ["LinkedIn InMail Template", "Cold Email Framework", "Alumni Referral Request"])
        with col_out2:
            company_target = st.text_input("Target Corporate Institution / Company", value="Target Organization")
            tone_style = st.selectbox("Tone Setting", ["Warm & Value-First", "Direct & Technical Corporate", "High-Impact Graduate Enthusiast"])
            
        if st.button("Generate High-Conversion Messaging Strategy", key="btn_gen_outreach"):
            with st.spinner("Compiling structural messaging frameworks..."):
                if client:
                    try:
                        prompt = (
                            f"Write a high-converting {platform} message from a candidate to a {recipient_title} at {company_target}.\n"
                            f"Candidate Name: {st.session_state.cv_data_name}\n"
                            f"Candidate Core Identity: {st.session_state.cv_data_title}\n"
                            f"Core Skills to Reference: {st.session_state.cv_data_skills}\n"
                            f"Tone Profile: {tone_style}\n\n"
                            f"Ensure it avoids boring cliches, clearly highlights why their experience matters, and leaves a sharp, professional call-to-action."
                        )
                        response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                        st.markdown(f'<div style="background: #E8F5E9; border-left: 5px solid #063c22; padding: 20px; border-radius: 12px; margin-top:15px;">{response.text}</div>', unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Error processing text generation: {str(e)}")
                else:
                    st.warning("Connect your live GEMINI_API_KEY to unlock dynamic generation engines.")
        st.markdown('</div>', unsafe_allow_html=True)

    # ---- 5. PORTFOLIO STUDIO MODULE ----
    elif st.session_state.current_page == "Branding & Portfolio":
        if st.button("← Back to System Dashboard Menu", key="ret_from_branding"):
            st.session_state.current_page = "Home Menu"
            st.rerun()
            
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown('<h3>📁 Professional Portfolio Asset Studio</h3>', unsafe_allow_html=True)
        
        st.session_state.cv_data_projects = st.text_area("Describe Your Live Projects / Repositories", value=st.session_state.cv_data_projects, height=120, placeholder="Project 1: System description, code stack, metrics and outcomes achieved...")
        
        if st.button("Optimize Project Descriptions for Behance/GitHub", key="btn_optimize_portfolio"):
            if st.session_state.cv_data_projects:
                with st.spinner("Polishing portfolio text layout matrices..."):
                    if client:
                        try:
                            prompt = (
                                f"You are a professional branding strategist. Optimize these technical project logs into a structured portfolio presentation suitable for GitHub Readmes or Behance project sheets.\n"
                                f"User Projects Info:\n{st.session_state.cv_data_projects}\n\n"
                                f"Reformat them with clear headings, clean feature bullet points, technical architecture breakdowns, and impact summaries."
                            )
                            response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                            st.markdown(f'<div style="background: #E8F5E9; border-left: 5px solid #063c22; padding: 20px; border-radius: 12px; margin-top:15px;">{response.text}</div>', unsafe_allow_html=True)
                        except Exception as e:
                            st.error(f"Portfolio agent connection lost: {str(e)}")
                    else:
                        st.warning("Please verify your API key configs to use live generation.")
            else:
                st.warning("Please fill in your current project notes first.")
        st.markdown('</div>', unsafe_allow_html=True)

    # ---- 6. ENVIRONMENT SYSTEM SETTINGS MODULE ----
    elif st.session_state.current_page == "Profile Config":
        if st.button("← Back to System Dashboard Menu", key="ret_from_cfg"):
            st.session_state.current_page = "Home Menu"
            st.rerun()
            
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown('<h3>⚙️ Secure Local Database & Environment Management</h3>', unsafe_allow_html=True)
        st.write(f"**Current Workspace Directory Reference:** `{os.getcwd()}`")
        st.write(f"**Active Instance Index Key:** `{current_user}`")
        
        if st.button("Check Local File Safety & Run Database Audit", key="btn_audit_db"):
            if os.path.exists(USER_FILE):
                st.success(f"File index verification: Local `{USER_FILE}` database path is healthy and functional.")
                with open(USER_FILE, "r") as f:
                    data = json.load(f)
                st.json({"Registered Profiles Index Count": len(data.keys()), "Active Security Handshakes": True})
            else:
                st.error("No centralized local database found. Run setup tasks to initialize.")
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
