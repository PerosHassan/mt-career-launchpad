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

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "gemini-2.5-flash-lite"
)
# ============================================================
# INITIALIZE GEMINI CLIENT
# ============================================================

client = genai.Client(api_key=API_KEY)
# ============================================================
# SYSTEM PROMPT
# ============================================================

SYSTEM_PROMPT = """
You are MT Career Launchpad AI.

You are an intelligent Career Development Assistant built to help students,
graduates and professionals grow in their careers.

Your responsibilities include:

• Resume Analysis

• Career Assessment

• CV Writing

• ATS Optimization

• Interview Preparation

• Career Roadmaps

• Skills Gap Analysis

• Learning Recommendations

• Certification Recommendations

Always:

- Think carefully before answering.

- Understand the user's goal.

- Give professional advice.

- Explain your reasoning.

- Structure responses with headings.

- Use bullet points.

- End with practical next steps.

Never fabricate information.

If you do not know something,
state the limitation clearly.
"""
# ============================================================
# TASK DETECTION
# ============================================================

def detect_task(user_input: str):

    text = user_input.lower()

    if "resume" in text:
        return "resume"

    if "cv" in text:
        return "cv"

    if "roadmap" in text:
        return "roadmap"

    if "career" in text:
        return "career"

    if "interview" in text:
        return "interview"

    return "general"
    def resume_prompt(user_input):

    return f"""
You are an ATS Resume Expert.

Analyse this resume professionally.

Provide:

1. ATS Score

2. Strengths

3. Weaknesses

4. Missing Skills

5. Improvements

6. Final Recommendation

Resume:

{user_input}
"""
    def career_prompt(user_input):

    return f"""
You are a Senior Career Coach.

Analyse the user's information.

Recommend:

• Best Career Paths

• Skills to Learn

• Certifications

• Job Opportunities

• One-Year Career Plan

Information:

{user_input}
"""
    def cv_prompt(user_input):

    return f"""
Create an ATS-friendly CV.

Include:

Professional Summary

Skills

Education

Experience

Projects

Achievements

Information:

{user_input}
"""
    def roadmap_prompt(user_input):

    return f"""
Create a 12-month learning roadmap.

Career Goal:

{user_input}

Include:

Monthly Learning Plan

Projects

Certifications

Portfolio

Resources

Career Opportunities
"""
    def interview_prompt(user_input):

    return f"""
You are an Interview Coach.

Prepare the user for interviews.

Provide:

Common Questions

Model Answers

Tips

Mistakes to Avoid

Role:

{user_input}
"""
    def build_prompt(task, user_input):

    if task == "resume":
        return resume_prompt(user_input)

    if task == "career":
        return career_prompt(user_input)

    if task == "cv":
        return cv_prompt(user_input)

    if task == "roadmap":
        return roadmap_prompt(user_input)

    if task == "interview":
        return interview_prompt(user_input)

    return user_input
    def validate_response(response):

    if not response:
        return "No response generated."

    return response.strip()
    def generate_response(task: str, user_input: str):

    task = detect_task(user_input)

    engineered_prompt = build_prompt(
        task,
        user_input
    )

    try:

        response = client.models.generate_content(

            model=MODEL_NAME,

            contents=engineered_prompt,

            config=types.GenerateContentConfig(

                system_instruction=SYSTEM_PROMPT,

                temperature=0.7,

                top_p=0.95,

                max_output_tokens=2048,

            )

        )

        return validate_response(response.text)

    except Exception as e:

        return f"AI Engine Error: {e}"
