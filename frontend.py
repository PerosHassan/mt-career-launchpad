import streamlit as st
import requests
# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="MT Career Launchpad",
    page_icon="🚀",
    layout="wide"
)
# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"
# ============================================================
# BACKEND URL
# ============================================================

BACKEND_URL = "http://localhost:8000"
# ============================================================
# SEND REQUEST TO AI ENGINE
# ============================================================

def call_ai(task: str, user_input: str):

    try:

        response = requests.post(
            f"{BACKEND_URL}/generate",
            json={
                "task": task,
                "input": user_input
            }
        )

        if response.status_code == 200:
            return response.json()["response"]

        return f"Backend Error: {response.status_code}"

    except Exception as e:
        return f"Connection Error: {e}"
# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

with st.sidebar:

    st.title("🚀 MT Career Launchpad")

    st.markdown("---")

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

    st.markdown("---")
    st.caption("Powered by Google Gemini AI")
# ============================================================
# APPLICATION TITLE
# ============================================================

st.title("🚀 MT Career Launchpad")

st.markdown(
    "### Your AI-powered Career Development Assistant"
)
# ============================================================
# DASHBOARD
# ============================================================

if st.session_state.page == "Dashboard":

    st.header("🏠 Dashboard")

    st.success(
        "Welcome to MT Career Launchpad!"
    )

    st.write(
        """
MT Career Launchpad uses Generative AI to help users:

- Analyze resumes
- Discover career paths
- Build professional CVs
- Generate career roadmaps
- Prepare for interviews
"""
    )

    st.info(
        "Select a feature from the sidebar to begin."
    )
    # ============================================================
# AI RESUME ANALYZER
# ============================================================

elif st.session_state.page == "Resume":

    st.header("📄 AI Resume Analyzer")

    st.write(
        "Paste your resume below and let the AI analyze it."
    )

    resume = st.text_area(
        "Resume",
        height=300,
        placeholder="Paste your resume here..."
    )

    if st.button("Analyze Resume"):

        if not resume.strip():

            st.warning("Please paste your resume first.")

        else:

            with st.spinner("Analyzing your resume..."):

                result = call_ai(
                    task="resume",
                    user_input=resume
                )

                st.success("Analysis Complete")

                st.markdown(result)
                # ============================================================
# CAREER ASSESSMENT
# ============================================================

elif st.session_state.page == "Career":

    st.header("🧠 AI Career Assessment")

    st.write(
        "Tell the AI about yourself to receive personalized career advice."
    )

    career_info = st.text_area(
        "Your Information",
        height=250,
        placeholder="Describe your education, skills, interests and career goals..."
    )

    if st.button("Get Career Advice"):

        if not career_info.strip():

            st.warning("Please enter your information.")

        else:

            with st.spinner("Generating career advice..."):

                result = call_ai(
                    task="career",
                    user_input=career_info
                )

                st.success("Career Assessment Complete")

                st.markdown(result)
                # ============================================================
# CV BUILDER
# ============================================================

elif st.session_state.page == "CV":

    st.header("📝 AI CV Builder")

    st.write(
        "Provide your professional information to generate an ATS-friendly CV."
    )

    cv_info = st.text_area(
        "CV Information",
        height=300,
        placeholder="Education, experience, projects, skills..."
    )

    if st.button("Generate CV"):

        if not cv_info.strip():

            st.warning("Please enter your information.")

        else:

            with st.spinner("Generating your CV..."):

                result = call_ai(
                    task="cv",
                    user_input=cv_info
                )

                st.success("CV Generated Successfully")

                st.markdown(result)
                # ============================================================
# CAREER ROADMAP
# ============================================================

elif st.session_state.page == "Roadmap":

    st.header("🗺 AI Career Roadmap")

    st.write(
        "Enter your dream career and receive a personalized learning roadmap."
    )

    career_goal = st.text_input(
        "Career Goal",
        placeholder="Example: Product Manager"
    )

    if st.button("Generate Roadmap"):

        if not career_goal.strip():

            st.warning("Please enter a career goal.")

        else:

            with st.spinner("Creating your roadmap..."):

                result = call_ai(
                    task="roadmap",
                    user_input=career_goal
                )

                st.success("Roadmap Generated Successfully")

                st.markdown(result)





