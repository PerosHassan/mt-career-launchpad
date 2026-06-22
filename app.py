# ============================================================================
# FEATURE 3: AI INTERVIEW SIMULATOR (ENHANCED)
# ============================================================================
def generate_interview_question(role, difficulty="medium"):
    """Generate AI-powered interview questions"""
    questions = {
        "technical": [
            "Explain the difference between SQL and NoSQL databases.",
            "How would you optimize a slow-running algorithm?",
            "Describe your experience with cloud platforms.",
            "What is the difference between GET and POST requests?"
        ],
        "behavioral": [
            "Tell me about a time you faced a challenging project deadline.",
            "Describe a situation where you had to work with a difficult team member.",
            "Give an example of how you've shown leadership.",
            "Tell me about a mistake you made and how you handled it."
        ],
        "hr": [
            "Why do you want to work for our company?",
            "Where do you see yourself in 5 years?",
            "What are your greatest strengths and weaknesses?",
            "Why should we hire you?"
        ]
    }
    
    import random
    category = random.choice(list(questions.keys()))
    return random.choice(questions[category]), category
