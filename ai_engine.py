import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY not found. Please add it to your .env file."
    )

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_response(prompt: str) -> str:
    """
    Generate a response from Google's Gemini model.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
