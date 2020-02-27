from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    username: str
    password: str


class User(BaseModel):
    user_id: int
    username: str
    email: str
    disabled: bool

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str
