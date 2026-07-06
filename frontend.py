import streamlit as st

# Page config
st.set_page_config(
    page_title="MT Career Launchpad",
    page_icon="🚀",
    layout="wide"
)

# Sidebar
st.sidebar.title("MT Career Launchpad")
menu = st.sidebar.selectbox(
    "Navigate",
    ["Home", "Career Assessment", "AI CV Builder", "Job Recommendations"]
)

# Home Page
if menu == "Home":
    st.title("🚀 Welcome to MT Career Launchpad")
    st.write("Your AI-powered platform for career growth, CV building, and job discovery.")
    
    st.image("https://via.placeholder.com/900x300", caption="Build. Learn. Launch.")

    st.info("Select a feature from the sidebar to begin.")

# Career Assessment
elif menu == "Career Assessment":
    st.header("🧠 Career Assessment")

    name = st.text_input("Enter your name")
    interest = st.text_area("What are your interests?")

    if st.button("Analyze"):
        st.success(f"Hi {name}, based on your interests we will generate career suggestions soon.")

# AI CV Builder
elif menu == "AI CV Builder":
    st.header("📄 AI CV Builder")

    full_name = st.text_input("Full Name")
    skills = st.text_area("List your skills")

    if st.button("Generate CV"):
        st.success("CV generated successfully (backend integration coming next).")

# Job Recommendations
elif menu == "Job Recommendations":
    st.header("💼 Job Recommendations")

    field = st.text_input("Enter your field (e.g. AI, Design, Engineering)")

    if st.button("Find Jobs"):
        st.info(f"Searching jobs for: {field}")
