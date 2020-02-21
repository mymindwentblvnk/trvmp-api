from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str


class User(BaseModel):
    user_id: int
    email: str
    name: str = None
    is_active: bool

    class Config:
        orm_mode = True
