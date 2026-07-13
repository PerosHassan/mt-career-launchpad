# 🚀 MT Career Launchpad AI

MT Career Launchpad AI is an AI-powered career development platform that helps students, graduates, and professionals make informed career decisions using Google's Gemini Generative AI.

The platform provides personalized career support through resume analysis, career assessments, ATS-friendly CV generation, interview preparation, career roadmaps, and AI-powered recommendations based on user profiles.

---

# 🌟 Features

## 🔐 User Management
- User registration and login
- Secure password hashing
- Session-based authentication
- User-specific dashboard
- Profile management

## 🤖 AI Career Tools
- 📄 AI Resume Analyzer
- 🧠 Career Assessment
- 📝 ATS-Friendly CV Builder
- 🗺 Personalized Career Roadmap
- 🎤 AI Interview Coach

## 📊 Personalization
- User career profile
- Profile completion tracking
- AI responses based on user information
- Personalized career recommendations

## 📥 Export Features
- Professional PDF reports
- Microsoft Word document export

## ⚙️ Technology
- Google Gemini Generative AI
- FastAPI Backend
- Streamlit Frontend
- SQLite Database
- Modular AI Engine
- Prompt Engineering

---

# 🏗️ Project Architecture

```text
                    User
                      │
                      ▼
            Streamlit Frontend
                      │
                      ▼
             FastAPI Backend
                      │
                      ▼
              Authentication
                      │
                      ▼
              User Database
              (SQLite)
                      │
                      ▼
                AI Engine
          (Prompt Engineering)
                      │
                      ▼
            Google Gemini API
                      │
                      ▼
              Personalized AI
               Response
```
---
## 📂 Project Structure
```text
mt-career-launchpad/
│
├── ai_engine.py        # AI Engine & Prompt Engineering
├── backend.py          # FastAPI Backend
├── frontend.py         # Streamlit Frontend
├── .env                # Environment Variables
├── requirements.txt    # Project Dependencies
├── README.md           # Documentation
```
---
# ⚙️ Installation
## 1. Clone the Repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/mt-career-launchpad.git
cd mt-career-launchpad
```
## 2. Create a Virtual Environment
### Windows
```bash
python -m venv venv
venv\Scripts\activate
```
### Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```
## 3. Install Dependencies
```bash
pip install -r requirements.txt
```
## 4. Configure Environment Variables
Create a `.env` file in the project root.
```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
MODEL_NAME=gemini-2.5-flash-lite
```
---
# 📦 Requirements
This project uses the following technologies:
- Python 3.11+
- Streamlit
- FastAPI
- Uvicorn
- Requests
- python-dotenv
- Google GenAI SDK
---
# ▶️ Running the Application
## Start the Backend
```bash
uvicorn backend:app --reload
```
The backend will be available at:
```
http://localhost:8000
```
---
## Start the Frontend
Open another terminal and run:
```bash
streamlit run frontend.py
```
The application will be available at:
```
http://localhost:8501
```
---
## API Endpoint
POST
```
/generate
```
Example Request
```json
{
    "task": "resume",
    "input": "Paste your resume here..."
}
```
---
# 🤖 AI Engine
The AI Engine is implemented in `ai_engine.py`.
It is responsible for:
- Loading environment variables
- Connecting to Google Gemini
- Managing the system prompt
- Prompt engineering
- Routing user requests
- Generating AI responses
- Validating AI outputs
- Handling AI-related errors
## AI Workflow
```text
User Request
      │
      ▼
Frontend (Streamlit)
      │
      ▼
Backend (FastAPI)
      │
      ▼
AI Engine
      │
      ├── System Prompt
      ├── Prompt Templates
      ├── Task Routing
      ├── Gemini API
      └── Response Validation
      ▼
AI Response
```
The AI Engine uses prompt engineering techniques to generate structured and professional career guidance tailored to the user's request.
---
# 🛠️ Technologies Used

| Technology | Purpose |
| :--- | :--- |
| Python 3.11 | Programming Language |
| Streamlit | Frontend User Interface |
| FastAPI | Backend REST API |
| Uvicorn | ASGI Server |
| Google GenAI SDK | Gemini AI Integration |
| python-dotenv | Environment Variable Management |
| Requests | HTTP Communication |

---
# 🚀 Future Improvements
The following enhancements are planned for future releases:
- User authentication and login
- Save career history and AI conversations
- Resume file upload (PDF/DOCX)
- LinkedIn profile analysis
- AI-powered interview simulator
- Job recommendation engine
- Resume scoring dashboard
- Export CV as PDF
- Admin analytics dashboard
- Multi-language support
---
# 📌 Project Status
The project architecture and AI integration have been completed.
Current implementation includes:
- ✅ Streamlit Frontend
- ✅ FastAPI Backend
- ✅ Modular AI Engine
- ✅ Prompt Engineering
- ✅ System Prompt Design
- ✅ Task-Based Prompt Routing
- ✅ Google Gemini Integration
> **Note:** During testing, AI response generation may depend on the availability of a valid Google Gemini API key and an active Google AI Studio/Google Cloud billing configuration.
---
# 👨‍💻 Author
**Hassan Peros**
Founder, Middle Technology
Passionate about Artificial Intelligence, Product Management, Digital Innovation, and Career Development.
GitHub:
https://github.com/YOUR_GITHUB_USERNAME
LinkedIn:
https://www.linkedin.com/in/YOUR_LINKEDIN_USERNAME
---
# 📄 License
This project is licensed under the MIT License.
Feel free to use, modify, and distribute this project for educational and personal learning purposes.
