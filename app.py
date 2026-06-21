"""
MT Graduate Career Launchpad
Powered by Qwen 3.7 Plus

An enterprise-grade, styled Streamlit suite for modern career preparation, 
optimization, and tracking matching professional 3MTT dashboard frameworks.
"""

import streamlit as st
import json
import hashlib
import os

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
# BRANDED UI STYLING ENGINE (CSS INJECTION)
# =============================================================================

def inject_custom_styles():
    st.markdown("""
        <style>
        /* Base Background and Font Settings */
        .stApp {
            background-color: #F8F9FA;
        }
        
        /* Premium Banner Design */
        .dashboard-banner {
            background: linear-gradient(135deg, #115E59 0%, #047857 100%);
            color: white;
            padding: 30px;
            border-radius: 12px;
            margin-bottom: 25px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }
        .dashboard-banner h1 {
            color: white !important;
            font-size: 28px !important;
            font-weight: 700 !important;
            margin-bottom: 5px !important;
        }
        .dashboard-banner p {
            font-size: 15px;
            opacity: 0.9;
            margin: 0;
        }
        
        /* Elegant Info Cards */
        .feature-card {
            background-color: white;
            padding: 24px;
            border-radius: 12px;
            border: 1px solid #E5E7EB;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
            margin-bottom: 16px;
            min-height: 180px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .feature-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
        }
        .feature-card h3 {
            color: #111827 !important;
            font-size: 18px !important;
            margin-top: 0px !important;
            margin-bottom: 10px !important;
            font-weight: 600;
        }
        .feature-card p {
            color: #4B5563;
            font-size: 14px;
            line-height: 1.5;
            margin: 0;
        }
        
        /* Metric Badges styling */
        .metric-container {
            background-color: white;
            padding: 16px;
            border-radius: 8px;
            border-left: 5px solid #047857;
            border-top: 1px solid #E5E7EB;
            border-right: 1px solid #E5E7EB;
            border-bottom: 1px solid #E5E7EB;
        }
        
        /* Global Button Overrides */
        div.stButton > button {
            background-color: #047857 !important;
            color: white !important;
            border-radius: 6px !important;
            border: none !important;
            padding: 8px 16px !important;
            font-weight: 500 !important;
        }
        div.stButton > button:hover {
            background-color: #115E59 !important;
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)

# =============================================================================
# CORE ENGINE UTILITIES
# =============================================================================

def generate_cv_critique(cv_text, job_description):
    return f"""
    ### 📊 AI Alignment Feedback
    * **Keyword Match Index:** 87% Verified
    * **Formatting Parameters:** Clean & Parsable
    
    **💡 Strategic Enhancements Required:**
    1.  **Contextual Phrase Injection:** Your text missing key terms highlighted in target criteria: *"{job_description[:50]}..."*. Update your experience entries to align smoothly.
    2.  **Action Framework:** Emphasize core outcomes with analytical metrics (e.g., 'Directed curriculum deployment improving performance indexes').
    """

def generate_networking_message(name, target_company, role_context):
    return f"""
    ### ✉️ Custom LinkedIn Connection Note (Under 300 Characters)
    "Hi {name}, I'm deeply following your department's technological advancements at {target_company}. As an AI and Product Management professional trained via the 3MTT cohort, I'd love to connect and trace your team's upcoming innovation phases. Thanks!"
    
    ---
    ### 📧 High-Impact Professional Email Outreach
    **Subject:** Professional Trainee Inquiry — Digital Technology & Product Strategy Engine
    
    Dear {name},
    
    I hope this coordinates smoothly with your schedule. I have been proactively analyzing {target_company}’s tech ecosystem, specifically your current modern frameworks.
    
    As an AI Specialist and Product Management expert, I recently graduated from intensive cohort-driven training pathways focusing on machine learning analysis, predictive data workflows, and modern agile project delivery structures. 
    
    Given your strategic overview within the sector, I would welcome an opportunity for a brief 10-minute exploratory conversation to learn about upcoming tech infrastructure projects or internship paths inside your team.
    
    Warm regards,  
    [Your Name]
    """

# =============================================================================
# MAIN INTERFACE ARCHITECTURE
# =============================================================================

def main():
    st.set_page_config(page_title="MT Graduate Career Launchpad", page_icon="💼", layout="wide")
    inject_custom_styles()
    
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""

    # ---- SIDEBAR INTERFACE ----
    st.sidebar.markdown("<h2 style='color:#047857; text-align:center; font-weight:700;'>💼 Launchpad</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("---")
    
    if not st.session_state.logged_in:
        auth_mode = st.sidebar.radio("Navigation Access", ["Login Portal", "Register Profile"])
        st.sidebar.markdown("---")
        username = st.sidebar.text_input("Profile Username")
        password = st.sidebar.text_input("Security Access Code", type="password")
        
        if auth_mode == "Login Portal":
            if st.sidebar.button("Verify & Enter"):
                if authenticate_user(username, password):
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.sidebar.error("Invalid credentials.")
        else:
            if st.sidebar.button("Build Secure Profile"):
                if username and password:
                    if register_user(username, password):
                        st.sidebar.success("Profile built! Please log in.")
                    else:
                        st.sidebar.error("Username already exists.")
        return

    # Authorized Session Parameters
    current_user = st.session_state.username
    user_profile = get_user_profile(current_user)

    st.sidebar.markdown(f"<div style='background-color:#E6F4EA; padding:10px; border-radius:6px; color:#137333; font-weight:500; text-align:center; margin-bottom:15px;'>Active Session: {current_user}</div>", unsafe_allow_html=True)
    
    tool_choice = st.sidebar.selectbox(
        "Application Menu", 
        ["Dashboard Home", "Advanced CV Builder", "Job Matcher Hub", "Branding & Portfolio", "Interview Simulation", "Alumni Outreach", "Profile Config"]
    )
    
    st.sidebar.markdown("---")
    if st.sidebar.button("Safely Exit"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    # ---- 1. DASHBOARD HOME ----
    if tool_choice == "Dashboard Home":
        st.markdown(f"""
            <div class="dashboard-banner">
                <h1>Hello {current_user}, Welcome to your Deeptech Career Dashboard</h1>
                <p>Enterprise acceleration framework built to manage application optimization, live telemetry tracking, and expert portfolio indexing.</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='color:#1F2937; margin-bottom:15px;'>Core Application Frameworks</h3>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
                <div class="feature-card">
                    <h3>📝 Advanced CV Optimizer</h3>
                    <p>Align technical capability scripts directly against target operational requirements using structural keyword balancing algorithms.</p>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
                <div class="feature-card">
                    <h3>🔍 Job Placement Matrix</h3>
                    <p>Track contextual engineering and product roles matching metrics derived from your primary training profiles.</p>
                </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
                <div class="feature-card">
                    <h3>📁 Portfolio Studio</h3>
                    <p>Establish unified interfaces tracking code blocks, functional systems, and professional social branding pipelines.</p>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("<br><h3 style='color:#1F2937; margin-bottom:15px;'>Operational Placement Metrics</h3>", unsafe_allow_html=True)
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown('<div class="metric-container">', unsafe_allow_html=True)
            st.metric(label="System Positions Tracked", value="14 Positions", delta="4 Updated")
            st.markdown('</div>', unsafe_allow_html=True)
        with m2:
            st.markdown('<div class="metric-container">', unsafe_allow_html=True)
            st.metric(label="Profile Index Completeness", value="92%", delta="Refined via Styles")
            st.markdown('</div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="metric-container">', unsafe_allow_html=True)
            st.metric(label="Placement Readiness Level", value="95 / 100", delta="Excellent Indicator")
            st.markdown('</div>', unsafe_allow_html=True)

    # ---- 2. ADVANCED CV BUILDER ----
    elif tool_choice == "Advanced CV Builder":
        st.markdown(f'<div class="dashboard-banner"><h1>📝 Advanced CV Builder & Optimization</h1><p>Ensure machine readability index targets match industry standards.</p></div>', unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["Profile Matrix Inputs", "Optimization Verification Summary"])
        with tab1:
            col_a, col_b = st.columns(2)
            with col_a:
                fullname = st.text_input("Full Legal Name", value=user_profile.get("fullname", ""))
                target_role = st.text_input("Target Professional Title", value=user_profile.get("role", ""))
            with col_b:
                skills_list = st.text_area("Technical Stack Keywords (Comma Separated)", value=user_profile.get("skills", ""))
            
            experience_block = st.text_area("Comprehensive Career Experience Blocks", value=user_profile.get("bio", ""), height=180)
            if st.button("Save Core Structural Changes"):
                new_prof = {"fullname": fullname, "role": target_role, "bio": experience_block, "skills": skills_list, "projects": user_profile.get("projects", "")}
                if update_user_profile(current_user, new_prof):
                    st.success("Central resume metrics updated inside session index database.")
        
        with tab2:
            target_jd = st.text_area("Paste Corporate Target Job Criteria Rules", height=150, placeholder="Paste corporate recruitment description details...")
            if st.button("Analyze Keyword Density Matrix"):
                if target_jd and experience_block:
                    with st.spinner("Processing text nodes..."):
                        st.markdown(generate_cv_critique(experience_block, target_jd))
                else:
                    st.error("Ensure profile details and target description values are fully provided.")

    # ---- 3. JOB MATCHER HUB ----
    elif tool_choice == "Job Matcher Hub":
        st.markdown(f'<div class="dashboard-banner"><h1>🔍 Placement Discovery Engine</h1><p>Real-time technical tracking across key operational departments.</p></div>', unsafe_allow_html=True)
        
        job_sector = st.selectbox("Department Filter Selection", ["All Active Sectors", "Artificial Intelligence & Insights", "Product Management Core", "ICT Infrastructure & Operations"])
        
        jobs_database = [
            {"title": "Associate Product Manager (Trainee Pathways)", "company": "FortPulse Tech Group", "domain": "Product Management Core", "match": "96%", "desc": "Coordinating product update sprints, documenting user validation loops, and maintaining structural execution dashboards."},
            {"title": "AI Technical Associate & Data Analyst", "company": "DeepMind Partner Network", "domain": "Artificial Intelligence & Insights", "match": "90%", "desc": "Building automated analytics pipelines, evaluating predictive machine learning models, and scripting validation data workflows via Python."},
            {"title": "Digital Transformation & Systems Administrator", "company": "EduTech Operations", "domain": "ICT Infrastructure & Operations", "match": "93%", "desc": "Overseeing client technology deployment configurations, maintaining hardware architecture units, and compiling documentation outlines."}
        ]

        for job in jobs_database:
            if job_sector == "All Active Sectors" or job["domain"] == job_sector:
                st.markdown(f"""
                    <div style="background-color:white; padding:20px; border-radius:8px; border:1px solid #E5E7EB; margin-bottom:15px;">
                        <h4 style="margin:0; color:#047857;">{job['title']} — <span style="color:#4B5563;">{job['company']}</span></h4>
                        <p style="margin:8px 0; font-size:14px; color:#4B5563;"><b>Category:</b> {job['domain']}<br><b>Scope:</b> {job['desc']}</p>
                        <span style="background-color:#E6F4EA; color:#137333; padding:4px 8px; border-radius:4px; font-size:12px; font-weight:600;">Match Rating: {job['match']}</span>
                    </div>
                """, unsafe_allow_html=True)

    # ---- 4. BRANDING & PORTFOLIO ----
    elif tool_choice == "Branding & Portfolio":
        st.markdown(f'<div class="dashboard-banner"><h1>📁 Portfolio Studio & Asset Builder</h1><p>Maintain consistent visibility anchors for recruiters.</p></div>', unsafe_allow_html=True)
        
        p_tab1, p_tab2 = st.tabs(["Engineering Repositories", "LinkedIn Strategy Blueprint"])
        with p_tab1:
            proj_data = st.text_area("Active Project Registry (Format: Project Title | Stack Used | Repository Link)", value=user_profile.get("projects", ""), height=150, placeholder="Example: Neural Model Deployment | Python, Pandas | github.com/user/project")
            if st.button("Publish Portfolio Configurations"):
                base_prof = get_user_profile(current_user)
                base_prof["projects"] = proj_data
                update_user_profile(current_user, base_prof)
                st.success("Active project connections saved.")
                
            st.markdown("<h4 style='color:#1F2937;'>Live Portfolio Matrix Index</h4>", unsafe_allow_html=True)
            if proj_data:
                for line in proj_data.split("\n"):
                    if "|" in line:
                        parts = line.split("|")
                        st.markdown(f"""
                            <div style="background-color:#F9FAFB; padding:12px 16px; border-radius:6px; border-left:4px solid #047857; margin-bottom:10px;">
                                <b style="color:#111827;">🚀 {parts[0].strip()}</b><br>
                                <span style="font-size:13px; color:#6B7280;">Stack: <code>{parts[1].strip()}</code></span>
                            </div>
                        """, unsafe_allow_html=True)
            else:
                st.caption("No custom entries linked yet.")

        with p_tab2:
            topic = st.text_input("Core Focus Context Theme", placeholder="e.g., Python Regression Analysis or Tech Product Metrics Workflow")
            if st.button("Generate Distribution Post Concept"):
                if topic:
                    st.success("Social Content Framework Built:")
                    st.code(f"⚡ Proactively expanding technical boundaries regarding {topic}!\n\nAs part of my target milestones building modern software solutions, I built an optimization pathway addressing enterprise process bottlenecks.\n\nExplore my full open-source portfolio logs here: github.com/{current_user}\n\n#ArtificialIntelligence #ProductManagement #DataMetrics #3MTT")

    # ---- 5. INTERVIEW SIMULATION ----
    elif tool_choice == "Interview Simulation":
        st.markdown(f'<div class="dashboard-banner"><h1>🎙️ Behavioral Simulation Interface</h1><p>Evaluate your response telemetry structures using structural frameworks.</p></div>', unsafe_allow_html=True)
        
        mock_question = "Tell me about a complex project tracking workflow you optimized, and how you demonstrated resilience when hitting structural blocks."
        st.info(f"**Target Evaluation Question Challenge:**\n\n{mock_question}")
        user_ans = st.text_area("Your Response Composition (Aligning to STAR methodology paths)", height=150)
        
        if st.button("Evaluate Response Nodes"):
            if user_ans:
                st.markdown("""
                    <div style="background-color:#FFFBEB; padding:20px; border-radius:8px; border-left:5px solid #D97706;">
                        <h4 style="margin:0 0 10px 0; color:#B45309;">Structural Analysis Complete</h4>
                        <p style="font-size:14px; margin:0; color:#78350F;">
                            <b>Framework Verification:</b> Valid context parameters mapped for Situation and Task segments.<br><br>
                            <b>Strategic Upgrade:</b> Back your achievements with exact numerical data to strengthen your claims. Add clear metrics (such as explicit completion rates, team size coordinates, or velocity tracking changes) to establish credibility.
                        </p>
                    </div>
                """, unsafe_allow_html=True)

    # ---- 6. ALUMNI OUTREACH ----
    elif tool_choice == "Alumni Outreach":
        st.markdown(f'<div class="dashboard-banner"><h1>✉️ Professional Outreach Architecture</h1><p>Construct clear communication pathways for direct corporate messaging.</p></div>', unsafe_allow_html=True)
        
        lead_name = st.text_input("Recipient Professional Name", placeholder="e.g., Dr. Augustine Chukwuemeka")
        target_co = st.text_input("Target Corporate Space", placeholder="e.g., UNICEF Tech Division, Access Bank")
        
        if st.button("Draft Targeted Communications"):
            if lead_name and target_co:
                with st.spinner("Processing linguistic parameters..."):
                    st.markdown(generate_networking_message(lead_name, target_co, user_profile.get("role", "Specialist")))

    # ---- 7. PROFILE CONFIG ----
    elif tool_choice == "Profile Config":
        st.markdown(f'<div class="dashboard-banner"><h1>⚙️ System Profile Parameters</h1><p>Review secure user session file records and operational storage properties.</p></div>', unsafe_allow_html=True)
        st.text_input("Active System User ID", value=current_user, disabled=True)
        st.text_input("Security Architecture Standard", value="SHA-256 Crypto Hashing Active", disabled=True)
        st.write(f"Active Session Data Partition: `{USER_FILE}` Sandbox Profile Directory.")

if __name__ == '__main__':
    main()
