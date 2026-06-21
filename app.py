"""
MT Graduate Career Launchpad
Powered by Qwen 3.7 Plus

A single-file Streamlit application for career support.
- Secure user authentication (File-based)
- Home Dashboard with rich content
- AI CV Builder
- Cover Letter Generator
- Interview Coach

To run this application:
1. Install Streamlit: pip install streamlit
2. Run the app: streamlit run app.py
"""

import streamlit as st
import json
import hashlib
import os

# =============================================================================
# FILE MANAGEMENT & AUTHENTICATION FUNCTIONS
# =============================================================================

USER_FILE = "users.json"

def hash_password(password):
    """Securely hash passwords using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    """Load users from the local JSON file."""
    if not os.path.exists(USER_FILE):
        return {}
    try:
        with open(USER_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {}

def save_users(users):
    """Save users to the local JSON file."""
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

def register_user(username, password):
    """Register a new user if the username doesn't already exist."""
    users = load_users()
    if username in users:
        return False
    users[username] = hash_password(password)
    save_users(users)
    return True

def authenticate_user(username, password):
    """Verify user credentials."""
    users = load_users()
    if username in users and users[username] == hash_password(password):
        return True
    return False

# =============================================================================
# MOCK AI GENERATION FUNCTIONS (Ready for Qwen 3.7 Plus Integration)
# =============================================================================

def generate_cv_critique(cv_text, job_description):
    """Mock AI CV Builder analysis."""
    return f"""
    ### 🚀 Qwen AI CV Analysis & Recommendations
    
    **Strengths Identified:**
    * Good structural layout and clear formatting.
    * Strong foundational technical terms detected in text.

    **Areas for Improvement regarding the Job Description:**
    * **Action Verbs:** Enhance your professional summary using dynamic verbs (e.g., 'Spearheaded', 'Optimized').
    * **Keyword Alignment:** The job description heavily mentions *"{job_description[:30]}..."*. Make sure these exact phrases are reflected in your experience.
    
    **Tailored Summary Suggestion:**
    "Ambitious Management Trainee graduate with hands-on experience in project coordination and data analysis, tailored perfectly to meet the challenges of this role."
    """

def generate_cover_letter(user_profile, company_name, job_title):
    """Mock Cover Letter Generator."""
    return f"""
    Dear Hiring Team at {company_name},
    
    I am writing to express my strong interest in the {job_title} position. As a recent graduate of the MT Graduate Career Launchpad program, I have honed intensive skills perfectly aligned with your team's mission.
    
    My background includes:
    {user_profile}
    
    I am highly drawn to {company_name} because of your industry-leading innovation. I am confident that my proactive drive makes me an asset to your workforce. Thank you for your time and consideration.
    
    Sincerely,
    [Your Name]
    """

def generate_interview_feedback(question, user_answer):
    """Mock Interview Coach feedback."""
    return f"""
    ### 🎙️ Interview Coach Feedback
    
    **Question Evaluated:** *"{question}"*
    
    **Feedback on your response:**
    * **STAR Method Alignment:** Your response touches on the *Situation* and *Task*, but could structure the *Action* and *Result* segments more clearly.
    * **Tone & Delivery:** Highly professional and confident. 
    
    **💡 Refined Answer Suggestion:**
    Try adding concrete metrics. Instead of saying "I helped the team save time," try: *"By automating our data ingestion pipeline, I reduced weekly processing cycles by 15%."*
    """

# =============================================================================
# STREAMLIT UI APPLICATION
# =============================================================================

