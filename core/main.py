import google.generativeai as genai
import time
from core.config import get_settings
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.agents.interview_agent import InterviewAgent

settings = get_settings()

app = FastAPI()
interview_agent = InterviewAgent()

class CandidateProfile(BaseModel):
    profile: str

@app.post("/interview/start")
async def start_interview(candidate: CandidateProfile):
    try:
        response = await interview_agent.generate_response(candidate.profile)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class InterviewAgent:
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(model_name='gemini-2.0-flash') #change the model according to use

    async def generate_response(self, prompt: str):
        max_retries = 3
        retry_delay = 1

        for attempt in range(max_retries):
            try:
                response = self.model.generate_content(prompt)
                return response.text.strip()
            except Exception as e:
                if attempt == max_retries - 1:
                    return f"Error: Failed to generate response after {max_retries} retries. Details: {str(e)}"
                time.sleep(retry_delay)
                retry_delay *= 2