import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError(
        "GOOGLE_API_KEY not found. Please add it to your .env file."
    )

# Create Gemini client
client = genai.Client(api_key=api_key)

# Model name
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash")


def generate_response(prompt: str) -> str:
    """
    Generate a response using Google Gemini.
    """
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )
        return response.text

    except Exception as e:
        return f"Error: {e}"
