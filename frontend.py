import streamlit as st
import requests

# ------------------------------------
# Page Configuration
# ------------------------------------
st.set_page_config(
    page_title="MT Career Launchpad",
    page_icon="🚀",
    layout="wide"
)

# ------------------------------------
# Backend API URL
# ------------------------------------
API_URL = "http://backend:8000/generate"

# ------------------------------------
# Session State
# ------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# ------------------------------------
# Sidebar Navigation
# ------------------------------------
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

    if st.button("💼 Job Recommendations"):
        st.session_state.page = "Jobs"

    if st.button("📚 Learning Hub"):
        st.session_state.page = "Learning"

    if st.button("⚙ Settings"):
        st.session_state.page = "Settings"

# ------------------------------------
# Dashboard
# ------------------------------------
if st.session_state.page == "Dashboard":

    st.title("🚀 MT Career Launchpad")

    st.subheader("Welcome!")

    st.write("""
This platform helps students, graduates, and professionals accelerate their careers using Artificial Intelligence.

### Features

- 🤖 AI Resume Analyzer
- 🧠 Career Assessment
- 📄 CV Builder
- 🗺 Career Roadmap Generator
- 💼 Job Recommendations
- 📚 Learning Hub

Use the sidebar to explore each feature.
""")
  # ------------------------------------
# AI Resume Analyzer
# ------------------------------------
elif st.session_state.page == "Resume":

    st.title("🤖 AI Resume Analyzer")

    st.write(
        "Upload or paste your resume below and receive AI-powered feedback."
    )

    resume = st.text_area(
        "Paste your Resume",
        height=300,
        placeholder="Paste your resume here..."
    )

    if st.button("Analyze Resume"):

        if resume.strip() == "":
            st.warning("Please paste your resume first.")

        else:
            with st.spinner("Analyzing your resume..."):

                try:
                    response = requests.post(
                        API_URL,
                        json={
                            "prompt": f"""
Analyze the following resume and provide:
1. Strengths
2. Weaknesses
3. Missing Skills
4. ATS Score
5. Improvement Suggestions

Resume:

{resume}
"""
                        }
                    )

                    if response.status_code == 200:
                        st.success("Analysis Complete")
                        st.write(response.json()["response"])
                    else:
                        st.error("Backend returned an error.")

                except Exception as e:
                    st.error(f"Connection Error: {e}")
                  # ------------------------------------
# Career Assessment
# ------------------------------------
elif st.session_state.page == "Assessment":

    st.title("🧠 Career Assessment")

    st.write(
        "Answer the questions below and receive AI-powered career recommendations."
    )

    interests = st.text_area(
        "What are your interests?",
        placeholder="Example: Technology, design, business, healthcare..."
    )

    skills = st.text_area(
        "What skills do you currently have?",
        placeholder="Example: Python, graphic design, communication..."
    )

    goals = st.text_area(
        "What are your career goals?",
        placeholder="Describe your dream career..."
    )

    if st.button("Generate Career Advice"):

        if not interests or not skills or not goals:
            st.warning("Please complete all fields.")

        else:
            with st.spinner("Analyzing your profile..."):

                prompt = f"""
You are a professional career coach.

Based on the following information:

Interests:
{interests}

Skills:
{skills}

Career Goals:
{goals}

Provide:

1. Best career paths
2. Recommended skills to learn
3. Certifications
4. Learning roadmap
5. Final career advice
"""

                try:
                    response = requests.post(
                        API_URL,
                        json={"prompt": prompt}
                    )

                    if response.status_code == 200:
                        st.success("Assessment Complete!")
                        st.write(response.json()["response"])
                    else:
                        st.error("Unable to generate assessment.")

                except Exception as e:
                    st.error(f"Error: {e}")
                  # ------------------------------------
