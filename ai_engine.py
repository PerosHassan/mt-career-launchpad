import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found. Please add it to your .env file.")

MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash-lite")

# ============================================================
# INITIALIZE GEMINI CLIENT
# ============================================================
client = genai.Client(api_key=API_KEY)

# ============================================================
# TASK CONSTANTS
# ============================================================
TASK_RESUME = "resume"
TASK_CAREER = "career"
TASK_CV = "cv"
TASK_ROADMAP = "roadmap"
TASK_INTERVIEW = "interview"

# ============================================================
# SYSTEM PROMPT
# ============================================================
SYSTEM_PROMPT = """
You are MT Career Launchpad AI, an intelligent career development assistant.

Your responsibilities include:
- Resume Analysis
- ATS Resume Optimization
- Career Assessment
- CV Writing
- Career Roadmaps
- Interview Preparation
- Skill Gap Analysis
- Learning Recommendations
- Certification Recommendations

Always:
- Think carefully before responding.
- Provide accurate and professional advice.
- Use clear headings.
- Use bullet points where appropriate.
- Explain your reasoning.
- Give practical next steps.
- Never fabricate information.
- If you are uncertain, state your limitations honestly.
"""

# ============================================================
# PROMPT TEMPLATES
# ============================================================
def resume_prompt(user_input: str) -> str:
    return f"""You are an ATS Resume Expert. Analyze the following resume and provide:
    1. ATS Score (out of 100)
    2. Strengths
    3. Weaknesses
    4. Missing Skills
    5. Recommendations for Improvement
    6. Final Summary
    Resume: {user_input}"""

def career_prompt(user_input: str) -> str:
    return f"""You are a Senior Career Advisor. Based on the user's profile, provide:
    1. Suitable Career Paths
    2. Skills to Develop
    3. Recommended Certifications
    4. Job Opportunities
    5. One-Year Career Development Plan
    User Information: {user_input}"""

def cv_prompt(user_input: str) -> str:
    return f"""You are an expert CV Writer. Create a professional ATS-friendly CV using the information below.
    Include: Professional Summary, Skills, Education, Experience, Projects, Certifications, Achievements.
    Information: {user_input}"""

def roadmap_prompt(user_input: str) -> str:
    return f"""You are a Career Mentor. Create a detailed 12-month learning roadmap.
    Career Goal: {user_input}
    Include: Beginner Skills, Intermediate Skills, Advanced Skills, Recommended Courses, Certifications, Portfolio Projects, Timeline, Career Opportunities."""

def interview_prompt(user_input: str) -> str:
    return f"""You are an Interview Coach. Prepare the user for interviews.
    Provide: Common Interview Questions, Sample Answers, Interview Tips, Mistakes to Avoid.
    Target Role: {user_input}"""

# ============================================================
# PROMPT ROUTER
# ============================================================
def build_prompt(task: str, user_input: str) -> str:
    tasks = {
        TASK_RESUME: resume_prompt,
        TASK_CAREER: career_prompt,
        TASK_CV: cv_prompt,
        TASK_ROADMAP: roadmap_prompt,
        TASK_INTERVIEW: interview_prompt
    }
    
    if task in tasks:
        return tasks[task](user_input)
    
    return f"You are an AI Career Assistant. Respond professionally to the following request: {user_input}"

# ============================================================
# RESPONSE VALIDATION & GENERATION
# ============================================================
def validate_response(response_text: str) -> str:
    if not response_text:
        return "No response was generated or the response was empty."
    return response_text.strip()

def generate_response(task: str, user_input: str) -> str:
    engineered_prompt = build_prompt(task, user_input)
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=engineered_prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.7,
                top_p=0.95,
                max_output_tokens=2048,
            ),
        )
        return validate_response(response.text)
    except Exception as e:
        return f"AI Engine Error: {str(e)}"
