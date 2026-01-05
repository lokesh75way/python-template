from typing import List, Optional
from pydantic import BaseModel, validator
from .item import Item

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str
    
    # 3.3 Validation & serialization
    # 3.3 Custom validators
    @validator('password')
    def password_must_be_strong(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return v

class User(UserBase):
    id: int
    is_active: bool
    # 3.3 Nested schemas
    items: List[Item] = []

    class Config:
        from_attributes = True
