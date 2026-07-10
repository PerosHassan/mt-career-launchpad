import streamlit as st
import requests

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="MT Career Launchpad",
    page_icon="🚀",
    layout="wide"
)

# -------------------------------
# Session State
# -------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# -------------------------------
# Backend URL
# -------------------------------
BACKEND_URL = "http://localhost:8000"

# -------------------------------
# Sidebar
# -------------------------------
with st.sidebar:
    st.title("🚀 MT Career Launchpad")
    st.markdown("---")

    if st.button("🏠 Dashboard"):
        st.session_state.page = "Dashboard"

    if st.button("🤖 AI Resume Analyzer"):
        st.session_state.page = "Resume"

    if st.button("🧠 Career Assessment"):
        st.session_state.page = "Assessment"

    if st.button("📄 CV Builder"):
        st.session_state.page = "CV"

    if st.button("🗺 Career Roadmap"):
        st.session_state.page = "Roadmap"

st.title("🚀 MT Career Launchpad")
st.markdown("### Your AI-powered career development assistant")

# -------------------------------
# Dashboard
# -------------------------------
if st.session_state.page == "Dashboard":

    st.header("🏠 Dashboard")

    st.info(
        "Welcome to MT Career Launchpad.\n\n"
        "Choose a feature from the sidebar to begin."
    )

    st.write("### Available Features")

    st.markdown("""
- 🤖 AI Resume Analyzer
- 🧠 Career Assessment
- 📄 CV Builder
- 🗺 Career Roadmap
""")

# -------------------------------
# AI Resume Analyzer
# -------------------------------
elif st.session_state.page == "Resume":

    st.header("🤖 AI Resume Analyzer")

    resume = st.text_area(
        "Paste your resume below:",
        height=300
    )

    if st.button("Analyze Resume"):

        if resume.strip() == "":
            st.warning("Please paste your resume first.")

        else:
            with st.spinner("Analyzing your resume..."):

                try:
                    response = requests.post(
                        f"{BACKEND_URL}/generate",
                        json={
                            "prompt": f"""
Analyze the following resume and provide:

1. Overall score out of 100.
2. Strengths.
3. Weaknesses.
4. Missing skills.
5. ATS optimization tips.
6. Recommended improvements.

Resume:

{resume}
"""
                        }
                    )

                    if response.status_code == 200:
                        result = response.json()
                        st.success("Analysis Complete")
                        st.write(result["response"])

                    else:
                        st.error(
                            f"Backend Error: {response.status_code}"
                        )

                except Exception as e:
                    st.error(f"Connection Error: {e}")

# -------------------------------
# Career Assessment
# -------------------------------
elif st.session_state.page == "Assessment":

    st.header("🧠 Career Assessment")

    interests = st.text_area(
        "Tell us about your interests, skills, education, and career goals:",
        height=250
    )

    if st.button("Get Career Advice"):

        if interests.strip() == "":
            st.warning("Please enter your information first.")

        else:
            with st.spinner("Generating career advice..."):

                try:
                    response = requests.post(
                        f"{BACKEND_URL}/generate",
                        json={
                            "prompt": f"""
Based on the information below, provide:

1. Best career paths.
2. Skills to learn.
3. Certifications to obtain.
4. Job opportunities.
5. A one-year career roadmap.

User Information:

{interests}
"""
                        }
                    )

                    if response.status_code == 200:
                        result = response.json()
                        st.success("Career Assessment Complete")
                        st.write(result["response"])

                    else:
                        st.error(f"Backend Error: {response.status_code}")

                except Exception as e:
                    st.error(f"Connection Error: {e}")

# -------------------------------
# CV Builder
# -------------------------------
elif st.session_state.page == "CV":

    st.header("📄 AI CV Builder")

    cv_info = st.text_area(
        "Enter your education, work experience, skills, achievements, and certifications:",
        height=300
    )

    if st.button("Generate CV"):

        if cv_info.strip() == "":
            st.warning("Please enter your information first.")

        else:
            with st.spinner("Generating professional CV..."):

                try:
                    response = requests.post(
                        f"{BACKEND_URL}/generate",
                        json={
                            "prompt": f"""
Using the information below, create a professional ATS-friendly CV with:

1. Professional Summary
2. Skills
3. Education
4. Work Experience
5. Certifications
6. Projects
7. Achievements

Information:

{cv_info}
"""
                        }
                    )

                    if response.status_code == 200:
                        result = response.json()
                        st.success("CV Generated Successfully")
                        st.write(result["response"])

                    else:
                        st.error(f"Backend Error: {response.status_code}")

                except Exception as e:
                    st.error(f"Connection Error: {e}")

# -------------------------------
# Career Roadmap
# -------------------------------
elif st.session_state.page == "Roadmap":

    st.header("🗺 AI Career Roadmap")

    career_goal = st.text_input(
        "What career are you interested in?"
    )

    if st.button("Generate Roadmap"):

        if career_goal.strip() == "":
            st.warning("Please enter a career goal.")

        else:
            with st.spinner("Generating roadmap..."):

                try:
                    response = requests.post(
                        f"{BACKEND_URL}/generate",
                        json={
                            "prompt": f"""
Create a detailed learning roadmap for someone who wants to become:

{career_goal}

Include:

1. Beginner skills
2. Intermediate skills
3. Advanced skills
4. Recommended certifications
5. Free learning resources
6. Portfolio projects
7. Timeline for 12 months
8. Career opportunities
"""
                        }
                    )

                    if response.status_code == 200:
                        result = response.json()
                        st.success("Roadmap Generated Successfully")
                        st.write(result["response"])

                    else:
                        st.error(f"Backend Error: {response.status_code}")

                except Exception as e:
                    st.error(f"Connection Error: {e}")
