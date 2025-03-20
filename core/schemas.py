from pydantic import BaseModel
from enum import Enum

class ModelType(str, Enum):
    GEMINI = "gemini"

class AgentRequest(BaseModel):
    prompt: str
    model: ModelType = ModelType.GEMINI

class TaskResponse(BaseModel):
    task_id: str
    status: str