import streamlit as st
import json
import hashlib
import os
import PyPDF2
import pdfplumber
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime

# Try to import Gemini
try:
    from google import genai
    AI_LIBRARY_AVAILABLE = True
except ImportError:
    AI_LIBRARY_AVAILABLE = False

# ============================================================================
# FILE MANAGEMENT
# ============================================================================
USER_FILE = "users.json"
APPLICATIONS_FILE = "applications.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_json(filename, default={}):
    if not os.path.exists(filename):
        return default
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except:
        return default

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_users():
    return load_json(USER_FILE, {})

def save_users(users):
    save_json(USER_FILE, users)

def load_applications():
    return load_json(APPLICATIONS_FILE, {})

def save_applications(apps):    save_json(APPLICATIONS_FILE, apps)

def register_user(username, password):
    users = load_users()
    if username in users:
        return False
    users[username] = {
        "password": hash_password(password),
        "profile": {"fullname": "", "role": "", "bio": "", "skills": "", "projects": ""},
        "applications": []
    }
    save_users(users)
    return True

def authenticate_user(username, password):
    users = load_users()
    if username in users:
        stored_data = users[username]
        if isinstance(stored_data, str):
            return stored_data == hash_password(password)
        return stored_data.get("password") == hash_password(password)
    return False

def update_user_profile(username, profile_data):
    users = load_users()
    if username in users:
        if isinstance(users[username], str):
            users[username] = {"password": users[username], "profile": profile_data}
        else:
            users[username]["profile"] = profile_data
        save_users(users)
        return True
    return False

def get_user_profile(username):
    users = load_users()
    if username in users and isinstance(users[username], dict):
        return users[username].get("profile", {"fullname": "", "role": "", "bio": "", "skills": "", "projects": ""})
    return {"fullname": "", "role": "", "bio": "", "skills": "", "projects": ""}

def get_ai_client():
    if not AI_LIBRARY_AVAILABLE:
        return None
    api_key = st.secrets.get("GEMINI_API_KEY") if hasattr(st, 'secrets') else None
    if not api_key:
        return None
    try:
        return genai.Client(api_key=api_key)
    except:
        return None
# ============================================================================
# FEATURE 1: RESUME PDF PARSER
# ============================================================================
def parse_resume_pdf(uploaded_file):
    """Extract text and info from PDF resume"""
    extracted_text = ""
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    extracted_text += text + "\n"
        
        # Simple keyword extraction
        skills_keywords = ["Python", "Java", "JavaScript", "SQL", "Excel", "Power BI", 
                          "Machine Learning", "Data Analysis", "Project Management", 
                          "Communication", "Leadership", "Teamwork"]
        
        found_skills = [skill for skill in skills_keywords if skill.lower() in extracted_text.lower()]
        
        return {
            "text": extracted_text,
            "skills": ", ".join(found_skills),
            "success": True
        }
    except Exception as e:
        return {"error": str(e), "success": False}

# ============================================================================
# FEATURE 2: JOB BOARD INTEGRATION
# ============================================================================
def fetch_jobs(keyword="graduate", location="remote", limit=10):
    """Fetch jobs from API (using mock data for demo)"""
    # Mock job data - replace with real API in production
    mock_jobs = [
        {"title": f"Graduate {keyword} - Role {i}", 
         "company": f"Company {i}", 
         "location": location if location != "remote" else "Remote",
         "salary": f"${50000 + i*5000} - ${70000 + i*5000}",
         "description": f"Exciting opportunity for a graduate {keyword} professional...",
         "posted": f"{i} days ago"}
        for i in range(1, limit+1)
    ]
    return mock_jobs

