import google.generativeai as genai
import os

class CareerAI:
    def __init__(self):
        # API key is fetched from the environment for security
        api_key = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_response(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text
