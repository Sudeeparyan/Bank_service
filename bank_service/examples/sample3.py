from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class Task(BaseModel):
    summary: str
    description: Optional[str] = None
    estimate: float
    priority: Optional[int] = None

app = FastAPI()

@app.post("/tasks/")
async def create_task(task: Task):
    return task

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000 )