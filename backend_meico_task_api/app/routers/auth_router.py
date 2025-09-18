from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.db import get_db

from app.services.auth_service import AuthService
from app.schemas.auth_schema import LoginIn, TokenOut
from app.schemas.user_schema import UserOut, UserCreate



# auth = APIRouter(prefix="/auth", tags=["auth"])
auth = APIRouter(tags=["auth"])



@auth.post("/register", response_model=UserOut)
def register(payload: UserCreate, db: Session = Depends(get_db)): 
    return AuthService(db).register(payload)


@auth.post("/token", response_model=TokenOut)
def login(payload: LoginIn, db: Session = Depends(get_db)):
    token = AuthService(db).authenticate(payload)
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return token


