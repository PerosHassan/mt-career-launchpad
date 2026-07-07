from fastapi import FastAPI
from pydantic import BaseModel
from ai_engine import generate_response

app = FastAPI(title="MT Career Launchpad API")


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {
        "message": "Welcome to the MT Career Launchpad API!",
        "status": "running"
    }


@app.post("/generate")
def generate(request: PromptRequest):
    response = generate_response(request.prompt)
    return {"response": response}
