from sqlalchemy import Column, Integer, String, DateTime,TIMESTAMP, func
from app.config.db import Base

class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    task_status = Column(String(50), nullable=False, default="pendiente")
    user_id = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.utc_timestamp())
