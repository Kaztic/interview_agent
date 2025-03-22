#!/bin/bash

# Activate virtual environment
source interview_agent_env/bin/activate

# Run the FastAPI server using uvicorn
uvicorn server:app --host 0.0.0.0 --port 8000 --reload 