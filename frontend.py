import streamlit as st
import requests

st.set_page_config(
    page_title="MT Career Launchpad",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "username" not in st.session_state:
    st.session_state.username = "Guest"
    with st.sidebar:
    st.image("https://img.icons8.com/color/96/graduation-cap.png", width=80)

    st.title("MT Career Launchpad")

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

    st.markdown("---")
    st.caption("Powered by MIDDLE TECHNOLOGY")
    if st.session_state.page == "Dashboard":

    st.title("🚀 MT Career Launchpad")

    st.success("Welcome back! Ready to accelerate your career today?")

    st.markdown("---")
        col1, col2, col3, col4 = st.columns(4)

    col1.metric("Resume Score", "82%")
    col2.metric("ATS Match", "89%")
    col3.metric("Courses", "12")
    col4.metric("Career Level", "Graduate")

    st.markdown("---")
    c1, c2 = st.columns(2)

    with c1:
        st.info("""
### 📄 Resume Analyzer

Upload or paste your resume.

Receive AI-powered suggestions for improving:

- ATS Compatibility
- Grammar
- Keywords
- Professional Summary
- Skills
""")

    with c2:
        st.info("""
### 💼 Career Recommendations

Discover:

- Suitable Career Paths

- High-demand Skills

- Learning Resources

- Job Opportunities
""")
     elif st.session_state.page == "Resume":

    st.title("🤖 AI Resume Analyzer")

    st.write("Paste your resume below and receive AI-powered feedback.")

    resume = st.text_area("Resume", height=300)

    if st.button("Analyze Resume"):

        if resume.strip() == "":
            st.warning("Please paste your resume first.")

        else:
            with st.spinner("Analyzing with Gemini AI..."):

                try:
                    response = requests.post(
                        "http://backend:8000/analyze",
                        json={"text": resume}
                    )

                    if response.status_code == 200:
                        st.success("Analysis Complete!")
                        st.write(response.json()["feedback"])
                    else:
                        st.error("Backend returned an error.")

                except Exception as e:
                    st.error(f"Cannot connect to backend: {e}")
elif st.session_state.page == "Assessment":

    st.title("🧠 Career Assessment")

    st.write("Evaluate your strengths and discover suitable career paths.")

    communication = st.slider("Communication Skills", 1, 10, 5)
    leadership = st.slider("Leadership", 1, 10, 5)
    technical = st.slider("Technical Skills", 1, 10, 5)

    if st.button("Generate Assessment"):

        score = communication + leadership + technical

        st.success(f"Your Assessment Score: {score}/30")

        if score >= 24:
            st.info("Excellent! You are highly employable.")

        elif score >= 18:
            st.info("Good potential. Continue improving your skills.")

        else:
            st.warning("Focus on improving your skills through continuous learning.")
            elif st.session_state.page == "CV":

    st.title("📄 CV Builder & Optimizer")

    st.text_input("Full Name")

    st.text_input("Email")

    st.text_input("Phone")

    st.text_area("Professional Summary")

    st.text_area("Skills")

    st.text_area("Experience")

    st.text_area("Education")

    if st.button("Generate CV"):

        st.success("CV Generated Successfully!")

        st.info("PDF export will be added in the next version.")
        elif st.session_state.page == "Roadmap":

    st.title("🗺 Career Roadmap")

    st.markdown("""
### Suggested Career Journey

✅ Build your Resume

⬇️

✅ Improve ATS Score

⬇️

✅ Learn High Demand Skills

⬇️

✅ Apply for Jobs

⬇️

✅ Prepare for Interviews

⬇️

🎉 Get Hired
""")
elif st.session_state.page == "Jobs":

    st.title("💼 Job Recommendations")

    st.write("Recommended Positions")

    st.write("• Software Developer")

    st.write("• UI/UX Designer")

    st.write("• Data Analyst")

    st.write("• AI Engineer")

    st.write("• Product Designer")

elif st.session_state.page == "Learning":

    st.title("📚 Learning Hub")

    st.write("Recommended Learning Platforms")

    st.write("• Coursera")

    st.write("• Udemy")

    st.write("• ALX")

    st.write("• freeCodeCamp")

    st.write("• Google Career Certificates")

elif st.session_state.page == "Settings":

    st.title("⚙ Settings")

    st.text_input("Display Name")

    st.selectbox(
        "Theme",
        ["Light", "Dark"]
    )

    st.button("Save Settings")
