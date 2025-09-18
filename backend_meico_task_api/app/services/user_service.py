from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.security import create_access_token
from app.repositories.user_repository import UserRepository
from app.schemas.auth_schema import LoginIn
from app.schemas.user_schema import UserCreate
from app.utils.tools_hashing import hash_password, verify_password


class UserService:


    def __init__(self, db: Session):
        self.repository = UserRepository(db)
    

    def one_user(self, user_id: int):
        return self.repository.get_by_id(user_id)
