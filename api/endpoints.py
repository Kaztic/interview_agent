from fastapi import APIRouter
from tasks.llm_tasks import process_interview_task
from core.schemas import AgentRequest, TaskResponse

router = APIRouter()

@router.post("/interview", response_model=TaskResponse)
async def create_interview_task(request: AgentRequest):
    task = process_interview_task.delay(request.prompt)
    return {
        "task_id": task.id,
        "status": "queued"
    }

@router.get("/tasks/{task_id}", response_model=dict)
async def get_task_result(task_id: str):
    task_result = process_interview_task.AsyncResult(task_id)
    return {
        "task_id": task_id,
        "status": task_result.status,
        "result": task_result.result
    }