def main():
    st.set_page_config(page_title="MT Graduate Career Launchpad", page_icon="💼", layout="wide")
    
    # Initialize session state variables for login tracking
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""

    # ---- SIDEBAR: AUTHENTICATION & NAVIGATION ----
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
                    st.sidebar.error("Invalid username or password.")
        else:
            if st.sidebar.button("Register Account"):
                if username and password:
                    if register_user(username, password):
                        st.sidebar.success("Registration successful! Please Log In.")
                    else:
                        st.sidebar.error("Username already exists.")
                else:
                    st.sidebar.error("Please fill out both fields.")
                    
        st.info("Please log in or register via the sidebar to access the AI Career Tools.")
        return

    # ---- AUTHENTICATED USER INTERFACE ----
    st.sidebar.success(f"Logged in as: **{st.session_state.username}**")
    
    # Tool Navigation Menu
    tool_choice = st.sidebar.selectbox(
        "Select AI Tool", 
        ["Home Dashboard", "AI CV Builder", "Cover Letter Generator", "Interview Coach"]
    )
    
    # Logout Button at the bottom of sidebar
    st.sidebar.markdown("---")
    if st.sidebar.button("Log Out"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    # ---- MAIN APP INTERACTION PAGES ----
    st.title("🚀 MT Graduate Career Launchpad")
    st.caption("Powered by Qwen 3.7 Plus AI Architecture")
    st.markdown("---")

    # Welcoming, content-rich Home Dashboard
    if tool_choice == "Home Dashboard":
        st.subheader(f"Welcome back, {st.session_state.username}! 👋")
        st.markdown("""
        Welcome to your intelligent career acceleration suite. This platform is specifically tailored to help 
        graduates refine their professional branding, optimize application assets, and ace competitive interviews.
        
        ### 💡 Available Intelligence Tools:
        """)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("### 📝 AI CV Builder\n\nTailor your current resume against any target job description. Uncover skill gaps and instantly optimize your keywords.")
        with col2:
            st.success("### ✉️ Cover Letter Builder\n\nGenerate high-impact, completely bespoke cover letters highlighting your unique background for specific employers.")
        with col3:
            st.warning("### 🎙️ Interview Coach\n\nPractice tough behavioral interview questions and receive structured feedback utilizing the STAR methodology.")
            
        st.markdown("---")
        st.markdown("""
        ### 📱 Mobile User Tip:
        If you are on a mobile device, **tap the small arrow icon (`>`) at the top-left corner** of your screen to open the navigation menu and launch a specific tool!
        """)

    # TOOL 1: AI CV Builder
    elif tool_choice == "AI CV Builder":
        st.header("📝 AI CV Builder & Tailoring Tool")
        st.write("Paste your current CV text and target job description to optimize your content.")
        
        col1, col2 = st.columns(2)
        with col1:
            cv_input = st.text_area("Your Current CV Text", height=250, placeholder="Paste your resume details here...")
        with col2:
            jd_input = st.text_area("Target Job Description", height=250, placeholder="Paste the job advertisement requirements here...")
            
        if st.button("Analyze & Optimize CV"):
            if cv_input and jd_input:
                with st.spinner("Qwen AI is reviewing your layout and syntax..."):
                    feedback = generate_cv_critique(cv_input, jd_input)
                    st.markdown(feedback)
            else:
                st.warning("Please provide both your CV and the Job Description to continue.")

    # TOOL 2: Cover Letter Generator
    elif tool_choice == "Cover Letter Generator":
        st.header("✉️ Cover Letter Generator")
        st.write("Generate a bespoke, professional cover letter tailored to your dream organization.")
        
        comp_name = st.text_input("Company Name", placeholder="e.g., Google, McKinsey, Stripe")
        j_title = st.text_input("Job Title", placeholder="e.g., Management Trainee, Associate Consultant")
        u_profile = st.text_area("Key Highlights of Your Profile", height=150, placeholder="e.g., Computer Science honors graduate with 2 internships in data analysis and agile scrum experience.")
        
        if st.button("Generate Cover Letter"):
            if comp_name and j_title and u_profile:
                with st.spinner("Drafting high-impact cover letter via Qwen AI..."):
                    letter = generate_cover_letter(u_profile, comp_name, j_title)
                    st.success("Cover letter generated successfully!")
                    st.text_area("Generated Output", value=letter.strip(), height=350)
            else:
                st.warning("Please fill out all the input fields.")

    # TOOL 3: Interview Coach
    elif tool_choice == "Interview Coach":
        st.header("🎙️ AI Interactive Interview Coach")
        st.write("Practice answering challenging behavioral or technical questions and receive immediate smart feedback.")
        
        mock_question = "Tell me about a time you had to deal with a conflict within a cross-functional team, and how you resolved it."
        st.info(f"**Practice Question:** \n\n {mock_question}")
        
        user_ans = st.text_area("Your Response (Use the STAR Method: Situation, Task, Action, Result)", height=200, placeholder="Type your answer here...")
        
        if st.button("Submit Response for Feedback"):
            if user_ans:
                with st.spinner("Analyzing communication frameworks and metrics..."):
                    coach_feedback = generate_interview_feedback(mock_question, user_ans)
                    st.markdown(coach_feedback)
            else:
                st.warning("Please type an answer before requesting feedback.")

if __name__ == '__main__':
    main()
