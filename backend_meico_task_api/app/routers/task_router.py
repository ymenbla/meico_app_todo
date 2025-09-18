from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.config.db import get_db
from app.core.security import get_current_user
from app.schemas.task_schema import TaskCreate, TaskUpdate, TaskOut
from app.services.task_service import TaskService

task = APIRouter(tags=["tasks"])


@task.get("/tasks", response_model=list[TaskOut])
def all_task(
    db: Session = Depends(get_db), 
    current_user: dict = Depends(get_current_user)
):
    user_id = current_user.get('user_id', 0)
    return TaskService(db).all_tasks(user_id)


@task.post("/tasks", response_model=TaskOut)
def put_task(
    payload: TaskCreate, db: Session = Depends(get_db), 
    current_user: dict = Depends(get_current_user)
):
    
    payload.user_id = current_user.get('user_id', 0)
    print("payload",payload)
    return TaskService(db).new_task(task=payload)


@task.put("/tasks/{id}", response_model=TaskOut)
def put_task(
    id: int, 
    payload: TaskUpdate, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return TaskService(db).update_task(task_id=id, task=payload)


@task.delete("/tasks/{id}", status_code=status.HTTP_204_NO_CONTENT)
def put_task(
    id: int, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    task_deleted = TaskService(db).delete_task(id)
    if not task_deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return None