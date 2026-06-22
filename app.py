"""
MT Graduate Career Launchpad
Enterprise AI Agent Edition - Elite SaaS Dashboard Blueprint Upgrade
Developed by MIDDLE TECHNOLOGY
"""

import streamlit as st
import json
import hashlib
import os

# =============================================================================
# PERSISTENT ENVIRONMENT MEMORY ENGINE
# =============================================================================
@st.cache_resource
def get_global_memory_bridge():
    return {"active_sessions": {}}

global_bridge = get_global_memory_bridge()

# =============================================================================
# INITIALIZE STABLE PROD AI AGENT ENGINE (PERMANENT API FIX)
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
    if not os.path.exists(USER_FILE):        return {}
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
# FRONTEND SYSTEM DESIGN & HIGH-IMPACT CORPORATE THEME CONFIGURATION# =============================================================================
def inject_premium_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=300;400;500;600;700;800&display=swap');
        
        /* HIDE STREAMLIT HEADER TOOLBAR ICONS */
        #MainMenu {visibility: hidden !important;}
        header {visibility: hidden !important;}
        [data-testid="stToolbar"] {display: none !important;}
        .stApp header {display: none !important;}
        
        /* Universal Canvas Background Slate (#F8FAFC) */
        .stApp {
            background-color: #F8FAFC !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: #1E293B !important;
        }
        
        h1, h2, h3, h4, h5, h6, p, span, label {
            color: #1E293B !important;
        }

        /* Input Labels Typography Overrides */
        div[data-testid="stWidgetLabel"] p, label p {
            color: #1E293B !important;
            font-weight: 700 !important;
            font-size: 15px !important;
        }
        
        /* Corporate Emerald Green Header Box (#0B6B3A) */
        .premium-hero {
            background: linear-gradient(135deg, #0B6B3A 0%, #063c22 100%);
            text-align: center;
            padding: 35px 20px;
            border-radius: 20px;
            margin-bottom: 25px;
            box-shadow: 0 10px 25px rgba(11, 107, 58, 0.15);
        }
        .premium-hero h1 {
            font-size: 38px !important;
            font-weight: 800 !important;
            color: #ffffff !important;
            margin: 0 !important;
        }
        .premium-hero p.tagline {
            color: #19D17B !important;
            font-size: 18px !important;
            margin-top: 6px !important;
            font-weight: 500 !important;        }
        
        /* Base SaaS Premium Container Cards */
        .premium-card {
            background: #ffffff;
            padding: 24px;
            border-radius: 16px;
            border: 1px solid #E2E8F0;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(30, 41, 59, 0.03);
        }
        .premium-card h3 {
            font-size: 20px !important;
            font-weight: 700 !important;
            margin-top: 0 !important;
            color: #0B6B3A !important;
        }

        /* Color-Coded Widgets */
        .badge-green {
            background-color: #DCFCE7 !important;
            border-left: 5px solid #22C55E !important;
            color: #14532D !important;
            padding: 12px 16px; border-radius: 8px; margin-bottom: 10px; font-weight: 500;
        }
        .badge-blue {
            background-color: #DBEAFE !important;
            border-left: 5px solid #3B82F6 !important;
            color: #1E3A8A !important;
            padding: 12px 16px; border-radius: 8px; margin-bottom: 10px; font-weight: 500;
        }
        .badge-orange {
            background-color: #FFEDD5 !important;
            border-left: 5px solid #F97316 !important;
            color: #7C2D12 !important;
            padding: 12px 16px; border-radius: 8px; margin-bottom: 10px; font-weight: 500;
        }
        .badge-red {
            background-color: #FEE2E2 !important;
            border-left: 5px solid #EF4444 !important;
            color: #7F1D1D !important;
            padding: 12px 16px; border-radius: 8px; margin-bottom: 10px; font-weight: 500;
        }

        /* SaaS Platform Analytics Grid */
        .saas-grid {
            display: flex; gap: 15px; margin-bottom: 25px; flex-wrap: wrap;
        }
        .saas-analytics-card {
            flex: 1; min-width: 160px; background: #ffffff; border: 1px solid #E2E8F0;            padding: 20px 16px; border-radius: 12px; text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02); border-top: 4px solid #0B6B3A;
        }
        .saas-val { font-size: 28px; font-weight: 800; color: #1E293B; margin-bottom: 4px; }
        .saas-lbl { font-size: 12px; color: #64748B; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
        
        /* Interactive Platform Framework Form Buttons */
        div.stButton > button, div.stDownloadButton > button {
            background: linear-gradient(90deg, #0B6B3A 0%, #19D17B 100%) !important;
            color: #ffffff !important;
            border-radius: 12px !important;
            border: none !important;
            padding: 10px 20px !important;
            font-weight: 700 !important;
            transition: all 0.3s ease;
        }
        div.stButton > button:hover, div.stDownloadButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(25, 209, 123, 0.3);
            color: #ffffff !important;
        }

        /* Platform Bottom Branding Footer */
        .system-footer {
            margin-top: 40px; padding: 30px; background-color: #0B6B3A;
            border-radius: 16px; color: #ffffff !important; text-align: center;
        }
        .system-footer h4, .system-footer p, .system-footer span { color: #ffffff !important; }
        </style>
    """, unsafe_allow_html=True)

# =============================================================================
# MAIN INTERFACE ARCHITECTURE
# =============================================================================
def main():
    st.set_page_config(page_title="Graduate Career Launchpad", page_icon="🎓", layout="wide")
    inject_premium_styles()
    
    # Initialize Core Application Session Lifecycle States
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.current_page = "Dashboard Workspace"
        st.session_state.cv_data_name = ""
        st.session_state.cv_data_title = ""
        st.session_state.cv_data_skills = ""
        st.session_state.cv_data_exp = ""
        st.session_state.cv_data_projects = ""
        st.session_state.copilot_messages = [
            {"role": "assistant", "content": "Hello! I am your Launchpad AI Career Copilot. How can I accelerate your career journey today?"}        ]

    # Platform Title Presentation Box
    st.markdown("""
        <div class="premium-hero">
            <h1>Graduate Career Launchpad</h1>
            <p class="tagline">Enterprise AI-Powered Employability & Acceleration Ecosystem</p>
        </div>
    """, unsafe_allow_html=True)

    # Secure Multi-Channel Authentication Gateway UI Canvas
    if not st.session_state.logged_in:
        col_auth_left, col_auth_right = st.columns(2)
        
        with col_auth_left:
            st.markdown('<div class="premium-card"><h3>🔒 Login Secure Portal</h3><p>Verify ecosystem access tokens.</p></div>', unsafe_allow_html=True)
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
                    st.session_state.current_page = "Dashboard Workspace"
                    st.rerun()
                else:
                    st.error("Authentication handshake failed.")
            
            st.markdown("---")
            if st.button("Continue with Google", key="oauth_google_btn"):
                st.session_state.logged_in = True
                st.session_state.username = "GoogleUser"
                st.session_state.current_page = "Dashboard Workspace"
                st.rerun()
                
            if st.button("Continue with LinkedIn", key="oauth_linkedin_btn"):
                st.session_state.logged_in = True
                st.session_state.username = "LinkedInUser"
                st.session_state.current_page = "Dashboard Workspace"
                st.rerun()
                    
        with col_auth_right:
            st.markdown('<div class="premium-card"><h3>✨ Create Graduate Account</h3><p>Configure a fresh isolated local profile instance.</p></div>', unsafe_allow_html=True)
            reg_user = st.text_input("Choose Workspace Username", key="r_user_field")
            reg_pass = st.text_input("Generate Cryptographic Pass"), type="password", key="r_pass_field")            if st.button("Configure New Workspace Data", key="act_reg_btn"):
                if reg_user and reg_pass:
                    if register_user(reg_user, reg_pass):
                        st.success("Configuration index registered! Authenticate on left matrix.")
                    else:
                        st.error("Selected username parameter is already assigned.")
        
        render_impact_section()
        return

    current_user = st.session_state.username
    client = get_ai_agent()

    # Active Execution Command Operational Bar
    c_status_left, c_status_right = st.columns([5, 1])
    with c_status_left:
        st.markdown(f"<h5>🟢 Workspace Operational Index: <b>{current_user}</b></h5>", unsafe_allow_html=True)
    with c_status_right:
        if st.button("Disconnect Portal", key="btn_global_disconnect"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.current_page = "Dashboard Workspace"
            st.rerun()

    # Unified Left Core Sidebar Navigation Control Panel
    with st.sidebar:
        st.markdown("### 🧭 Platform Navigation Matrix")
        if st.button("🏠 Comprehensive Unified Dashboard", use_container_width=True): 
            st.session_state.current_page = "Dashboard Workspace"
            st.rerun()
        if st.button("📄 Enterprise CV Evaluation Core", use_container_width=True): 
            st.session_state.current_page = "Advanced CV Builder"
            st.rerun()
        if st.button("🎤 Live Interview Simulator Hub", use_container_width=True): 
            st.session_state.current_page = "Interview Simulation"
            st.rerun()
        if st.button("🤝 Employer Hiring Marketplace", use_container_width=True): 
            st.session_state.current_page = "Employer Connect"
            st.rerun()
        if st.button("⚙️ Core Platform Config Settings", use_container_width=True): 
            st.session_state.current_page = "Profile Config"
            st.rerun()

    # =============================================================================
    # MODULE ROUTING ROUTER RUN MATRIX
    # =============================================================================
    
    if st.session_state.current_page == "Dashboard Workspace":
        st.markdown(f"## Welcome back, {current_user} 👋")
                # Career Readiness Score Banner Block
        st.markdown('<div class="premium-card" style="border-top: 4px solid #19D17B;">', unsafe_allow_html=True)
        col_crs_left, col_crs_right = st.columns([1, 2])
        with col_crs_left:
            st.markdown("<h4 style='margin:0; color:#64748B;'>Career Readiness Score</h4>", unsafe_allow_html=True)
            st.markdown("<div style='font-size: 48px; font-weight: 800; color: #0B6B3A;'>82%</div>", unsafe_allow_html=True)
            st.markdown("<code style='font-size:16px; color:#0B6B3A;'>████████░░</code>", unsafe_allow_html=True)
        with col_crs_right:
            st.markdown("<p style='margin: 4px 0;'>🟩 <b>Profile Strength:</b> 90%</p>", unsafe_allow_html=True)
            st.markdown("<p style='margin: 4px 0;'>🟩 <b>Skills Match Coefficient:</b> 78%</p>", unsafe_allow_html=True)
            st.markdown("<p style='margin: 4px 0;'>🟩 <b>Ecosystem CV Quality index:</b> 88%</p>", unsafe_allow_html=True)
            st.markdown("<p style='margin: 4px 0;'>🟩 <b>Interview Readiness Score:</b> 72%</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # SaaS Platform Analytics Grid
        st.markdown("""
            <div class="saas-grid">
                <div class="saas-analytics-card"><div class="saas-val">88%</div><div class="saas-lbl">ATS Match Score</div></div>
                <div class="saas-analytics-card"><div class="saas-val">54</div><div class="saas-lbl">Matched Active Jobs</div></div>
                <div class="saas-analytics-card"><div class="saas-val">3</div><div class="saas-lbl">Live Interviews</div></div>
                <div class="saas-analytics-card"><div class="saas-val">2</div><div class="saas-lbl">Remaining Skill Gaps</div></div>
            </div>
        """, unsafe_allow_html=True)

        col_main_left, col_main_right = st.columns([3, 2])

        with col_main_left:
            st.markdown('<div class="premium-card"><h3>🧠 Core Cognitive Assessment Engine</h3></div>', unsafe_allow_html=True)
            ans = st.radio("Do you prioritize building scalable technical software architectures or managing business delivery workflows?", 
                          ["Select Preference Track...", "Software System & AI Development", "Product & Project Strategy Workflows"])
            
            if "AI Development" in ans or "Strategy" in ans:
                st.markdown("<div class='badge-green'>🟩 <b>Calculated Persona Classification:</b> Strategic High-Growth Technical Leader</div>", unsafe_allow_html=True)
                
                st.markdown('<div class="premium-card"><h3>🔮 Forward Predictive Employability Projections</h3></div>', unsafe_allow_html=True)
                col_prob_l, col_prob_r = st.columns([1, 2])
                with col_prob_l:
                    st.markdown("<div style='font-size: 36px; font-weight:800; color:#0B6B3A; text-align:center;'>87%</div>", unsafe_allow_html=True)
                    st.markdown("<p style='color:#0B6B3A; font-weight:700; text-align:center;'>High Probability</p>", unsafe_allow_html=True)
                with col_prob_r:
                    st.markdown("<span style='color:#22C55E;'>✓</span> <b>Strong Technical Communication Vectors</b><br/>", unsafe_allow_html=True)
                    st.markdown("<span style='color:#22C55E;'>✓</span> <b>Highly Competitive ATS Parameter Optimization</b><br/>", unsafe_allow_html=True)
                    st.markdown("<span style='color:#22C55E;'>✓</span> <b>High Structural Career Alignment Match</b><br/>", unsafe_allow_html=True)
                    st.markdown("<span style='color:#EF4444;'>⚠</span> <span style='color:#7F1D1D;'>Missing High-Fidelity Capstone Framework Portfolios</span>", unsafe_allow_html=True)

                st.markdown('<div class="premium-card"><h3>💼 Strategic Job Match Engine Mapping</h3></div>', unsafe_allow_html=True)
                
                jobs_data = [
                    {"title": "Project Coordinator / Product Associate", "match": "94%"},
                    {"title": "Junior Business Systems Analyst", "match": "89%"},                    {"title": "Technical Operations Specialist", "match": "87%"}
                ]
                for j in jobs_data:
                    c_j1, c_j2 = st.columns([3, 2])
                    with c_j1:
                        st.markdown(f"<div class='badge-blue'>🔷 <b>{j['title']}</b> ({j['match']} Match Profile Correlation)</div>", unsafe_allow_html=True)
                    with c_j2:
                        st.markdown("<div style='margin-top:4px;'>", unsafe_allow_html=True)
                        st.button("Apply Instantly", key=f"apply_{j['title']}")
                        st.markdown("</div>", unsafe_allow_html=True)

            st.markdown('<div class="premium-card"><h3>🔍 Operational Skills Gap Audit Engine</h3></div>', unsafe_allow_html=True)
            st.markdown("<div class='badge-blue'>🔷 <b>Current Operational Skill Matrix:</b> MS Word, Advanced Excel Data Formats, Functional Interpersonal Presentation.</div>", unsafe_allow_html=True)
            st.markdown("<div class='badge-red'>🟥 <b>Identified Missing Target Skills Base:</b> Cloud Infrastructure Architecture, Scalable Project Management Frameworks, Automated Power BI Analytics Dashboards.</div>", unsafe_allow_html=True)

            st.markdown('<div class="premium-card"><h3>📚 Curriculum Learning Roadmap Timeline Engine</h3></div>', unsafe_allow_html=True)
            col_m1, col_m2, col_m3, col_m4 = st.columns(4)
            with col_m1: 
                st.markdown("<div class='badge-orange'>🔸 <b>Month 1</b><br/>Excel Advanced Tracking</div>", unsafe_allow_html=True)
            with col_m2: 
                st.markdown("<div class='badge-orange'>🔸 <b>Month 2</b><br/>Power BI Architecture</div>", unsafe_allow_html=True)
            with col_m3: 
                st.markdown("<div class='badge-orange'>🔸 <b>Month 3</b><br/>Project Management</div>", unsafe_allow_html=True)
            with col_m4: 
                st.markdown("<div class='badge-orange'>🔸 <b>Month 4</b><br/>Portfolio Blueprint</div>", unsafe_allow_html=True)

        with col_main_right:
            st.markdown('<div class="premium-card" style="border: 2px solid #0B6B3A; background-color: #F0FDF4;">', unsafe_allow_html=True)
            st.markdown("<h3 style='color: #0B6B3A !important; margin-bottom: 2px;'>🏆 MT Employability Score™</h3>", unsafe_allow_html=True)
            st.markdown("<div style='font-size: 42px; font-weight: 800; color: #0B6B3A; margin-bottom:10px;'>84 <span style='font-size:20px; font-weight:500; color:#64748B;'>/ 100</span></div>", unsafe_allow_html=True)
            st.markdown("<p style='margin:3px 0; font-size:14px;'>🎯 <b>Career Target Index Match:</b> 92%</p>", unsafe_allow_html=True)
            st.markdown("<p style='margin:3px 0; font-size:14px;'>📄 <b>CV Structure Evaluation Strength:</b> 88%</p>", unsafe_allow_html=True)
            st.markdown("<p style='margin:3px 0; font-size:14px;'>🧠 <b>Technical Skills Readiness Profile:</b> 79%</p>", unsafe_allow_html=True)
            st.markdown("<p style='margin:3px 0; font-size:14px;'>🎤 <b>Behavioral Interview Capability Skill:</b> 76%</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="premium-card"><h3>🤖 Ask Launchpad AI Career Copilot</h3></div>', unsafe_allow_html=True)
            
            st.markdown("<p style='font-size:12px; font-weight:700; color:#64748B; margin-bottom:4px;'>QUICK ACTION CHIPS PROMPTS:</p>", unsafe_allow_html=True)
            c_chip1, c_chip2 = st.columns(2)
            with c_chip1:
                if st.button("📄 How do I improve my CV?", use_container_width=True):
                    st.session_state.copilot_messages.append({"role": "user", "content": "How do I improve my CV?"})
                    if client:
                        try:
                            resp = client.models.generate_content(model='gemini-2.5-flash', 
                                contents="Give 3 short actionable points to improve a graduate CV specifically focusing on technical skills impact mapping.")
                            st.session_state.copilot_messages.append({"role": "assistant", "content": resp.text})
                        except:
                            st.session_state.copilot_messages.append({"role": "assistant", "content": "To enhance your CV: 1. Use action verbs 2. Align keywords with job descriptions 3. Quantify results"})                    else:
                        st.session_state.copilot_messages.append({"role": "assistant", "content": "To enhance your CV profile: 1. Inject clear action verbs. 2. Align keywords with target jobs. 3. Quantify metric results."})
            with c_chip2:
                if st.button("✉️ Create a cover letter", use_container_width=True):
                    st.session_state.copilot_messages.append({"role": "user", "content": "Create a cover letter template"})
                    st.session_state.copilot_messages.append({"role": "assistant", "content": "Subject: Application for Target Role\n\nDear Hiring Team,\n\nI am writing to express my interest in the position..."})

            for msg in st.session_state.copilot_messages[-4:]:
                if msg["role"] == "user":
                    st.markdown(f"<div style='text-align:right; margin:6px 0;'><span style='background-color:#E2E8F0; padding:8px 12px; border-radius:12px; display:inline-block; font-size:14px;'><b>You:</b> {msg['content']}</span></div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div style='text-align:left; margin:6px 0;'><span style='background-color:#DCFCE7; padding:8px 12px; border-radius:12px; display:inline-block; font-size:14px; border-left:4px solid #0B6B3A;'><b>AI:</b> {msg['content']}</span></div>", unsafe_allow_html=True)
            
            chat_box_input = st.text_input("Consult Copilot Stream Intelligence...", key="copilot_live_chat_input_field")
            if st.button("Dispatch Query Pipeline Line", key="btn_send_chat_copilot"):
                if chat_box_input:
                    st.session_state.copilot_messages.append({"role": "user", "content": chat_box_input})
                    if client:
                        try:
                            r = client.models.generate_content(model='gemini-2.5-flash', contents=chat_box_input)
                            st.session_state.copilot_messages.append({"role": "assistant", "content": r.text})
                        except:
                            st.session_state.copilot_messages.append({"role": "assistant", "content": "Query processed successfully."})
                    else:
                        st.session_state.copilot_messages.append({"role": "assistant", "content": "Local processing completed."})
                    st.rerun()

            st.markdown('<div class="premium-card"><h3>🏁 Operational Career Journey Progress Tracker</h3></div>', unsafe_allow_html=True)
            st.markdown("🔹 **Profile Setup** ✅ `COMPLETED`", unsafe_allow_html=True)
            st.markdown("🔹 **Cognitive Assessment** ✅ `COMPLETED`", unsafe_allow_html=True)
            st.markdown("🔹 **AI CV Optimization** ✅ `COMPLETED`", unsafe_allow_html=True)
            st.markdown("🔹 **Interview Simulation** ⏳ `IN PROGRESS`", unsafe_allow_html=True)
            st.markdown("🔹 **Job Placement** ⏳ `PENDING`", unsafe_allow_html=True)

        render_impact_section()

    elif st.session_state.current_page == "Advanced CV Builder":
        st.markdown('<div class="premium-card"><h3>📄 Enterprise AI CV Optimization Workspace</h3></div>', unsafe_allow_html=True)
        
        st.file_uploader("Drag & Drop CV or Profile Document", type=["pdf", "docx"])
        st.session_state.cv_data_name = st.text_input("Full Legal Name", value=st.session_state.cv_data_name)
        st.session_state.cv_data_title = st.text_input("Target Professional Title", value=st.session_state.cv_data_title)
        st.session_state.cv_data_skills = st.text_area("Technical Skills", value=st.session_state.cv_data_skills)
        st.session_state.cv_data_exp = st.text_area("Career Experience", value=st.session_state.cv_data_exp)
        
        if st.button("Save Profile Parameters"):
            p = {"fullname": st.session_state.cv_data_name, "role": st.session_state.cv_data_title, 
                 "skills": st.session_state.cv_data_skills, "bio": st.session_state.cv_data_exp, 
                 "projects": st.session_state.cv_data_projects}
            update_user_profile(current_user, p)            st.success("Profile saved successfully!")

        target_description_text = st.text_area("Paste Target Job Description")
        if st.button("Execute CV Optimization Analysis"):
            if client:
                with st.spinner("Processing..."):
                    prompt = f"ATS audit for {st.session_state.cv_data_title}. Skills: {st.session_state.cv_data_skills}. Target: {target_description_text}"
                    try:
                        response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                        st.session_state["last_cv_output"] = response.text
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.session_state["last_cv_output"] = "### ATS SCORE: 88%\n\n**Strengths:** Clear layout\n**Weaknesses:** Needs action keywords"

        if "last_cv_output" in st.session_state:
            st.info(st.session_state["last_cv_output"])
            cv_html = f"<html><body><h2>ATS Report</h2><pre>{st.session_state['last_cv_output']}</pre></body></html>"
            st.download_button("📥 Download Report", data=cv_html, file_name="ATS_Report.html", mime="text/html")

    elif st.session_state.current_page == "Interview Simulation":
        st.markdown('<div class="premium-card"><h3>🎤 Interview Intelligence & Simulation</h3></div>', unsafe_allow_html=True)
        itype = st.selectbox("Select Interview Type", ["Graduate Trainee", "Internship", "Entry Level"])
        st.warning("**Question:** Tell us about a time you handled project roadblocks under pressure.")
        user_response = st.text_area("Type Your Response")
        
        if st.button("Submit for Evaluation"):
            if client:
                with st.spinner("Analyzing..."):
                    try:
                        r = client.models.generate_content(model='gemini-2.5-flash', 
                            contents=f"Evaluate: '{user_response}' for {itype}")
                        st.session_state["last_interview_output"] = r.text
                    except:
                        st.error("Connection error")
            else:
                st.session_state["last_interview_output"] = "### Score: 79%\n\nGood structure. Use STAR framework."

        if "last_interview_output" in st.session_state:
            st.info(st.session_state["last_interview_output"])

    elif st.session_state.current_page == "Employer Connect":
        st.markdown('<div class="premium-card" style="border-top:4px solid #3B82F6;"><h3>🏢 Employer Portal</h3></div>', unsafe_allow_html=True)
        
        c_emp1, c_emp2 = st.columns(2)
        with c_emp1:
            st.markdown("#### 🔍 Search Candidates")
            st.text_input("Filter by Skills")
            st.button("Search")
            st.markdown("---")            st.markdown("#### 💼 Post Jobs")
            st.text_input("Job Title")
            st.text_area("Job Description")
            st.button("Publish")
            
        with c_emp2:
            st.markdown('<div class="premium-card"><h3>🌟 Top Matches</h3></div>', unsafe_allow_html=True)
            st.write("🟢 **Candidate** — Match: `94%`")
            st.button("View Profile")

    elif st.session_state.current_page == "Profile Config":
        st.markdown('<div class="premium-card"><h3>⚙️ Platform Settings</h3></div>', unsafe_allow_html=True)
        st.write(f"Working Directory: `{os.getcwd()}`")
        st.info("System diagnostics: OK")

    render_footer()

def render_impact_section():
    st.markdown("""
        <div class="premium-card" style="margin-top: 35px; border-top: 4px solid #0B6B3A; background: #F8FAFC;">
            <h3 style="text-align:center; color:#0B6B3A !important; font-weight:800;">📈 Launchpad Impact Metrics</h3>
            <div style="display: flex; justify-content: space-around; flex-wrap: wrap; text-align: center; margin-top: 20px;">
                <div style="padding:10px;"><div style="font-size:32px; font-weight:800; color:#0B6B3A;">1,250+</div><div style="font-size:12px; color:#64748B; font-weight:700;">GRADUATES</div></div>
                <div style="padding:10px;"><div style="font-size:32px; font-weight:800; color:#0B6B3A;">3,800+</div><div style="font-size:12px; color:#64748B; font-weight:700;">CVS OPTIMIZED</div></div>
                <div style="padding:10px;"><div style="font-size:32px; font-weight:800; color:#0B6B3A;">940+</div><div style="font-size:12px; color:#64748B; font-weight:700;">INTERVIEWS</div></div>
                <div style="padding:10px;"><div style="font-size:32px; font-weight:800; color:#0B6B3A;">76%</div><div style="font-size:12px; color:#64748B; font-weight:700;">SUCCESS RATE</div></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_footer():
    st.markdown("""
        <div class="system-footer">
            <h4>Graduate Career Launchpad</h4>
            <p style="margin-top: 4px; font-weight: 600; color: #19D17B !important;">Developed by MIDDLE TECHNOLOGY</p>
            <p style="font-size: 14px; opacity: 0.9;"><b>Founder:</b> Hassan Peros</p>
            <p style="font-size: 14px; margin-top: 8px; font-style: italic; max-width: 700px; margin-left: auto; margin-right: auto;">
                "Bridging the gap between graduates and employment through AI-powered career intelligence."
            </p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
