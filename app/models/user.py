from sqlmodel import SQLModel,  Field,CheckConstraint
from typing import Optional

class User(SQLModel,table= True):
    id: Optional[int] = Field(default=None,primary_key= True)
    name: str
    email:str
    password:str
    role: Optional[str] = Field(default='N',sa_column_args=(CheckConstraint("role in  ('A','N')")))