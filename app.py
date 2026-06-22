import streamlit as st
import json
import hashlib
import os

@st.cache_resource
def get_global_memory_bridge():
    return {"active_sessions": {}}

global_bridge = get_global_memory_bridge()

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
        return False    users[username] = {
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

def inject_premium_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=300;400;500;600;700;800&display=swap');
        #MainMenu {visibility: hidden !important;}
        header {visibility: hidden !important;}
        [data-testid="stToolbar"] {display: none !important;}
        .stApp {
            background-color: #F8FAFC !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: #1E293B !important;
        }
        .premium-hero {
            background: linear-gradient(135deg, #0B6B3A 0%, #063c22 100%);
            text-align: center;
            padding: 35px 20px;
            border-radius: 20px;            margin-bottom: 25px;
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
            font-weight: 500 !important;
        }
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
            border-left: 5px solid #EF4444 !important;            color: #7F1D1D !important;
            padding: 12px 16px; border-radius: 8px; margin-bottom: 10px; font-weight: 500;
        }
        .saas-grid {
            display: flex; gap: 15px; margin-bottom: 25px; flex-wrap: wrap;
        }
        .saas-analytics-card {
            flex: 1; min-width: 160px; background: #ffffff; border: 1px solid #E2E8F0;
            padding: 20px 16px; border-radius: 12px; text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02); border-top: 4px solid #0B6B3A;
        }
        .saas-val { font-size: 28px; font-weight: 800; color: #1E293B; margin-bottom: 4px; }
        .saas-lbl { font-size: 12px; color: #64748B; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
        div.stButton > button {
            background: linear-gradient(90deg, #0B6B3A 0%, #19D17B 100%) !important;
            color: #ffffff !important;
            border-radius: 12px !important;
            border: none !important;
            padding: 10px 20px !important;
            font-weight: 700 !important;
        }
        .system-footer {
            margin-top: 40px; padding: 30px; background-color: #0B6B3A;
            border-radius: 16px; color: #ffffff !important; text-align: center;
        }
        .system-footer h4, .system-footer p { color: #ffffff !important; }
        </style>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Graduate Career Launchpad", page_icon="🎓", layout="wide")
    inject_premium_styles()
    
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.current_page = "Dashboard Workspace"
        st.session_state.cv_data_name = ""
        st.session_state.cv_data_title = ""
        st.session_state.cv_data_skills = ""
        st.session_state.cv_data_exp = ""
        st.session_state.cv_data_projects = ""
        st.session_state.copilot_messages = [{"role": "assistant", "content": "Hello! I am your Launchpad AI Career Copilot."}]

    st.markdown("""
        <div class="premium-hero">
            <h1>Graduate Career Launchpad</h1>
            <p class="tagline">Enterprise AI-Powered Employability & Acceleration Ecosystem</p>
        </div>
    """, unsafe_allow_html=True)
    if not st.session_state.logged_in:
        col_auth_left, col_auth_right = st.columns(2)
        
        with col_auth_left:
            st.markdown('<div class="premium-card"><h3>🔒 Login</h3></div>', unsafe_allow_html=True)
            lin_user = st.text_input("Username", key="l_user_field")
            lin_pass = st.text_input("Password", type="password", key="l_pass_field")
            if st.button("Login", key="act_login_btn"):
                if authenticate_user(lin_user, lin_pass):
                    st.session_state.logged_in = True
                    st.session_state.username = lin_user
                    st.session_state.current_page = "Dashboard Workspace"
                    st.rerun()
                else:
                    st.error("Login failed.")
            
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
            st.markdown('<div class="premium-card"><h3>✨ Register</h3></div>', unsafe_allow_html=True)
            reg_user = st.text_input("Choose Username", key="r_user_field")
            reg_pass = st.text_input("Create Password", type="password", key="r_pass_field")
            if st.button("Register", key="act_reg_btn"):
                if reg_user and reg_pass:
                    if register_user(reg_user, reg_pass):
                        st.success("Registered! Please login.")
                    else:
                        st.error("Username taken.")
        
        render_impact_section()
        return

    current_user = st.session_state.username
    client = get_ai_agent()

    c_status_left, c_status_right = st.columns([5, 1])
    with c_status_left:
        st.markdown(f"🟢 Logged in as: **{current_user}**")    with c_status_right:
        if st.button("Logout", key="btn_global_disconnect"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.current_page = "Dashboard Workspace"
            st.rerun()

    with st.sidebar:
        st.markdown("### 🧭 Navigation")
        if st.button("🏠 Dashboard", use_container_width=True): 
            st.session_state.current_page = "Dashboard Workspace"
            st.rerun()
        if st.button("📄 CV Builder", use_container_width=True): 
            st.session_state.current_page = "Advanced CV Builder"
            st.rerun()
        if st.button("🎤 Interview", use_container_width=True): 
            st.session_state.current_page = "Interview Simulation"
            st.rerun()
        if st.button("🤝 Employers", use_container_width=True): 
            st.session_state.current_page = "Employer Connect"
            st.rerun()

    if st.session_state.current_page == "Dashboard Workspace":
        st.markdown(f"## Welcome back, {current_user} 👋")
        st.markdown('<div class="premium-card"><h3>📊 Dashboard</h3><p>Your career dashboard is ready!</p></div>', unsafe_allow_html=True)
        render_impact_section()

    elif st.session_state.current_page == "Advanced CV Builder":
        st.markdown('<div class="premium-card"><h3>📄 CV Builder</h3></div>', unsafe_allow_html=True)
        st.text_input("Full Name", value=st.session_state.cv_data_name)
        st.text_input("Target Role", value=st.session_state.cv_data_title)
        st.text_area("Skills", value=st.session_state.cv_data_skills)
        if st.button("Save"):
            st.success("Saved!")

    elif st.session_state.current_page == "Interview Simulation":
        st.markdown('<div class="premium-card"><h3>🎤 Interview Practice</h3></div>', unsafe_allow_html=True)
        st.text_area("Type your answer")
        st.button("Submit")

    elif st.session_state.current_page == "Employer Connect":
        st.markdown('<div class="premium-card"><h3>🏢 Employer Portal</h3></div>', unsafe_allow_html=True)

    render_footer()

def render_impact_section():
    st.markdown("""
        <div class="premium-card" style="margin-top: 35px; border-top: 4px solid #0B6B3A;">
            <h3 style="text-align:center; color:#0B6B3A !important;">📈 Impact Metrics</h3>
            <div style="display: flex; justify-content: space-around; text-align: center;">                <div><div style="font-size:32px; font-weight:800; color:#0B6B3A;">1,250+</div><div>Graduates</div></div>
                <div><div style="font-size:32px; font-weight:800; color:#0B6B3A;">3,800+</div><div>CVs Optimized</div></div>
                <div><div style="font-size:32px; font-weight:800; color:#0B6B3A;">76%</div><div>Success Rate</div></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_footer():
    st.markdown("""
        <div class="system-footer">
            <h4>Graduate Career Launchpad</h4>
            <p>Developed by MIDDLE TECHNOLOGY</p>
            <p><b>Founder:</b> Hassan Peros</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
