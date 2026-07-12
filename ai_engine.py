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
    raise ValueError(
        "GOOGLE_API_KEY not found. Please add it to your .env file."
    )

# ============================================================
# MODEL CONFIGURATION
# ============================================================
MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "gemini-2.5-flash"
)

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
You are MT Career Launchpad AI.

You are an intelligent Career Development Assistant built to help students,
graduates and professionals make informed career decisions.

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

- Understand the user's goal.
- Think carefully before answering.
- Provide accurate and professional advice.
- Explain your reasoning.
- Structure responses using headings.
- Use bullet points whenever appropriate.
- End with practical next steps.
- Never fabricate information.
- If uncertain, clearly state your limitations.
"""

# ============================================================
# PROMPT TEMPLATES
# ============================================================

def resume_prompt(user_input: str) -> str:
    return f"""
You are an ATS Resume Expert.

Analyse the following resume professionally.

Provide:

1. ATS Score (out of 100)
2. Strengths
3. Weaknesses
4. Missing Skills
5. Recommendations for Improvement
6. Final Summary

Resume:

{user_input}
"""


def career_prompt(user_input: str) -> str:
    return f"""
You are a Senior Career Advisor.

Analyse the user's information.

Provide:

1. Suitable Career Paths
2. Skills to Develop
3. Recommended Certifications
4. Job Opportunities
5. One-Year Career Development Plan

User Information:

{user_input}
"""


def cv_prompt(user_input: str) -> str:
    return f"""
You are an Expert CV Writer.

Create an ATS-friendly professional CV.

Include:

- Professional Summary
- Skills
- Education
- Experience
- Projects
- Certifications
- Achievements

Information:

{user_input}
"""


def roadmap_prompt(user_input: str) -> str:
    return f"""
You are a Career Mentor.

Create a detailed 12-month learning roadmap.

Career Goal:

{user_input}

Include:

- Beginner Skills
- Intermediate Skills
- Advanced Skills
- Recommended Courses
- Certifications
- Portfolio Projects
- Monthly Timeline
- Career Opportunities
"""


def interview_prompt(user_input: str) -> str:
    return f"""
You are an Interview Coach.

Prepare the user for interviews.

Provide:

- Common Interview Questions
- Sample Answers
- Interview Tips
- Mistakes to Avoid

Target Role:

{user_input}
"""

# ============================================================
# PROMPT ROUTER
# ============================================================

def build_prompt(task: str, user_input: str) -> str:

    prompts = {
        TASK_RESUME: resume_prompt,
        TASK_CAREER: career_prompt,
        TASK_CV: cv_prompt,
        TASK_ROADMAP: roadmap_prompt,
        TASK_INTERVIEW: interview_prompt,
    }

    if task in prompts:
        return prompts[task](user_input)

    return f"""
You are a Professional Career Development Assistant.

Respond professionally to the following request.

User Request:

{user_input}
"""

# ============================================================
# RESPONSE VALIDATION
# ============================================================

def validate_response(response_text: str) -> str:

    if not response_text:
        return "No AI response was generated."

    return response_text.strip()

# ============================================================
# GENERATE AI RESPONSE
# ============================================================

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
        return f"AI Engine Error: {e}"
