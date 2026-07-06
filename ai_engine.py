import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()


class CareerAI:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError(
                "GOOGLE_API_KEY was not found in the .env file."
            )

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def analyze_resume(self, resume_text: str):

        prompt = f"""
You are an expert Career Coach, ATS Resume Reviewer and HR Recruiter.

Analyze the following resume.

Resume:

{resume_text}

Return the report using the following format.

# Resume Summary

# Employability Score (0-100)

# ATS Score (0-100)

# Strengths

# Weaknesses

# Missing Skills

# Recommended Certifications

# Suggested Career Paths

# Interview Preparation Tips

# Final Recommendations
"""

        try:

            response = self.model.generate_content(prompt)

            return response.text

        except Exception as e:

            return f"AI Error: {str(e)}"
