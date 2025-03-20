import google.generativeai as genai
import time
from core.config import get_settings

settings = get_settings()

class InterviewAgent:
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
    
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