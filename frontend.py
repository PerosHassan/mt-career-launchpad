import streamlit as st
import requests
import re

# Authentication
from auth import create_user, authenticate_user

# User Data
from user_data import (
    save_ai_history,
    get_user_history,
    get_user_stats,
    get_recent_activity,
    save_profile,
    get_profile,
    get_user_context,
    get_profile_completion
)

# Export Utilities
from export_utils import export_to_pdf, export_to_docx

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="MT Career Launchpad AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM STYLING
# ============================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

h1 {
    color: #2563eb;
    font-weight: bold;
}

h2 {
    color: #1e40af;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 48px;
    font-weight: bold;
}

.stTextArea textarea {
    border-radius: 10px;
}

.stTextInput input {
    border-radius: 10px;
}

.footer{
    text-align:center;
    color:gray;
    padding-top:30px;
}

.metric-box{
    background:#f7f9fc;
    padding:15px;
    border-radius:10px;
    border:1px solid #dddddd;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def clean_markdown_for_download(raw_text: str) -> str:
    """
    Strips raw markdown tags (like #, * and _) from text files 
    so they look clean and professional when opened locally.
    """
    if not raw_text:
        return ""
        
    # 1. Replace markdown headers (### Header) with capitalized spacing
    cleaned = re.sub(r'^#{1,6}\s*(.*)$', r'\n\1\n' + '='*len(r'\1'), raw_text, flags=re.MULTILINE)
    
    # 2. Remove Bold syntax (**text** -> text)
    cleaned = re.sub(r'\*\*(.*?)\*\*', r'\1', cleaned)
    
    # 3. Remove Italic syntax (*text* -> text)
    cleaned = re.sub(r'\*(.*?)\*', r'\1', cleaned)
    
    # 4. Standardize markdown bullets to neat professional dash list format
    cleaned = re.sub(r'^\s*[\*\-_]\s+', r'  - ', cleaned, flags=re.MULTILINE)
    
    # 5. Collapse excessive line breaks
    cleaned = re.sub(r'\n{3,}', r'\n\n', cleaned)
    
    return cleaned.strip()

# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "user" not in st.session_state:
    st.session_state.user = None

# ============================================================
# BACKEND CONFIGURATION & AI REQUEST FUNCTION
# ============================================================

# Swapped out local testing server for your live production Render deployment
BACKEND_URL = "https://mt-career-launchpad-api.onrender.com"

def call_ai(task: str, user_input: str):
    try:
        user_context = ""

        if st.session_state.user:
            user_context = get_user_context(st.session_state.user["id"])

        response = requests.post(
            f"{BACKEND_URL}/generate",
            json={
                "task": task,
                "input": f"""User Profile:

{user_context}

User Request:

{user_input}
"""
            },
            timeout=120
        )

        if response.status_code == 200:
            result = response.json()["response"]

            # Save AI result for logged-in user
            if st.session_state.user:
                save_ai_history(
                    user_id=st.session_state.user["id"],
                    task=task,
                    input_text=user_input,
                    ai_response=result
                )

            return result

        return f"❌ Backend Error ({response.status_code})"

    except Exception as e:
        return f"❌ Connection Error:\n\n{e}"

# ============================================================
# AUTHENTICATION FUNCTIONS
# ============================================================

def logout():
    st.session_state.user = None
    st.session_state.page = "Dashboard"
    st.rerun()

def signup_page():
    st.title("🚀 Create MT Career Launchpad Account")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    password = st.text_input("Password", type="password")

    if st.button("Create Account"):
        if not name or not email or not password:
            st.warning("Please complete all fields.")
        else:
            success = create_user(name, email, password)
            if success:
                st.success("Account created successfully. Please login.")
            else:
                st.error("Email already exists.")

def login_page():
    st.title("🔐 Login to MT Career Launchpad AI")
    email = st.text_input("Email Address")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = authenticate_user(email, password)
        if user:
            st.session_state.user = user
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid email or password.")

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.image(
        "https://img.icons8.com/color/96/artificial-intelligence.png",
        width=70
    )

    st.title("MT Career Launchpad")
    st.caption("AI Career Development Platform")
    st.divider()

    # IF USER IS LOGGED IN
    if st.session_state.user:
        st.success(f"👋 Welcome {st.session_state.user['name']}")

        if st.button("🏠 Dashboard"):
            st.session_state.page = "Dashboard"

        if st.button("👤 My Profile"):
            st.session_state.page = "Profile"

        if st.button("📚 My History"):
            st.session_state.page = "History"

        if st.button("📄 Resume Analyzer"):
            st.session_state.page = "Resume"

        if st.button("🧠 Career Assessment"):
            st.session_state.page = "Career"

        if st.button("📝 CV Builder"):
            st.session_state.page = "CV"

        if st.button("🗺 Career Roadmap"):
            st.session_state.page = "Roadmap"

        if st.button("🎤 Interview Coach"):
            st.session_state.page = "Interview"

        st.divider()

        if st.button("🚪 Logout"):
            logout()

        st.divider()
        st.success("🟢 AI Engine Online")
        st.caption("Powered by Google Gemini")

    # IF USER IS NOT LOGGED IN
    else:
        st.info("Please login to access MT Career Launchpad AI")
        option = st.radio("Account", ["Login", "Sign Up"])
        st.divider()

        if option == "Login":
            login_page()
        else:
            signup_page()

# ============================================================
# MAIN APPLICATION AREA (CHECK AUTHENTICATION)
# ============================================================

if st.session_state.user:

    # HEADER
    st.title("🚀 MT Career Launchpad AI")
    st.markdown(
        """
        ### Your AI-powered Career Development Assistant
        Helping students, graduates, and professionals build successful careers using Generative AI.
        """
    )

    # 1. DASHBOARD
    if st.session_state.page == "Dashboard":
        st.header("🏠 Dashboard")
        st.success(f"Welcome {st.session_state.user['name']} 👋")

        # USER CAREER PROGRESS (ANALYTICS)
        user_id = st.session_state.user["id"]
        stats = get_user_stats(user_id)

        st.subheader("📊 Your Career Progress")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric("📄 Resume Analyses", stats["resume"])

        with c2:
            st.metric("🧠 Career Assessments", stats["career"])

        with c3:
            st.metric("📝 CV Generations", stats["cv"])

        with c4:
            st.metric("🎤 Interview Practice", stats["interview"])

        st.divider()

        # RECENT ACTIVITY
        st.subheader("🕒 Recent Activity")
        recent = get_recent_activity(user_id)

        if not recent:
            st.info("No AI activity yet. Start using the AI tools.")
        else:
            for item in recent:
                task = item[0]
                date = item[1]
                st.write(f"🤖 **{task.upper()}** — {date}")

        st.divider()

        st.write(
            """
            MT Career Launchpad AI uses **Google Gemini Generative AI**
            to help students, graduates and professionals make smarter
            career decisions.
            
            Choose any AI tool from the sidebar to begin your journey.
            """
        )
        st.divider()

        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("### 📄 Resume Analyzer\n\n✔ ATS Score\n✔ Resume Review\n✔ Missing Skills\n✔ Improvement Tips")
        with col2:
            st.success("### 🧠 Career Coach\n\n✔ Career Advice\n✔ Certifications\n✔ Skill Gap Analysis\n✔ Career Planning")
        with col3:
            st.warning("### 🚀 AI Career Roadmap\n\n✔ Learning Plan\n✔ Monthly Goals\n✔ Portfolio Projects\n✔ Career Growth")

        st.divider()
        st.subheader("✨ Available AI Features")
        feature1, feature2 = st.columns(2)
        with feature1:
            st.markdown("✅ Resume Analyzer\n✅ Career Assessment\n✅ CV Builder\n✅ Career Roadmap")
        with feature2:
            st.markdown("✅ Interview Coach\n✅ Google Gemini AI\n✅ FastAPI Backend\n✅ Streamlit Frontend")

        st.divider()
        st.subheader("📈 Platform Overview")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("AI Features", "5")
        m2.metric("Backend", "FastAPI")
        m3.metric("Frontend", "Streamlit")
        m4.metric("Model", "Gemini")

    # 2. PROFILE PAGE
    elif st.session_state.page == "Profile":
        st.header("👤 My Profile")

        # PROFILE COMPLETION GAUGE
        completion = get_profile_completion(st.session_state.user["id"])
        st.subheader("📊 Profile Completion")
        st.progress(completion / 100)
        st.write(f"{completion}% Complete")

        user = st.session_state.user
        st.subheader("Account Information")
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Full Name", value=user["name"], disabled=True)
        with col2:
            st.text_input("Email", value=user["email"], disabled=True)

        st.divider()

        # Load existing profile
        profile = get_profile(user["id"])

        if profile:
            career_interest = profile[0]
            skills = profile[1]
            experience = profile[2]
            education = profile[3]
        else:
            career_interest = ""
            skills = ""
            experience = ""
            education = ""

        st.subheader("Career Profile")

        career_interest = st.text_input(
            "Career Goal",
            value=career_interest,
            placeholder="Example: AI Engineer, Product Manager"
        )

        skills = st.text_area(
            "Skills",
            value=skills,
            placeholder="Python, AI, Product Management..."
        )

        experience = st.text_area(
            "Experience",
            value=experience,
            placeholder="Describe your experience..."
        )

        education = st.text_area(
            "Education",
            value=education,
            placeholder="Your education background..."
        )

        if st.button("💾 Save Profile"):
            save_profile(
                user_id=user["id"],
                career_goal=career_interest,
                skills=skills,
                experience=experience,
                education=education
            )
            st.success("✅ Profile updated successfully")
            st.rerun()

    # 3. HISTORY PAGE
    elif st.session_state.page == "History":
        st.header("📚 My AI History")
        
        user_id = st.session_state.user["id"]
        history = get_user_history(user_id)

        if not history:
            st.info("You have not generated any AI content yet.")
        else:
            st.success(f"Found {len(history)} previous AI activities.")
            
            for item in history:
                task = item[0]
                response = item[1]
                date = item[2]

                with st.expander(f"🤖 {task.upper()} | {date}"):
                    st.write(response)

    # 4. RESUME ANALYZER (WITH NEW PDF & WORD EXPORT FORMATS)
    elif st.session_state.page == "Resume":
        st.header("📄 AI Resume Analyzer")
        st.write("Upload or paste your resume below and let AI evaluate it professionally.")
        resume = st.text_area("Resume", height=320, placeholder="Paste your complete resume here...")

        if st.button("🚀 Analyze Resume", use_container_width=True):
            if not resume.strip():
                st.warning("Please paste your resume first.")
            else:
                with st.spinner("🤖 Gemini AI is analyzing your resume..."):
                    result = call_ai(task="resume", user_input=resume)
                st.success("✅ Resume Analysis Complete")
                st.markdown(result)
                
                # Dynamic generation of PDF and DOCX files
                pdf_file = export_to_pdf("Resume Analysis Report", result)
                docx_file = export_to_docx("Resume Analysis Report", result)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.download_button(
                        "📄 Download PDF",
                        data=pdf_file,
                        file_name="resume_analysis_report.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )
                    
                with col2:
                    st.download_button(
                        "📝 Download Word",
                        data=docx_file,
                        file_name="resume_analysis_report.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                        use_container_width=True
                    )

    # 5. CAREER ASSESSMENT
    elif st.session_state.page == "Career":
        st.header("🧠 AI Career Assessment")
        st.write("Tell the AI about your education, skills and career goals.")
        career_info = st.text_area("Your Information", height=280, placeholder="Education:\nSkills:\nExperience:\nCareer Goal:\nInterests:")

        if st.button("🚀 Generate Career Advice", use_container_width=True):
            if not career_info.strip():
                st.warning("Please enter your information.")
            else:
                with st.spinner("🤖 MT AI is preparing your career advice..."):
                    result = call_ai(task="career", user_input=career_info)
                st.success("✅ Career Assessment Complete")
                st.markdown(result)
                
                # Strip markdown syntax for pristine plain text exports
                cleaned_result = clean_markdown_for_download(result)
                
                st.download_button(
                    "📥 Download Career Advice", 
                    cleaned_result, 
                    file_name="career_advice.txt", 
                    mime="text/plain"
                )

    # 6. CV BUILDER
    elif st.session_state.page == "CV":
        st.header("📝 AI CV Builder")
        st.write("Provide your professional information to generate an ATS-friendly CV.")
        cv_info = st.text_area("Professional Information", height=320, placeholder="Name\nEducation\nExperience\nSkills...")

        if st.button("🚀 Generate CV", use_container_width=True):
            if not cv_info.strip():
                st.warning("Please enter your professional information.")
            else:
                with st.spinner("🤖 Gemini AI is writing your professional CV..."):
                    result = call_ai(task="cv", user_input=cv_info)
                st.success("✅ CV Generated Successfully")
                st.markdown(result)
                
                # Strip markdown syntax for pristine plain text exports
                cleaned_result = clean_markdown_for_download(result)
                
                st.download_button(
                    "📥 Download CV", 
                    cleaned_result, 
                    file_name="generated_cv.txt", 
                    mime="text/plain"
                )

    # 7. CAREER ROADMAP
    elif st.session_state.page == "Roadmap":
        st.header("🗺️ AI Career Roadmap")
        st.write("Tell the AI your dream career and receive a personalized 12-month roadmap.")
        career_goal = st.text_input("Career Goal", placeholder="Example: AI Engineer")

        if st.button("🚀 Generate Career Roadmap", use_container_width=True):
            if not career_goal.strip():
                st.warning("Please enter your career goal.")
            else:
                with st.spinner("🤖 Gemini AI is creating your learning roadmap..."):
                    result = call_ai(task="roadmap", user_input=career_goal)
                st.success("✅ Career Roadmap Generated")
                st.markdown(result)
                
                # Strip markdown syntax for pristine plain text exports
                cleaned_result = clean_markdown_for_download(result)
                
                st.download_button(
                    "📥 Download Roadmap", 
                    cleaned_result, 
                    file_name="career_roadmap.txt", 
                    mime="text/plain"
                )

    # 8. INTERVIEW COACH
    elif st.session_state.page == "Interview":
        st.header("🎤 AI Interview Coach")
        st.write("Prepare for your next interview with personalized AI coaching.")
        job_role = st.text_input("Target Job Role", placeholder="Example: Product Manager")

        if st.button("🚀 Generate Interview Preparation", use_container_width=True):
            if not job_role.strip():
                st.warning("Please enter a job role.")
            else:
                with st.spinner("🤖 Preparing interview questions and answers..."):
                    result = call_ai(task="interview", user_input=job_role)
                st.success("✅ Interview Preparation Ready")
                st.markdown(result)
                
                # Strip markdown syntax for pristine plain text exports
                cleaned_result = clean_markdown_for_download(result)
                
                st.download_button(
                    "📥 Download Interview Guide", 
                    cleaned_result, 
                    file_name="interview_preparation.txt", 
                    mime="text/plain"
                )

# ============================================================
# NOT LOGGED IN SCREEN
# ============================================================
else:
    st.title("🚀 MT Career Launchpad AI")
    st.info(
        """
        Welcome to MT Career Launchpad AI.
        
        Please create an account or login from the sidebar
        to access your AI career development tools.
        """
    )

# ============================================================
# FOOTER
# ============================================================
st.divider()
st.markdown(
    """
    <div class="footer">
    ### 🚀 MT Career Launchpad AI
    Powered by **Google Gemini AI**, **FastAPI**, and **Streamlit**.  
    Designed to help students, graduates, and professionals make smarter career decisions with Generative AI.  
    © 2026 MT Career Launchpad. All Rights Reserved.
    </div>
    """,
    unsafe_allow_html=True
)
