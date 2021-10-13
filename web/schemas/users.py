from datetime import datetime
from pydantic import BaseModel


class UsersCreate(BaseModel):
    id: str
    email: str
    username: str
    password: str
    created_date: datetime


class UsersGet(BaseModel):
    id: str
    email: str
    username: str
    created_date: datetime
