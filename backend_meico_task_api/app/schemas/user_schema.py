
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    
    full_name: str
    email: str
    password: str

class UserCreate(User):
    pass
    

class UserOut(BaseModel):
    id: int
    full_name: str
    email: str
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True