import streamlit as st
import requests

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
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# ============================================================
# BACKEND CONFIGURATION
# ============================================================

BACKEND_URL = "http://localhost:8000"

# ============================================================
# AI REQUEST FUNCTION
# ============================================================

def call_ai(task: str, user_input: str):
    try:
        response = requests.post(
            f"{BACKEND_URL}/generate",
            json={
                "task": task,
                "input": user_input
            },
            timeout=120
        )

        if response.status_code == 200:
            return response.json()["response"]

        return f"❌ Backend Error ({response.status_code})"

    except Exception as e:
        return f"❌ Connection Error:\n\n{e}"

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

    if st.button("🏠 Dashboard"):
        st.session_state.page = "Dashboard"

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
    st.success("🟢 AI Engine Online")
    st.caption("Powered by Google Gemini")

# ============================================================
# HEADER
# ============================================================

st.title("🚀 MT Career Launchpad AI")

st.markdown(
"""
### Your AI-powered Career Development Assistant

Helping students, graduates, and professionals build successful careers using Generative AI.
"""
)

# ============================================================
# DASHBOARD
# ============================================================

if st.session_state.page == "Dashboard":
    st.header("🏠 Dashboard")
    st.success("Welcome to MT Career Launchpad AI")

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
        st.info(
            """
### 📄 Resume Analyzer

✔ ATS Score
✔ Resume Review
✔ Missing Skills
✔ Improvement Tips
"""
        )

    with col2:
        st.success(
            """
### 🧠 Career Coach

✔ Career Advice
✔ Certifications
✔ Skill Gap Analysis
✔ Career Planning
"""
        )

    with col3:
        st.warning(
            """
### 🚀 AI Career Roadmap

✔ Learning Plan
✔ Monthly Goals
✔ Portfolio Projects
✔ Career Growth
"""
        )

    st.divider()

    st.subheader("✨ Available AI Features")
    feature1, feature2 = st.columns(2)

    with feature1:
        st.markdown("""
✅ Resume Analyzer
✅ Career Assessment
✅ CV Builder
✅ Career Roadmap
""")

    with feature2:
        st.markdown("""
✅ Interview Coach
✅ Google Gemini AI
✅ FastAPI Backend
✅ Streamlit Frontend
""")

    st.divider()

    st.subheader("📈 Platform Overview")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("AI Features", "5")
    m2.metric("Backend", "FastAPI")
    m3.metric("Frontend", "Streamlit")
    m4.metric("Model", "Gemini")

    st.divider()

    st.info(
        """
### 🚀 How to Use

1. Select an AI feature from the sidebar.
2. Enter your information.
3. Click Generate.
4. Review your personalized AI response.
5. Improve your career with actionable recommendations.
"""
    )

# ============================================================
# AI RESUME ANALYZER
# ============================================================

elif st.session_state.page == "Resume":
    st.header("📄 AI Resume Analyzer")
    st.write("Upload or paste your resume below and let AI evaluate it professionally.")

    resume = st.text_area(
        "Resume",
        height=320,
        placeholder="Paste your complete resume here..."
    )

    if st.button("🚀 Analyze Resume", use_container_width=True):
        if not resume.strip():
            st.warning("Please paste your resume first.")
        else:
            with st.spinner("🤖 Gemini AI is analyzing your resume..."):
                result = call_ai(task="resume", user_input=resume)

            st.success("✅ Resume Analysis Complete")
            st.markdown(result)
            st.download_button(
                label="📥 Download Analysis",
                data=result,
                file_name="resume_analysis.txt",
                mime="text/plain"
            )

# ============================================================
# CAREER ASSESSMENT
# ============================================================

elif st.session_state.page == "Career":
    st.header("🧠 AI Career Assessment")
    st.write("Tell the AI about your education, skills and career goals.")

    career_info = st.text_area(
        "Your Information",
        height=280,
        placeholder="""
Example:

Education:
Skills:
Experience:
Career Goal:
Interests:
"""
    )

    if st.button("🚀 Generate Career Advice", use_container_width=True):
        if not career_info.strip():
            st.warning("Please enter your information.")
        else:
            with st.spinner("🤖 MT AI is preparing your career advice..."):
                result = call_ai(task="career", user_input=career_info)

            st.success("✅ Career Assessment Complete")
            st.markdown(result)
            st.download_button(
                "📥 Download Career Advice",
                result,
                file_name="career_advice.txt",
                mime="text/plain"
            )

# ============================================================
# CV BUILDER
# ============================================================

elif st.session_state.page == "CV":
    st.header("📝 AI CV Builder")
    st.write("Provide your professional information to generate an ATS-friendly CV.")

    cv_info = st.text_area(
        "Professional Information",
        height=320,
        placeholder="""
Name
Education
Experience
Projects
Skills
Certifications
Achievements
"""
    )

    if st.button("🚀 Generate CV", use_container_width=True):
        if not cv_info.strip():
            st.warning("Please enter your professional information.")
        else:
            with st.spinner("🤖 Gemini AI is writing your professional CV..."):
                result = call_ai(task="cv", user_input=cv_info)

            st.success("✅ CV Generated Successfully")
            st.markdown(result)
            st.download_button(
                "📥 Download CV",
                result,
                file_name="generated_cv.txt",
                mime="text/plain"
            )

# ============================================================
# CAREER ROADMAP
# ============================================================

elif st.session_state.page == "Roadmap":
    st.header("🗺️ AI Career Roadmap")
    st.write("Tell the AI your dream career and receive a personalized 12-month roadmap.")

    career_goal = st.text_input(
        "Career Goal",
        placeholder="Example: AI Engineer, Product Manager, Data Scientist"
    )

    if st.button("🚀 Generate Career Roadmap", use_container_width=True):
        if not career_goal.strip():
            st.warning("Please enter your career goal.")
        else:
            with st.spinner("🤖 Gemini AI is creating your learning roadmap..."):
                result = call_ai(task="roadmap", user_input=career_goal)

            st.success("✅ Career Roadmap Generated")
            st.markdown(result)
            st.download_button(
                "📥 Download Roadmap",
                result,
                file_name="career_roadmap.txt",
                mime="text/plain"
            )

# ============================================================
# INTERVIEW COACH
# ============================================================

elif st.session_state.page == "Interview":
    st.header("🎤 AI Interview Coach")
    st.write("Prepare for your next interview with personalized AI coaching.")

    job_role = st.text_input(
        "Target Job Role",
        placeholder="Example: Product Manager"
    )

    if st.button("🚀 Generate Interview Preparation", use_container_width=True):
        if not job_role.strip():
            st.warning("Please enter a job role.")
        else:
            with st.spinner("🤖 Preparing interview questions and answers..."):
                result = call_ai(task="interview", user_input=job_role)

            st.success("✅ Interview Preparation Ready")
            st.markdown(result)
            st.download_button(
                "📥 Download Interview Guide",
                result,
                file_name="interview_preparation.txt",
                mime="text/plain"
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
