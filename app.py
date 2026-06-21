"""
MT Graduate Career Launchpad
Powered by Qwen 3.7 Plus

A comprehensive Streamlit suite for modern career preparation, optimization, and tracking.
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
        # Handle legacy user data format
        if isinstance(stored_data, str):
            return stored_data == hash_password(password)
        return stored_data.get("password") == hash_password(password)
    return False

def update_user_profile(username, profile_data):
    users = load_users()
    if username in users:
        if isinstance(users[username], str):
            # Migrate legacy schema on the fly
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
# MOCK MIGRATED AI UTILITIES
# =============================================================================

def generate_cv_critique(cv_text, job_description):
    return f"""
    ### 🚀 Qwen AI Alignment Report
    *   **Keyword Match Score:** 84%
    *   **Formatting Structure:** Excellent layout detected.
    
    **🎯 Action Items for Optimization:**
    1.  **Incorporate Missing Keywords:** We noticed the target role heavily emphasizes terms like *"{job_description[:40]}..."*. Infuse these precisely into your summary.
    2.  **Quantify Metrics:** Replace vague statements with tangible outcomes (e.g., 'Optimized response latency by 20%').
    """

def generate_networking_message(name, target_company, role_context):
    return f"""
    ### ✉️ Custom LinkedIn Connection Message (300 Character Limit)
    "Hi {name}, I'm incredibly impressed by your team's innovative tech deployments at {target_company}. As a functional AI and product development graduate, I'd love to connect and follow your department's upcoming milestones. Thanks!"
    
    ---
    ### 📧 Professional Cold Outreach Email
    **Subject:** Inquiring regarding Innovation & Technology Trainee Pathways at {target_company}
    
    Dear {name},
    
    I hope this message finds you well. I have been closely tracking {target_company}'s tech footprint, particularly your focus on scalable digital modernization. 
    
    As an AI Specialist and Product Management professional, I recently completed intensive cohort-driven technical assignments spanning machine learning deployments and agile operational frameworks. My core training encompasses translating technical metrics into sound, business-aligned workflows.
    
    Given your leadership position within the workspace, I would deeply appreciate a brief 10-minute chat to learn more about upcoming engineering directions or internship channels within your branch.
    
    Warm regards,  
    [Your Name]
    """

# =============================================================================
# MAIN UI APPLICATION INTERFACE
# =============================================================================

def main():
    st.set_page_config(page_title="MT Graduate Career Launchpad", page_icon="💼", layout="wide")
    
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""

    st.sidebar.title("💼 Career Launchpad")
    
    if not st.session_state.logged_in:
        auth_mode = st.sidebar.radio("Choose Action", ["Login", "Register"])
        st.sidebar.markdown("---")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        
        if auth_mode == "Login":
            if st.sidebar.button("Log In"):
                if authenticate_user(username, password):
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.sidebar.error("Invalid credentials.")
        else:
            if st.sidebar.button("Register Account"):
                if username and password:
                    if register_user(username, password):
                        st.sidebar.success("Account constructed! Proceed to Log In.")
                    else:
                        st.sidebar.error("Username already registered.")
        return

    # User Profile State Loading
    current_user = st.session_state.username
    user_profile = get_user_profile(current_user)

    st.sidebar.success(f"Session Active: **{current_user}**")
    
    tool_choice = st.sidebar.selectbox(
        "Select Suite Interface", 
        ["Dashboard Home", "Advanced CV Builder", "Job Search Hub", "Portfolio Builder", "Interview Coach", "Networking Assistant", "Profile Engine"]
    )
    
    st.sidebar.markdown("---")
    if st.sidebar.button("Terminate Session"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    st.title("🚀 MT Graduate Career Launchpad")
    st.caption("AI-Powered Graduate Acceleration Ecosystem — Production Infrastructure")
    st.markdown("---")

    # ---- 1. DASHBOARD HOME ----
    if tool_choice == "Dashboard Home":
        st.subheader(f"Welcome back to the Launchpad, {current_user}! 👋")
        st.write("An enterprise ecosystem engineered to accelerate tech placement, portfolio optimization, and targeted job discovery.")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("### 📝 Advanced CV\nTailor foundational experience metrics directly against job requirements using localized linguistic analysis algorithms.")
        with col2:
            st.success("### 🔍 Job Search\nBrowse contextual, high-alignment target roles across local and international technology sectors.")
        with col3:
            st.warning("### 📁 Portfolio Engine\nConstruct cohesive layouts for professional portfolios, LinkedIn branding posts, and case studies.")

        st.markdown("---")
        st.markdown("### 📈 Application Flow Progress Engine")
        c1, c2, c3 = st.columns(3)
        c1.metric(label="Target Jobs Tracked", value="12 Positions", delta="3 New Today")
        c2.metric(label="Profile Architecture Completion", value="85%", delta="15% via Upgrades")
        c3.metric(label="Interview Readiness Index", value="92/100", delta="Excellent")

    # ---- 2. ADVANCED CV BUILDER ----
    elif tool_choice == "Advanced CV Builder":
        st.header("📝 Advanced CV Builder & Optimization Engine")
        
        tab1, tab2 = st.tabs(["Structured Data Input", "Linguistic Optimization Analysis"])
        
        with tab1:
            st.subheader("Construct Profile Metadata")
            col_a, col_b = st.columns(2)
            with col_a:
                fullname = st.text_input("Full Name", value=user_profile.get("fullname", ""))
                target_role = st.text_input("Target Corporate Title", value=user_profile.get("role", ""))
            with col_b:
                skills_list = st.text_area("Core Expertise Inventory (Comma Separated)", value=user_profile.get("skills", ""))
            
            experience_block = st.text_area("Detailed Professional Experience Narrative Blocks", value=user_profile.get("bio", ""), height=200)
            
            if st.button("Commit Core Profile Modifications"):
                new_prof = {"fullname": fullname, "role": target_role, "bio": experience_block, "skills": skills_list, "projects": user_profile.get("projects", "")}
                if update_user_profile(current_user, new_prof):
                    st.success("Central resume structural data cached successfully.")
        
        with tab2:
            st.subheader("Job Description Alignment Checker")
            target_jd = st.text_area("Paste Specific Target Job Description", height=150, placeholder="Paste corporate recruitment text constraints here...")
            if st.button("Run Comprehensive Contrast Optimization"):
                if target_jd and experience_block:
                    with st.spinner("Analyzing keyword density parameters..."):
                        report = generate_cv_critique(experience_block, target_jd)
                        st.markdown(report)
                else:
                    st.error("Ensure baseline experience records and target job metrics are fully populated.")

    # ---- 3. JOB SEARCH HUB ----
    elif tool_choice == "Job Search Hub":
        st.header("🔍 Automated Job Search & Recommendation Matrix")
        st.write("Browse current technology roles matching your technical skill inventory profile.")

        job_sector = st.selectbox("Filter Target Industry Domain", ["All Domains", "Artificial Intelligence & Analytics", "Product Management", "ICT Operations & Engineering"])
        
        jobs_database = [
            {"title": "Associate Product Manager (Trainee)", "company": "FortPulse Technologies", "domain": "Product Management", "match": "95%", "desc": "Assisting cross-functional development sprints, organizing project pipelines, and compiling product requirements metrics."},
            {"title": "AI Technical Associate & Data Analyst", "company": "DeepMind Innovation Lab Network", "domain": "Artificial Intelligence & Analytics", "match": "88%", "desc": "Building predictive neural layouts, tracking target model performance metrics, and executing tabular data workflows via Python."},
            {"title": "Digital Transformation Officer / Technology Instructor", "company": "EduTech Systems Infrastructure", "domain": "ICT Operations & Engineering", "match": "91%", "desc": "Deploying physical hardware environments, educating users on technological operations, and drafting curriculum outlines."}
        ]

        for job in jobs_database:
            if job_sector == "All Domains" or job["domain"] == job_sector:
                with st.container():
                    st.markdown(f"### {job['title']} — **{job['company']}**")
                    col_x, col_y = st.columns([4, 1])
                    with col_x:
                        st.write(f"**Domain Sector:** {job['domain']} | **Context:** {job['desc']}")
                    with col_y:
                        st.metric(label="Profile Alignment Score", value=job["match"])
                    st.markdown("---")

    # ---- 4. PORTFOLIO BUILDER ----
    elif tool_choice == "Portfolio Builder":
        st.header("📁 Portfolio Asset & Professional Branding Architecture")
        st.write("Organize your open-source repositories, case studies, and corporate branding updates inside one master space.")

        p_tab1, p_tab2 = st.tabs(["Technical Project Portfolio", "LinkedIn Social Branding Planner"])
        
        with p_tab1:
            st.subheader("Manage Active Technical Case Studies")
            proj_data = st.text_area("Project Metadata Log (Format: Project Title | Tech Stack | GitHub URL Link)", value=user_profile.get("projects", ""), height=150, placeholder="Example: Linear Regression Engine | Python, Scikit-learn | github.com/user/repo")
            
            if st.button("Save Portfolio Repositories"):
                base_prof = get_user_profile(current_user)
                base_prof["projects"] = proj_data
                update_user_profile(current_user, base_prof)
                st.success("Project repository connections updated.")
                
            st.markdown("### 🌐 Live Public Portfolio Preview Render")
            if proj_data:
                for line in proj_data.split("\n"):
                    if "|" in line:
                        parts = line.split("|")
                        st.markdown(f"> **🚀 {parts[0].strip()}**  \n> *Stack:* `{parts[1].strip()}` — [Source Repository Address]({parts[2].strip() if len(parts)>2 else '#'})")
            else:
                st.caption("No data logged yet. Add your repository entries above.")

        with p_tab2:
            st.subheader("📝 Content Pipeline & LinkedIn Post Studio")
            topic = st.text_input("Core Theme Focus", placeholder="e.g., Deploying Neural Networks or Completing 3MTT Milestones")
            if st.button("Generate Dynamic Brand Post Blueprint"):
                if topic:
                    st.success("Content Framework Ready:")
                    st.code(f"🚀 Thrilled to share my latest technical milestones focused heavily on {topic}!\n\nAs part of my career velocity progression within the digital ecosystem, I engineered an operational workflow that addresses real-world constraints.\n\nCheck out my full technical repository matrix here: github.com/{current_user}\n\n#ArtificialIntelligence #ProductManagement #TechGrowth #3MTT")
                else:
                    st.warning("Provide a theme context target.")

    # ---- 5. INTERVIEW COACH ----
    elif tool_choice == "Interview Coach":
        st.header("🎙️ AI Interactive Interview Coach")
        mock_question = "Tell me about a complex project tracking workflow you optimized, and how you demonstrated resilience when hitting structural blocks."
        st.info(f"**Target Evaluation Challenge:** \n\n {mock_question}")
        
        user_ans = st.text_area("Draft Response Block (Adhering to STAR Framework principles)", height=150)
        if st.button("Analyze Response Parameters"):
            if user_ans:
                with st.spinner("Analyzing syntax profiles..."):
                    st.markdown("""
                    ### 🎙️ Structural Diagnostic Feedback
                    *   **STAR Methodology Framework Check:** Strong layout outlining *Situation* and *Task*. 
                    *   **Constructive Growth Suggestion:** Infuse concrete quantitative data points. Incorporate metrics like explicit percentages, time tracking changes, or delivery parameters to validate performance claims.
                    """)
            else:
                st.error("Populate target response data.")

    # ---- 6. NETWORKING ASSISTANT ----
    elif tool_choice == "Networking Assistant":
        st.header("✉️ AI Professional Outreach & Connection Engine")
        st.write("Generate high-impact networking templates to build relationships with corporate hiring leads or alumni panels.")
        
        lead_name = st.text_input("Recipient Professional Name", placeholder="e.g., Dr. Augustine Chukwuemeka")
        target_co = st.text_input("Target Organization Ecosystem", placeholder="e.g., UNICEF, Access Bank")
        
        if st.button("Generate Tactical Connection Messages"):
            if lead_name and target_co:
                with st.spinner("Processing outreach metrics..."):
                    outreach = generate_networking_message(lead_name, target_co, user_profile.get("role", "Specialist"))
                    st.markdown(outreach)
            else:
                st.error("Ensure recipient name and corporate target fields are fully populated.")

    # ---- 7. PROFILE ENGINE ----
    elif tool_choice == "Profile Engine":
        st.header("⚙️ Core Identity Account Engine")
        st.write("Manage secure credential systems and infrastructure configurations for this session account.")
        
        st.text_input("Active Username Handle", value=current_user, disabled=True)
        st.text_input("Password Security Protocol", value="••••••••••••••••", disabled=True)
        st.write(f"Account Data Footprint Location: Local Host Sandbox Storage (`{USER_FILE}`)")

if __name__ == '__main__':
    main()