# CV Builder
# ------------------------------------
elif st.session_state.page == "CV":

    st.title("📄 AI CV Builder")

    st.write("Enter your details below to generate a professional CV.")

    full_name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    education = st.text_area("Education")
    experience = st.text_area("Work Experience")
    skills = st.text_area("Skills")
    certifications = st.text_area("Certifications")

    if st.button("Generate Professional CV"):

        if (
            not full_name
            or not email
            or not education
            or not skills
        ):
            st.warning("Please complete all required fields.")

        else:
            with st.spinner("Generating your professional CV..."):

                prompt = f"""
Create a professional ATS-friendly CV using the following information.

Name:
{full_name}

Email:
{email}

Phone:
{phone}

Education:
{education}

Experience:
{experience}

Skills:
{skills}

Certifications:
{certifications}

Generate a clean professional CV suitable for international job applications.
"""

                try:
                    response = requests.post(
                        API_URL,
                        json={"prompt": prompt}
                    )

                    if response.status_code == 200:
                        st.success("CV Generated Successfully!")
                        st.write(response.json()["response"])
                    else:
                        st.error("Failed to generate CV.")

                except Exception as e:
                    st.error(f"Error: {e}")
                  # ------------------------------------
# Career Roadmap
# ------------------------------------
elif st.session_state.page == "Roadmap":

    st.title("🗺 AI Career Roadmap")

    career_goal = st.text_input(
        "What career do you want to pursue?"
    )

    if st.button("Generate Roadmap"):

        if not career_goal:
            st.warning("Please enter a career goal.")

        else:
            with st.spinner("Creating your roadmap..."):

                prompt = f"""
Create a detailed learning roadmap for someone who wants to become a {career_goal}.

Include:

1. Beginner Stage
2. Intermediate Stage
3. Advanced Stage
4. Recommended Certifications
5. Projects to Build
6. Estimated Timeline
"""

                try:
                    response = requests.post(
                        API_URL,
                        json={"prompt": prompt}
                    )

                    if response.status_code == 200:
                        st.success("Roadmap Ready!")
                        st.write(response.json()["response"])
                    else:
                        st.error("Unable to generate roadmap.")

                except Exception as e:
                    st.error(f"Error: {e}")


# ------------------------------------
# Job Recommendations
# ------------------------------------
elif st.session_state.page == "Jobs":

    st.title("💼 Job Recommendations")

    skills = st.text_area(
        "Enter your skills",
        placeholder="Example: Python, UI/UX Design, Data Analysis..."
    )

    if st.button("Find Matching Jobs"):

        if not skills:
            st.warning("Please enter your skills.")

        else:
            with st.spinner("Finding job recommendations..."):

                prompt = f"""
Recommend suitable jobs for someone with these skills:

{skills}

Include:

1. Job Titles
2. Responsibilities
3. Expected Salary
4. Companies Hiring
5. Skills to Improve
"""

                try:
                    response = requests.post(
                        API_URL,
                        json={"prompt": prompt}
                    )

                    if response.status_code == 200:
                        st.success("Recommendations Ready!")
                        st.write(response.json()["response"])
                    else:
                        st.error("Unable to fetch recommendations.")

                except Exception as e:
                    st.error(f"Error: {e}")


# ------------------------------------
# Learning Hub
# ------------------------------------
elif st.session_state.page == "Learning":

    st.title("📚 Learning Hub")

    st.markdown("""
### Recommended Learning Resources

- 🐍 Python Programming
- 🤖 Artificial Intelligence
- 🎨 UI/UX Design
- 💻 Web Development
- ☁️ Cloud Computing
- 📊 Data Science
- 🔒 Cybersecurity
- 📱 Mobile App Development

Continue learning every day to grow your career!
""")
  # ------------------------------------
# Settings
# ------------------------------------
elif st.session_state.page == "Settings":

    st.title("⚙️ Settings")

    st.info("Settings and preferences will be available in future updates.")

    st.markdown("""
### Current Version

- Version: **1.0**
- AI Model: **Google Gemini**
- Frontend: **Streamlit**
- Backend: **FastAPI**
""")

# ------------------------------------
# Footer
# ------------------------------------
st.markdown("---")

st.markdown(
    """
<div style="text-align:center;">
    <h4>🚀 MT Career Launchpad</h4>
    <p>Helping Students, Graduates, and Professionals Build Successful Careers with AI.</p>
    <p><b>Developed by Hassan Peros | MIDDLE TECHNOLOGY</b></p>
</div>
""",
    unsafe_allow_html=True,
)
