import streamlit as st
import requests

st.set_page_config(
    page_title="MT Graduate Career Launchpad",
    page_icon="🚀",
    layout="wide"
)

# Session state
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# Sidebar
with st.sidebar:
    st.title("🚀 MT Career Launchpad")
    st.caption("Launch Your Career With AI")

    pages = [
        "Dashboard",
        "AI Resume Analyzer",
        "Career Assessment",
        "CV Builder",
        "Career Roadmap",
        "Job Recommendations",
        "Learning Hub",
        "Settings",
    ]

    for page in pages:
        if st.button(page, use_container_width=True):
            st.session_state.page = page

    st.divider()
    st.success("🟢 System Online")

page = st.session_state.page

if page == "Dashboard":
    st.title("🚀 MT Graduate Career Launchpad")
    st.subheader("Welcome!")
    st.write("This is your AI-powered career development platform.")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Employability Score", "82%")
    col2.metric("ATS Match", "88%")
    col3.metric("Career Progress", "15%")
    col4.metric("AI Analyses", "0")

elif page == "AI Resume Analyzer":
    st.title("🤖 AI Resume Analyzer")

    resume = st.text_area(
        "Paste your resume below:",
        height=250
    )

    if st.button("Analyze with AI"):

        if resume.strip():

            with st.spinner("Analyzing..."):

                try:
                    response = requests.post(
                        "http://backend:8000/analyze",
                        json={"text": resume},
                        timeout=120
                    )

                    if response.status_code == 200:
                        result = response.json()
                        st.success("Analysis Complete")
                        st.markdown(result["feedback"])
                    else:
                        st.error("Backend returned an error.")

                except Exception as e:
                    st.error(f"Connection Error: {e}")

        else:
            st.warning("Please paste your resume first.")

elif page == "Career Assessment":
    st.title("🧠 Career Assessment")
    st.info("Coming soon...")

elif page == "CV Builder":
    st.title("📄 CV Builder")
    st.info("Coming soon...")

elif page == "Career Roadmap":
    st.title("🛣️ Career Roadmap")
    st.info("Coming soon...")

elif page == "Job Recommendations":
    st.title("💼 Job Recommendations")
    st.info("Coming soon...")

elif page == "Learning Hub":
    st.title("📚 Learning Hub")
    st.info("Coming soon...")

elif page == "Settings":
    st.title("⚙️ Settings")
    st.write("Version 2.0")
    st.success("Backend Connected")
