#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Install dependencies if not already installed
# pip install -r requirements.txt

# Run the FastAPI server using uvicorn
uvicorn server:app --host 0.0.0.0 --port 8000 --reload 