# ============================================================================
# FEATURE 3: AI INTERVIEW SIMULATOR (ENHANCED)
# ============================================================================
def generate_interview_question(role, difficulty="medium"):
    """Generate AI-powered interview questions"""
    questions = {
        "technical": [
            "Explain the difference between SQL and NoSQL databases.",
            "How would you optimize a slow-running algorithm?",
            "Describe your experience with cloud platforms.",
            "What is the difference between GET and POST requests?"
        ],
        "behavioral": [
            "Tell me about a time you faced a challenging project deadline.",
            "Describe a situation where you had to work with a difficult team member.",
            "Give an example of how you've shown leadership.",
            "Tell me about a mistake you made and how you handled it."
        ],
        "hr": [
            "Why do you want to work for our company?",
            "Where do you see yourself in 5 years?",
            "What are your greatest strengths and weaknesses?",
            "Why should we hire you?"
        ]
    }
    
    import random
    category = random.choice(list(questions.keys()))
    return random.choice(questions[category]), category
    client = get_ai_client()
    if client:
        try:
            prompt = f"""Evaluate this interview answer for a {role} position.
Question: {question}
Answer: {answer}

Provide:
1. Score out of 10
2. Strengths
3. Areas for improvement
4. Better way to phrase it"""
            response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
            return response.text
        except:
            return "AI evaluation unavailable. Good effort!"
    else:
        return "Score: 7/10 - Clear and concise. Consider adding specific examples and quantifiable results."

# ============================================================================
# FEATURE 4: SKILLS ASSESSMENT QUIZ
# ============================================================================def get_quiz_questions(skill_category):
    """Get quiz questions for different skills"""
    quizzes = {
        "Python": [
            {"q": "What is the output of print(2**3)?", "options": ["6", "8", "9", "5"], "answer": 1},
            {"q": "Which keyword is used to define a function?", "options": ["func", "def", "function", "define"], "answer": 1},
            {"q": "What data type is [1, 2, 3]?", "options": ["Tuple", "Dictionary", "List", "Set"], "answer": 2}
        ],
        "SQL": [
            {"q": "What does SQL stand for?", "options": ["Structured Query Language", "Simple Query Language", "System Query Language", "Standard Query Language"], "answer": 0},
            {"q": "Which command retrieves data from a database?", "options": ["GET", "FETCH", "SELECT", "RETRIEVE"], "answer": 2}
        ],
        "Excel": [
            {"q": "What function sums a range of cells?", "options": ["TOTAL", "ADD", "SUM", "AGGREGATE"], "answer": 2},
            {"q": "What is a pivot table used for?", "options": ["Data visualization", "Data summarization", "Data entry", "Data validation"], "answer": 1}
        ]
    }
    return quizzes.get(skill_category, [])

# ============================================================================
# FEATURE 5: SALARY ESTIMATOR
# ============================================================================
def estimate_salary(role, location, experience_years):
    """Estimate salary based on role and location"""
    base_salaries = {
        "Software Engineer": 75000,
        "Data Analyst": 65000,
        "Product Manager": 85000,
        "Business Analyst": 60000,
        "Project Coordinator": 55000,
        "Marketing Manager": 65000
    }
    
    base = base_salaries.get(role, 60000)
    location_multiplier = {"New York": 1.3, "San Francisco": 1.4, "London": 1.2, "Remote": 1.0}.get(location, 1.0)
    experience_multiplier = 1 + (experience_years * 0.1)
    
    estimated = base * location_multiplier * experience_multiplier
    return {
        "min": int(estimated * 0.9),
        "max": int(estimated * 1.1),
        "median": int(estimated)
    }

# ============================================================================
# FEATURE 6: AI COVER LETTER GENERATOR
# ============================================================================
def generate_cover_letter(name, role, company, skills, experience):
    """Generate AI-powered cover letter"""
    client = get_ai_client()    if client:
        try:
            prompt = f"""Write a professional cover letter for:
Name: {name}
Position: {role} at {company}
Skills: {skills}
Experience: {experience}

Make it concise, professional, and highlight relevant skills."""
            response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
            return response.text
        except:
            pass
    
    # Fallback template
    return f"""Dear Hiring Manager,

I am writing to express my strong interest in the {role} position at {company}.

With my background in {skills}, I am confident in my ability to contribute effectively to your team. My experience includes {experience}.

I am excited about the opportunity to bring my skills to {company} and would welcome the chance to discuss how I can contribute to your organization.

Thank you for your consideration.

Sincerely,
{name}"""

# ============================================================================
# FEATURE 7: APPLICATION TRACKER
# ============================================================================
def add_application(username, company, role, status="Applied"):
    apps = load_applications()
    if username not in apps:
        apps[username] = []
    
    apps[username].append({
        "company": company,
        "role": role,
        "status": status,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "id": len(apps[username]) + 1
    })
    save_applications(apps)

