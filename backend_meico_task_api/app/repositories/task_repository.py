from typing import Optional
from sqlalchemy.orm import Session
from app.models.task_model import Tasks
from app.schemas.task_schema import TaskCreate, TaskOut, TaskUpdate



class TaskRepository():



    def __init__(self, db: Session):
        self.db = db



    def get_all(self, user_id: int):
        return self.db.query(Tasks).filter(Tasks.user_id == user_id).all()
    


    def get_by_id(self, task_id: int):
        result = self.db.query(Tasks).filter(Tasks.id == task_id).first()
        return result


    def create(self, task: TaskCreate):
        
        db_task = Tasks(
            title = task.title,
            description = task.description,
            user_id = task.user_id
        )
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task
    
    def update(self, task_id: int, task: TaskUpdate):
        
        db_task = self.get_by_id(task_id)

        if db_task is not None:

            db_task.title =  task.title
            db_task.description = task.description
            db_task.task_status = task.task_status

            self.db.commit()
            self.db.refresh(db_task)
        return db_task
    
    def delete(self, task_id: int):
        db_task = self.get_by_id(task_id)

        if db_task is not None:
            self.db.delete(db_task)
            self.db.commit()
            return True  
        
        return False