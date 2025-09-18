from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.security import create_access_token
from app.repositories.user_repository import UserRepository
from app.schemas.auth_schema import LoginIn
from app.schemas.user_schema import UserCreate
from app.utils.tools_hashing import hash_password, verify_password


class AuthService:


    def __init__(self, db: Session):
        self.repository = UserRepository(db)
    


    def register(self, user: UserCreate):

        new_user = user
        new_user.password = hash_password(user.password)

        existing = self.repository.get_by_email(new_user.email)
        print(existing)
        if existing:
            raise HTTPException(status_code=400, detail="Product already exists")

        return self.repository.create(new_user)



    def authenticate(self, user: LoginIn):

        existing_user = self.repository.get_by_email(user.email)
        if not existing_user:
            return None
        if not verify_password(user.password, existing_user.password):
            return None

        access_token, expires_in = create_access_token({"sub": str(existing_user.id)})

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": expires_in
        }
        