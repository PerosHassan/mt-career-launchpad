# 🚀 MT Graduate Career Launchpad

> Launch Your Career With AI

**MT Graduate Career Launchpad** is an AI-powered career development platform developed by **MIDDLE TECHNOLOGY** to help graduates, students, and job seekers improve their employability through intelligent career guidance, resume analysis, and personalized learning.

---

## 🌟 Features

- 🤖 AI Resume Analysis using Google Gemini
- 📄 CV Builder & Optimizer
- 🧠 Career Assessment
- 📊 ATS Resume Score
- 🎯 Employability Score
- 💼 Personalized Career Recommendations
- 📚 Learning Roadmap
- 🎓 Graduate Career Support
- 🏆 Progress Dashboard

---

## 🏗️ System Architecture

The project follows a decoupled microservices architecture.

```
                   +----------------------+
                   |     Streamlit UI     |
                   |      frontend.py     |
                   +----------+-----------+
                              |
                              |
                    HTTP Requests (REST API)
                              |
                              ▼
                   +----------------------+
                   |      FastAPI API     |
                   |      backend.py      |
                   +----------+-----------+
                              |
                              |
                    AI Processing Layer
                              |
                              ▼
                +---------------------------+
                |     Google Gemini AI      |
                |      ai_engine.py         |
                +---------------------------+
```

---

## 📂 Project Structure

```
MT-Graduate-Career-Launchpad/
│
├── frontend.py
├── backend.py
├── ai_engine.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
├── .gitignore
└── .env
```

---

## 🛠 Technology Stack

### Frontend

- Streamlit

### Backend

- FastAPI

### Artificial Intelligence

- Google Gemini API

### Programming Language

- Python 3.10

### Containerization

- Docker
- Docker Compose

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/MT-Graduate-Career-Launchpad.git
```

Move into the project

```bash
cd MT-Graduate-Career-Launchpad
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```
GOOGLE_API_KEY=YOUR_NEW_GEMINI_API_KEY
```

---

## 🐳 Run with Docker

```bash
docker compose up --build
```

Frontend

```
http://localhost:8501
```

Backend

```
http://localhost:8000
```

---

## 🚧 Roadmap

### Version 1

- Resume Analysis
- Career Assessment
- Dashboard

### Version 2

- AI Career Coach
- Portfolio Builder
- Learning Hub
- Job Recommendation Engine
- Scholarship Portal
- Internship Portal

### Version 3

- Authentication
- Employer Dashboard
- AI Interview Practice
- Career Roadmap
- Analytics
- Mobile App

---

## 👨‍💻 Developed By

### MIDDLE TECHNOLOGY

Founder

**Hassan Peros**

Empowering graduates with AI-driven career solutions.

---

## 🤝 Contributing

Contributions, suggestions, and feedback are welcome.

If you'd like to contribute, please fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.
