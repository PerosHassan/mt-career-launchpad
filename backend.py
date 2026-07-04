from fastapi import FastAPI
from pydantic import BaseModel
from ai_engine import CareerAI

app = FastAPI()
ai_engine = CareerAI()

class CareerRequest(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_career(request: CareerRequest):
    # This keeps the AI functionality visible and decoupled from the frontend
    result = ai_engine.generate_response(f"Analyze this: {request.text}")
    return {"feedback": result}
