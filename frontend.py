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
# Backend URL
# -------------------------------
BACKEND_URL = "http://backend:8000"

# -------------------------------
# Session State
# -------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

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

    if st.button("🗺️ Career Roadmap"):
        st.session_state.page = "Roadmap"

    if st.button("💼 Job Recommendations"):
        st.session_state.page = "Jobs"

    if st.button("📚 Learning Hub"):
        st.session_state.page = "Learning"

    if st.button("⚙️ Settings"):
        st.session_state.page = "Settings"

# -------------------------------
# Dashboard
# -------------------------------
if st.session_state.page == "Dashboard":

    st.title("🚀 MT Career Launchpad")

    st.markdown("""
    ## Welcome!

    MT Career Launchpad is your AI-powered career companion.

    ### Features
    - 🤖 AI Resume Analyzer
    - 🧠 Career Assessment
    - 📄 CV Builder
    - 🗺️ Career Roadmap
    - 💼 Job Recommendations
    - 📚 Learning Hub

    Use the sidebar to navigate through the application.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Resumes Reviewed", "150+")

    with col2:
        st.metric("Career Paths", "50+")
      with col3:
        st.metric("AI Accuracy", "95%")
# -------------------------------
# AI Resume Analyzer
# -------------------------------
elif st.session_state.page == "Resume":

    st.title("🤖 AI Resume Analyzer")

    st.write("Paste your resume below and receive AI-powered feedback.")

    resume = st.text_area(
        "Resume",
        height=300,
        placeholder="Paste your resume here..."
    )

    if st.button("Analyze Resume"):

        if resume.strip() == "":
            st.warning("Please paste your resume first.")

        else:
            try:
                response = requests.post(
                    f"{BACKEND_URL}/analyze",
                    json={"text": resume}
                )

                if response.status_code == 200:
                    st.success("Analysis Complete!")
                    result = response.json()
                    st.write(result["feedback"])

                else:
                    st.error("Unable to analyze your resume.")

            except Exception as e:
                st.error(f"Connection error: {e}")

# -------------------------------
# Career Assessment
# -------------------------------
elif st.session_state.page == "Assessment":

    st.title("🧠 Career Assessment")

    st.write("Answer the questions below.")

    interest = st.selectbox(
        "What interests you most?",
        [
            "Software Development",
            "UI/UX Design",
            "Data Science",
            "Artificial Intelligence",
            "Cybersecurity",
            "Digital Marketing"
        ]
    )

    skill = st.slider(
        "Rate your current skill level",
        1,
        10,
        5
    )

    if st.button("Generate Career Advice"):

        st.success("Recommended Career Path")

        st.markdown(f"""
### Suggested Path

**Interest:** {interest}

**Skill Level:** {skill}/10

### Next Steps

- Build practical projects.
- Improve your portfolio.
- Earn relevant certifications.
- Network with professionals.
- Apply for internships and entry-level roles.
""")

# -------------------------------
# CV Builder
# -------------------------------
elif st.session_state.page == "CV":

    st.title("📄 CV Builder")

    full_name = st.text_input("Full Name")

    email = st.text_input("Email")

    phone = st.text_input("Phone Number")

    summary = st.text_area("Professional Summary")

    experience = st.text_area("Work Experience")

    education = st.text_area("Education")

    skills = st.text_area("Skills")

    if st.button("Generate CV"):

        st.success("CV Generated Successfully!")

        st.markdown("---")

        st.markdown(f"# {full_name}")

        st.write(email)

        st.write(phone)

        st.markdown("## Professional Summary")
        st.write(summary)

        st.markdown("## Experience")
        st.write(experience)

        st.markdown("## Education")
        st.write(education)

        st.markdown("## Skills")
        st.write(skills)
      
    with col3:
        st.metric("AI Accuracy", "95%")
      # -------------------------------
# Career Roadmap
# -------------------------------
elif st.session_state.page == "Roadmap":

    st.title("🗺️ Career Roadmap")

    career = st.selectbox(
        "Choose your desired career",
        [
            "Software Engineer",
            "UI/UX Designer",
            "Data Scientist",
            "AI Engineer",
            "Cybersecurity Analyst",
            "Product Manager"
        ]
    )

    if st.button("Generate Roadmap"):

        st.success(f"Roadmap for {career}")

        st.markdown("""
### Step 1
- Learn the fundamentals.

### Step 2
- Take online courses.
- Build practical projects.

### Step 3
- Create a strong portfolio.

### Step 4
- Earn industry certifications.

### Step 5
- Apply for internships or junior roles.

### Step 6
- Continue learning and improving.
""")

# -------------------------------
# Job Recommendations
# -------------------------------
elif st.session_state.page == "Jobs":

    st.title("💼 Job Recommendations")

    role = st.selectbox(
        "Preferred Job Role",
        [
            "Software Engineer",
            "Frontend Developer",
            "Backend Developer",
            "Data Scientist",
            "UI/UX Designer",
            "AI Engineer"
        ]
    )

 location = st.text_input("Preferred Location")

    if st.button("Find Jobs"):

        st.success("Recommended Jobs")

        st.markdown(f"""
### {role}

📍 Location: {location}

Suggested platforms:

- LinkedIn Jobs
- Indeed
- Glassdoor
- Wellfound
- Google Careers

Customize your resume before applying for each opportunity.
""")

# -------------------------------
# Learning Hub
# -------------------------------
elif st.session_state.page == "Learning":

    st.title("📚 Learning Hub")

    st.markdown("""
### Recommended Learning Resources

#### Programming
- Python
- JavaScript
- SQL

#### Design
- Figma
- Adobe XD

#### Artificial Intelligence
- Machine Learning
- Deep Learning
- Prompt Engineering

#### Certifications
- Google
- Microsoft
- AWS
- IBM

#### Soft Skills
- Communication
- Leadership
- Teamwork
- Problem Solving
""")
# -------------------------------
# Settings
# -------------------------------
elif st.session_state.page == "Settings":

    st.title("⚙️ Settings")

    st.write("Customize your MT Career Launchpad experience.")

    theme = st.selectbox(
        "Theme",
        ["Light", "Dark"]
    )

    notifications = st.checkbox(
        "Enable Notifications",
        value=True
    )

    email_updates = st.checkbox(
        "Receive Career Tips by Email",
        value=True
    )

    if st.button("Save Settings"):
        st.success("Settings saved successfully!")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")

st.markdown(
    """
    <div style="text-align:center;">
        <h4>🚀 MT Career Launchpad</h4>
        <p>AI-Powered Career Development Platform</p>
        <p>Developed by <strong>MIDDLE TECHNOLOGY</strong></p>
        <p>© 2026 All Rights Reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)
