import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

try:
    print("\n===== AVAILABLE MODELS =====\n")

    for model in client.models.list():
        print(model.name)

except Exception as e:
    print("ERROR:")
    print(e)
