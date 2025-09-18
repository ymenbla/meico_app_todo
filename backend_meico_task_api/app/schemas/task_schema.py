from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Task(BaseModel):
    title: str
    description: str


class TaskCreate(Task):
    user_id: Optional[int] = None


class TaskIn(BaseModel):
    id: int
    title: str
    description: str
    user_id: int
    task_status: Optional[str] = None
    created_at: Optional[datetime] = None


class TaskUpdate(TaskIn):
    pass

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    user_id: int
    task_status: str
    created_at: datetime

    class Config:
        orm_mode = True