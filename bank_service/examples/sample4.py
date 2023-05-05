from typing import Optional
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

class Task(BaseModel):
    summary: str
    description: Optional[str] = None
    estimate: float
    priority: Optional[int] = None

app = FastAPI()

@app.put("/tasks/{task_id}")
async def edit_item(task_id: int, task: Task):
    return {"item_id": task_id, **task.dict()}

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000 )