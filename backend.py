from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ai_engine import CareerAI

app = FastAPI(
    title="MT Graduate Career Launchpad API",
    version="2.0.0"
)

# Initialize the AI engine
career_ai = CareerAI()


class AnalysisRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {
        "message": "Welcome to MT Graduate Career Launchpad API",
        "status": "Running"
    }


@app.post("/analyze")
async def analyze(request: AnalysisRequest):
    """
    Analyze a user's resume using Google Gemini AI.
    """

    try:
        if not request.text.strip():
            raise HTTPException(
                status_code=400,
                detail="Resume text cannot be empty."
            )

        feedback = career_ai.analyze_resume(request.text)

        return {
            "success": True,
            "feedback": feedback
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Analysis failed: {str(e)}"
        )
