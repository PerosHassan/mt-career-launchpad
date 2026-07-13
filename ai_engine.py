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

# Updated default model string fallback to the faster, smarter gemini-2.5-flash
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

You are an intelligent AI Career Development Assistant designed to
help students, graduates and professionals achieve career success.

Your responsibilities include:

• Resume Analysis
• ATS Resume Optimization
• CV Writing
• Career Assessment
• Career Roadmaps
• Interview Preparation
• Skill Gap Analysis
• Learning Recommendations
• Certification Recommendations

Always:

Understand the user's goal.
Think before answering.
Give professional and practical advice.
Explain your reasoning.
Use headings.
Use bullet points.
End every response with actionable next steps.
Never fabricate information.
"""

# ============================================================
# PROMPT TEMPLATES
# ============================================================

def resume_prompt(user_input: str):
    return f"""
You are an ATS Resume Expert.
Analyse the following resume professionally.

Provide:
1. ATS Score
2. Strengths
3. Weaknesses
4. Missing Skills
5. Improvement Suggestions
6. Final Recommendation

Resume:
{user_input}
"""

def career_prompt(user_input: str):
    return f"""
You are a Senior Career Coach.
Analyse the user's profile.

Provide:
1. Best Career Paths
2. Skills to Learn
3. Certifications
4. Job Opportunities
5. One-Year Career Plan

User Information:
{user_input}
"""

def cv_prompt(user_input: str):
    return f"""
Create a professional ATS-friendly CV.

Include:
Professional Summary
Skills
Education
Experience
Projects
Certifications
Achievements

Information:
{user_input}
"""

def roadmap_prompt(user_input: str):
    return f"""
Create a detailed 12-month learning roadmap.

Career Goal:
{user_input}

Include:
Monthly Plan
Skills
Courses
Certifications
Portfolio Projects
Career Opportunities
"""

def interview_prompt(user_input: str):
    return f"""
You are an Interview Coach.
Prepare the user for interviews.

Provide:
Common Questions
Model Answers
Interview Tips
Mistakes to Avoid

Role:
{user_input}
"""

# ============================================================
# PROMPT ROUTER
# ============================================================

def build_prompt(task: str, user_input: str):
    prompts = {  
        TASK_RESUME: resume_prompt,  
        TASK_CAREER: career_prompt,  
        TASK_CV: cv_prompt,  
        TASK_ROADMAP: roadmap_prompt,  
        TASK_INTERVIEW: interview_prompt,  
    }  

    if task in prompts:  
        return prompts[task](user_input)  

    return user_input

# ============================================================
# RESPONSE VALIDATION
# ============================================================

def validate_response(text):
    if text is None:  
        return "No response generated."  

    if not str(text).strip():  
        return "No response generated."  

    return str(text).strip()

# ============================================================
# GENERATE RESPONSE
# ============================================================

def generate_response(task: str, user_input: str):
    prompt = build_prompt(task, user_input)  

    try:  
        response = client.models.generate_content(  
            model=MODEL_NAME,  
            contents=prompt,  
            config=types.GenerateContentConfig(  
                system_instruction=SYSTEM_PROMPT,  
                temperature=0.7,  
                top_p=0.95,  
                max_output_tokens=2048,  
            ),  
        )  

        return validate_response(response.text)  

    except Exception as e:  
        error = str(e)  

        # Google Gemini service temporarily busy  
        if "503" in error or "UNAVAILABLE" in error:  
            return (  
                "⚠️ The AI service is currently experiencing high demand.\n\n"  
                "Please wait a few moments and try again."  
            )  

        # Invalid API Key  
        if "API_KEY_INVALID" in error or "400" in error:  
            return (  
                "❌ AI Configuration Error.\n\n"  
                "The Google Gemini API key is invalid or missing."  
            )  

        # Any other unexpected error  
        return f"❌ AI Engine Error:\n\n{error}"
