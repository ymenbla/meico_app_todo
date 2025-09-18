from sqlalchemy.orm import Session

from app.repositories.task_repository import TaskRepository
from app.schemas.task_schema import TaskCreate, TaskIn, TaskUpdate

class TaskService:


    def __init__(self, db: Session):
        self.repository = TaskRepository(db)

    def one_task(self, id: int):
        return self.repository.get_by_id(id)

    def all_tasks(self, user_id: int):
        return self.repository.get_all(user_id)


    def new_task(self, task: TaskCreate):
        task_respone = self.repository.create(task)
        return task_respone
    
    def update_task(self, task_id: int, task: TaskUpdate):
        task_respone = self.repository.update(task_id, task)
        return task_respone
    
    def delete_task(self, task_id: int):
        task_respone = self.repository.delete(task_id)
        return task_respone

