from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ai_engine import CareerAI

app = FastAPI(
    title="MT Graduate Career Launchpad API",
    version="2.0.0"
)

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize AI
career_ai = CareerAI()


class ResumeRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return {
        "message": "Welcome to MT Graduate Career Launchpad API",
        "status": "Running"
    }


@app.post("/analyze")
def analyze_resume(request: ResumeRequest):

    feedback = career_ai.analyze_resume(request.text)

    return {
        "success": True,
        "feedback": feedback
    }