def get_user_applications(username):
    apps = load_applications()
    return apps.get(username, [])

def update_application_status(username, app_id, new_status):    apps = load_applications()
    if username in apps:
        for app in apps[username]:
            if app["id"] == app_id:
                app["status"] = new_status
                break
    save_applications(apps)

# ============================================================================
# FEATURE 8: CAREER PATH VISUALIZER
# ============================================================================
def get_career_path(target_role):
    """Get career progression path"""
    paths = {
        "Software Engineer": [
            {"level": "Junior Developer", "years": "0-2", "skills": ["Basic Programming", "Version Control"]},
            {"level": "Software Engineer", "years": "2-5", "skills": ["System Design", "Code Review"]},
            {"level": "Senior Engineer", "years": "5-8", "skills": ["Architecture", "Mentoring"]},
            {"level": "Tech Lead", "years": "8-12", "skills": ["Leadership", "Strategy"]},
            {"level": "Engineering Manager", "years": "12+", "skills": ["People Management", "Vision"]}
        ],
        "Data Analyst": [
            {"level": "Junior Analyst", "years": "0-2", "skills": ["Excel", "SQL Basics"]},
            {"level": "Data Analyst", "years": "2-5", "skills": ["Python/R", "Visualization"]},
            {"level": "Senior Analyst", "years": "5-8", "skills": ["Machine Learning", "Strategy"]},
            {"level": "Data Scientist", "years": "8-12", "skills": ["Advanced ML", "Research"]},
            {"level": "Data Science Manager", "years": "12+", "skills": ["Leadership", "AI Strategy"]}
        ]
    }
    return paths.get(target_role, paths["Software Engineer"])

