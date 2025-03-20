from celery_config import app
from core.agents import InterviewAgent
import asyncio

@app.task
def process_interview_task(prompt: str):
    agent = InterviewAgent()
    return asyncio.run(agent.generate_response(prompt))