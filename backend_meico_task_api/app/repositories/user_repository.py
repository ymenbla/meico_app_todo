from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate
from app.models.user_model import Users

class UserRepository:


    def __init__(self, db: Session):
        self.db = db



    def get_by_email(self, email: str):
        result = self.db.query(Users).filter(Users.email == email).first()
        return result
    


    def get_by_id(self, user_id: str):
        result = self.db.query(Users).filter(Users.id == user_id).first()
        return result



    def create(self, user: UserCreate):
        
        db_user = Users(
            full_name=user.full_name,
            email=user.email,
            password=user.password
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    