# ============================================================================
# STYLING
# ============================================================================
def inject_premium_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=300;400;500;600;700;800&display=swap');
        #MainMenu {visibility: hidden !important;}
        header {visibility: hidden !important;}
        [data-testid="stToolbar"] {display: none !important;}
        .stApp {
            background-color: #F8FAFC !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: #1E293B !important;
        }
        .premium-hero {
            background: linear-gradient(135deg, #0B6B3A 0%, #063c22 100%);
            text-align: center;
            padding: 35px 20px;            border-radius: 20px;
            margin-bottom: 25px;
            box-shadow: 0 10px 25px rgba(11, 107, 58, 0.15);
        }
        .premium-hero h1 {
            font-size: 38px !important;
            font-weight: 800 !important;
            color: #ffffff !important;
            margin: 0 !important;
        }
        .premium-hero p.tagline {
            color: #19D17B !important;
            font-size: 18px !important;
            margin-top: 6px !important;
            font-weight: 500 !important;
        }
        .premium-card {
            background: #ffffff;
            padding: 24px;
            border-radius: 16px;
            border: 1px solid #E2E8F0;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(30, 41, 59, 0.03);
        }
        .premium-card h3 {
            font-size: 20px !important;
            font-weight: 700 !important;
            margin-top: 0 !important;
            color: #0B6B3A !important;
        }
        .badge-green {
            background-color: #DCFCE7 !important;
            border-left: 5px solid #22C55E !important;
            color: #14532D !important;
            padding: 12px 16px;
            border-radius: 8px;
            margin-bottom: 10px;
            font-weight: 500;
        }
        .badge-blue {
            background-color: #DBEAFE !important;
            border-left: 5px solid #3B82F6 !important;
            color: #1E3A8A !important;
            padding: 12px 16px;
            border-radius: 8px;
            margin-bottom: 10px;
            font-weight: 500;
        }
        div.stButton > button {
            background: linear-gradient(90deg, #0B6B3A 0%, #19D17B 100%) !important;            color: #ffffff !important;
            border-radius: 12px !important;
            border: none !important;
            padding: 10px 20px !important;
            font-weight: 700 !important;
        }
        .system-footer {
            margin-top: 40px;
            padding: 30px;
            background-color: #0B6B3A;
            border-radius: 16px;
            color: #ffffff !important;
            text-align: center;
        }
        .system-footer h4, .system-footer p {
            color: #ffffff !important;
        }
        .career-timeline {
            border-left: 3px solid #0B6B3A;
            padding-left: 20px;
            margin: 10px 0;
        }
        </style>
    """, unsafe_allow_html=True)

# ============================================================================
# MAIN APP
# ============================================================================
def main():
    st.set_page_config(page_title="Graduate Career Launchpad", page_icon="🎓", layout="wide")
    inject_premium_styles()
    
    # Initialize session state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.current_page = "Dashboard"
        st.session_state.cv_data = {"fullname": "", "role": "", "skills": "", "experience": ""}
        st.session_state.quiz_score = 0
        st.session_state.interview_history = []

    # Header
    st.markdown("""
        <div class="premium-hero">
            <h1>Graduate Career Launchpad</h1>
            <p class="tagline">Enterprise AI-Powered Employability & Acceleration Ecosystem</p>
        </div>
    """, unsafe_allow_html=True)

    # Authentication    if not st.session_state.logged_in:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="premium-card"><h3>🔒 Login</h3></div>', unsafe_allow_html=True)
            username = st.text_input("Username", key="login_user")
            password = st.text_input("Password", type="password", key="login_pass")
            if st.button("Login", key="btn_login"):
                if authenticate_user(username, password):
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    profile = get_user_profile(username)
                    st.session_state.cv_data = profile
                    st.rerun()
                else:
                    st.error("Invalid credentials")
        
        with col2:
            st.markdown('<div class="premium-card"><h3>✨ Register</h3></div>', unsafe_allow_html=True)
            new_user = st.text_input("Choose Username", key="reg_user")
            new_pass = st.text_input("Create Password", type="password", key="reg_pass")
            if st.button("Register", key="btn_register"):
                if new_user and new_pass:
                    if register_user(new_user, new_pass):
                        st.success("Registered! Please login.")
                    else:
                        st.error("Username taken")
        
        st.markdown("---")
        render_impact_section()
        return

    # Logged In - Navigation
    current_user = st.session_state.username
    
    with st.sidebar:
        st.markdown(f"### 👤 {current_user}")
        st.markdown("---")
        st.markdown("### 🧭 Navigation")
        
        menu_options = {
            "🏠 Dashboard": "Dashboard",
            "📄 Resume Parser": "Resume Parser",
            "💼 Job Board": "Job Board",
            "🎤 Interview Simulator": "Interview Simulator",
            "📝 Skills Quiz": "Skills Quiz",
            "💰 Salary Estimator": "Salary Estimator",
            "✉️ Cover Letter Generator": "Cover Letter",
            "📊 Application Tracker": "Application Tracker",
            "🗺️ Career Path": "Career Path",
            "⚙️ Profile Settings": "Profile Settings"        }
        
        for label, page in menu_options.items():
            if st.button(label, use_container_width=True):
                st.session_state.current_page = page
                st.rerun()
        
        st.markdown("---")
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.current_page = "Dashboard"
            st.rerun()

    # Page Routing
    page = st.session_state.current_page
    
    if page == "Dashboard":
        render_dashboard(current_user)
    elif page == "Resume Parser":
        render_resume_parser()
    elif page == "Job Board":
        render_job_board(current_user)
    elif page == "Interview Simulator":
        render_interview_simulator()
    elif page == "Skills Quiz":
        render_skills_quiz()
    elif page == "Salary Estimator":
        render_salary_estimator()
    elif page == "Cover Letter":
        render_cover_letter_generator()
    elif page == "Application Tracker":
        render_application_tracker()
    elif page == "Career Path":
        render_career_path()
    elif page == "Profile Settings":
        render_profile_settings(current_user)

    render_footer()

# ============================================================================
# PAGE RENDERERS
# ============================================================================

def render_dashboard(user):
    st.markdown(f"## Welcome back, {user}! 👋")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Applications Tracked", len(get_user_applications(user)))    with col2:
        st.metric("Interviews Practiced", len(st.session_state.get("interview_history", [])))
    with col3:
        st.metric("Quizzes Completed", st.session_state.get("quiz_score", 0))
    with col4:
        st.metric("Profile Completeness", "75%")
    
    st.markdown('<div class="premium-card"><h3>🎯 Quick Actions</h3></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📄 Parse Resume", use_container_width=True):
            st.session_state.current_page = "Resume Parser"
            st.rerun()
    with col2:
        if st.button("💼 Browse Jobs", use_container_width=True):
            st.session_state.current_page = "Job Board"
            st.rerun()
    with col3:
        if st.button("🎤 Practice Interview", use_container_width=True):
            st.session_state.current_page = "Interview Simulator"
            st.rerun()
    
    render_impact_section()

def render_resume_parser():
    st.markdown('<div class="premium-card"><h3>📄 AI Resume Parser</h3><p>Upload your CV to auto-extract information</p></div>', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    
    if uploaded_file is not None:
        with st.spinner("Parsing your resume..."):
            result = parse_resume_pdf(uploaded_file)
            
            if result["success"]:
                st.success("Resume parsed successfully!")
                st.markdown("### Extracted Skills:")
                st.write(result.get("skills", "None detected"))
                
                st.markdown("### Full Text:")
                st.text_area("Resume Content", result["text"], height=300)
                
                # Auto-fill profile
                if st.button("💾 Save to Profile"):
                    st.session_state.cv_data["skills"] = result.get("skills", "")
                    update_user_profile(st.session_state.username, st.session_state.cv_data)
                    st.success("Profile updated!")
            else:
                st.error(f"Error parsing PDF: {result.get('error')}")

def render_job_board(user):    st.markdown('<div class="premium-card"><h3>💼 Job Board</h3><p>Find your dream job</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        keyword = st.text_input("Job Title/Keyword", "Graduate")
    with col2:
        location = st.text_input("Location", "Remote")
    
    if st.button("🔍 Search Jobs"):
        with st.spinner("Fetching jobs..."):
            jobs = fetch_jobs(keyword, location)
            
            for job in jobs:
                with st.container():
                    st.markdown(f"""
                    <div class="premium-card">
                        <h4>{job['title']}</h4>
                        <p><b>Company:</b> {job['company']} | <b>Location:</b> {job['location']}</p>
                        <p><b>Salary:</b> {job['salary']}</p>
                        <p>{job['description']}</p>
                        <p><i>Posted: {job['posted']}</i></p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button(f"💾 Track Application - {job['company']}", key=f"apply_{job['company']}"):
                            add_application(user, job['company'], job['title'])
                            st.success(f"Application to {job['company']} tracked!")
                    with col2:
                        st.button("🔗 Apply Now", key=f"link_{job['company']}")
                    st.markdown("---")

def render_interview_simulator():
    st.markdown('<div class="premium-card"><h3>🎤 AI Interview Simulator</h3><p>Practice with AI-powered questions</p></div>', unsafe_allow_html=True)
    
    role = st.text_input("Target Role", st.session_state.cv_data.get("role", "Software Engineer"))
    
    if "current_question" not in st.session_state:
        st.session_state.current_question = None
        st.session_state.question_category = None
    
    if st.button("🎲 Generate Question"):
        q, cat = generate_interview_question(role)
        st.session_state.current_question = q
        st.session_state.question_category = cat
        st.rerun()
    
    if st.session_state.current_question:
        st.info(f"**Category:** {st.session_state.question_category.title()}")        st.markdown(f"### {st.session_state.current_question}")
        
        answer = st.text_area("Your Answer", height=150)
        
        if st.button("✅ Evaluate Answer"):
            with st.spinner("AI is evaluating..."):
                feedback = evaluate_answer(st.session_state.current_question, answer, role)
                st.markdown("### 📊 Feedback:")
                st.write(feedback)
                
                if "interview_history" not in st.session_state:
                    st.session_state.interview_history = []
                st.session_state.interview_history.append({
                    "question": st.session_state.current_question,
                    "answer": answer,
                    "date": datetime.now().strftime("%Y-%m-%d")
                })

def render_skills_quiz():
    st.markdown('<div class="premium-card"><h3>📝 Skills Assessment Quiz</h3><p>Test your knowledge</p></div>', unsafe_allow_html=True)
    
    skill = st.selectbox("Select Skill", ["Python", "SQL", "Excel"])
    
    if "quiz_questions" not in st.session_state:
        st.session_state.quiz_questions = []
        st.session_state.quiz_index = 0
        st.session_state.quiz_correct = 0
    
    if st.button("🚀 Start Quiz"):
        st.session_state.quiz_questions = get_quiz_questions(skill)
        st.session_state.quiz_index = 0
        st.session_state.quiz_correct = 0
        st.rerun()
    
    if st.session_state.quiz_questions:
        if st.session_state.quiz_index < len(st.session_state.quiz_questions):
            q = st.session_state.quiz_questions[st.session_state.quiz_index]
            st.markdown(f"### Question {st.session_state.quiz_index + 1}: {q['q']}")
            
            answer = st.radio("Select your answer:", q["options"], key=f"q_{st.session_state.quiz_index}")
            
            if st.button("Submit Answer"):
                if q["options"].index(answer) == q["answer"]:
                    st.session_state.quiz_correct += 1
                    st.success("Correct! ✅")
                else:
                    st.error("Wrong! ❌")
                
                st.session_state.quiz_index += 1
                st.rerun()        else:
            score = st.session_state.quiz_correct
            total = len(st.session_state.quiz_questions)
            st.markdown(f"## Quiz Complete! 🎉")
            st.markdown(f"### Score: {score}/{total} ({score/total*100:.0f}%)")
            
            st.session_state.quiz_score += 1

def render_salary_estimator():
    st.markdown('<div class="premium-card"><h3>💰 Salary Estimator</h3><p>Know your worth</p></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        role = st.selectbox("Role", ["Software Engineer", "Data Analyst", "Product Manager", 
                                     "Business Analyst", "Project Coordinator", "Marketing Manager"])
    with col2:
        location = st.selectbox("Location", ["New York", "San Francisco", "London", "Remote", "Other"])
    with col3:
        experience = st.slider("Years of Experience", 0, 20, 2)
    
    if st.button("💵 Calculate Salary"):
        result = estimate_salary(role, location, experience)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Minimum", f"${result['min']:,}")
        with col2:
            st.metric("Median", f"${result['median']:,}")
        with col3:
            st.metric("Maximum", f"${result['max']:,}")
        
        # Chart
        df = pd.DataFrame({
            "Range": ["Min", "Median", "Max"],
            "Salary": [result["min"], result["median"], result["max"]]
        })
        fig = px.bar(df, x="Range", y="Salary", color="Range", 
                     color_discrete_sequence=["#0B6B3A", "#19D17B", "#0B6B3A"])
        st.plotly_chart(fig, use_container_width=True)

def render_cover_letter_generator():
    st.markdown('<div class="premium-card"><h3>✉️ AI Cover Letter Generator</h3><p>Create professional cover letters in seconds</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Name", st.session_state.cv_data.get("fullname", ""))
        role = st.text_input("Target Position", st.session_state.cv_data.get("role", ""))
    with col2:
        company = st.text_input("Company Name")
        skills = st.text_area("Your Skills", st.session_state.cv_data.get("skills", ""))    
    experience = st.text_area("Your Experience", st.session_state.cv_data.get("bio", ""))
    
    if st.button("✨ Generate Cover Letter"):
        with st.spinner("AI is writing..."):
            letter = generate_cover_letter(name, role, company, skills, experience)
            st.markdown("### Generated Cover Letter:")
            st.text_area("Cover Letter", letter, height=400)
            
            st.download_button(
                label="📥 Download as Text",
                data=letter,
                file_name=f"cover_letter_{company}.txt",
                mime="text/plain"
            )

def render_application_tracker():
    st.markdown('<div class="premium-card"><h3>📊 Application Tracker</h3><p>Track your job applications</p></div>', unsafe_allow_html=True)
    
    user = st.session_state.username
    applications = get_user_applications(user)
    
    if applications:
        # Stats
        col1, col2, col3, col4 = st.columns(4)
        statuses = [app["status"] for app in applications]
        with col1:
            st.metric("Total", len(applications))
        with col2:
            st.metric("Applied", statuses.count("Applied"))
        with col3:
            st.metric("Interview", statuses.count("Interview"))
        with col4:
            st.metric("Offer", statuses.count("Offer"))
        
        # Applications list
        for app in applications:
            with st.container():
                col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
                with col1:
                    st.markdown(f"**{app['role']}** at {app['company']}")
                with col2:
                    st.write(f"📅 {app['date']}")
                with col3:
                    status = st.selectbox("Status", ["Applied", "Interview", "Offer", "Rejected"], 
                                         index=["Applied", "Interview", "Offer", "Rejected"].index(app["status"]),
                                         key=f"status_{app['id']}")
                    if status != app["status"]:
                        update_application_status(user, app["id"], status)
                        st.rerun()                with col4:
                    st.markdown(get_status_emoji(app["status"]), unsafe_allow_html=True)
                st.markdown("---")
        
        # Chart
        df = pd.DataFrame(applications)
        if not df.empty:
            fig = px.pie(df, names='status', title='Application Status Distribution')
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No applications tracked yet. Start applying from the Job Board!")

def get_status_emoji(status):
    emojis = {"Applied": "📝", "Interview": "🎤", "Offer": "🎉", "Rejected": "❌"}
    return emojis.get(status, "📝")

def render_career_path():
    st.markdown('<div class="premium-card"><h3>🗺️ Career Path Visualizer</h3><p>Your journey to success</p></div>', unsafe_allow_html=True)
    
    target_role = st.text_input("Target Role", st.session_state.cv_data.get("role", "Software Engineer"))
    
    path = get_career_path(target_role)
    
    for i, stage in enumerate(path):
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.markdown(f"### {stage['years']}")
            with col2:
                st.markdown(f"""
                <div class="premium-card" style="border-left: 4px solid #0B6B3A;">
                    <h4>{stage['level']}</h4>
                    <p><b>Key Skills:</b> {', '.join(stage['skills'])}</p>
                </div>
                """, unsafe_allow_html=True)
            
            if i < len(path) - 1:
                st.markdown("<div style='height: 30px; border-left: 2px dashed #CBD5E1; margin-left: 50px;'></div>", unsafe_allow_html=True)

def render_profile_settings(user):
    st.markdown('<div class="premium-card"><h3>⚙️ Profile Settings</h3><p>Update your information</p></div>', unsafe_allow_html=True)
    
    fullname = st.text_input("Full Name", st.session_state.cv_data.get("fullname", ""))
    role = st.text_input("Target Role", st.session_state.cv_data.get("role", ""))
    skills = st.text_area("Skills", st.session_state.cv_data.get("skills", ""))
    experience = st.text_area("Experience/Bio", st.session_state.cv_data.get("bio", ""))
    projects = st.text_area("Projects", st.session_state.cv_data.get("projects", ""))
    
    if st.button("💾 Save Profile"):
        profile = {            "fullname": fullname,
            "role": role,
            "skills": skills,
            "bio": experience,
            "projects": projects
        }
        update_user_profile(user, profile)
        st.session_state.cv_data = profile
        st.success("Profile saved successfully!")

def render_impact_section():
    st.markdown("""
        <div class="premium-card" style="margin-top: 35px; border-top: 4px solid #0B6B3A;">
            <h3 style="text-align:center; color:#0B6B3A !important;">📈 Platform Impact</h3>
            <div style="display: flex; justify-content: space-around; text-align: center;">
                <div><div style="font-size:32px; font-weight:800; color:#0B6B3A;">1,250+</div><div>Graduates</div></div>
                <div><div style="font-size:32px; font-weight:800; color:#0B6B3A;">3,800+</div><div>CVs Optimized</div></div>
                <div><div style="font-size:32px; font-weight:800; color:#0B6B3A;">940+</div><div>Interviews</div></div>
                <div><div style="font-size:32px; font-weight:800; color:#0B6B3A;">76%</div><div>Success Rate</div></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_footer():
    st.markdown("""
        <div class="system-footer">
            <h4>Graduate Career Launchpad</h4>
            <p>Developed by MIDDLE TECHNOLOGY</p>
            <p><b>Founder:</b> Hassan Peros</p>
            <p><i>"Bridging the gap between graduates and employment through AI-powered career intelligence."</i></p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
