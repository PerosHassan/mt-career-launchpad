# MT Graduate Career Launchpad - Enterprise Edition

## Architecture Overview
This application is refactored into a **decoupled microservices architecture**:
1. **Frontend**: A Streamlit interface that handles user interaction.
2. **Backend**: A FastAPI service that processes requests and manages data flow.
3. **AI Engine**: A dedicated module for interacting with the Google Gemini API.

## Deployment
This project is fully dockerized. To launch the system:
`docker-compose up --build`
