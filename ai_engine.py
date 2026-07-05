import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class CareerAI:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError(
                "GOOGLE_API_KEY not found. Please add it to your .env file."
            )

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def analyze_resume(self, resume_text):
        """
        Analyze a user's resume and return professional career advice.
        """

        prompt = f"""
You are an expert Career Coach, ATS Resume Reviewer, HR Recruiter, and Hiring Manager.

Analyze the resume below and provide a professional report.

Resume:

{resume_text}

Provide your response using this format:

1. Overall Resume Summary

2. Employability Score (0-100)

3. ATS Compatibility Score (0-100)

4. Resume Strengths

5. Resume Weaknesses

6. Missing Skills

7. Recommended Certifications

8. Recommended Career Paths

9. Interview Preparation Tips

10. Suggested Resume Improvements

11. Final Career Advice
"""

        try:
            response = self.model.generate_content(prompt)

            return response.text

        except Exception as e:
            return f"AI Error: {str(e)}"
