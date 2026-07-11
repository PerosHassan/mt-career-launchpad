import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# ==========================
# Load Environment Variables
# ==========================
load_dotenv()

# Get API Key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError(
        "GOOGLE_API_KEY not found. Please add it to your .env file."
    )

# Initialize Gemini Client
client = genai.Client(api_key=api_key)

# Model Name
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash-lite")

# ==========================
# SYSTEM PROMPT
# ==========================
SYSTEM_PROMPT = """
You are MT Career Launchpad, an AI-powered Career Development Assistant.

Your responsibilities are to:
- Analyze resumes professionally.
- Recommend career paths.
- Suggest resume improvements.
- Identify skill gaps.
- Recommend certifications and learning resources.
- Help users prepare for interviews.
- Generate personalized career roadmaps.

Always respond professionally, accurately, and with actionable advice.

Structure every response using clear headings, bullet points, and numbered lists where appropriate.
"""

# ==========================
# GENERATE AI RESPONSE
# ==========================
def generate_response(user_prompt: str) -> str:
    """
    Sends the user's request to the Gemini Generative AI model
    and returns the generated response.
    """

    # Prompt Engineering
    formatted_prompt = f"""
User Request:
{user_prompt}

Please provide a detailed, professional, personalized, and actionable response.
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=formatted_prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.7,
                max_output_tokens=1024,
            ),
        )

        return response.text

    except Exception as e:
        return f"Error generating AI response: {str(e)}"
