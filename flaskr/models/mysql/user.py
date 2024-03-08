from sqlalchemy import Column, Integer, String, DateTime, func
from flaskr.models.mysql.base import BaseModel


class Users(BaseModel):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    age = Column(Integer, nullable=False)
    createdAt = Column(DateTime, nullable=False, default=func.now())
    updatedAt = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
