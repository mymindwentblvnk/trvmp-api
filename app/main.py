from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database.crud import get_user_by_email, create_user
from app.database import SessionLocal
from app.schemas import User, UserCreate, UserInDB

from starlette.status import HTTP_400_BAD_REQUEST

from app.authentication import fake_hash_password, fake_users_db, get_current_active_user


app = FastAPI()


def get_db() -> Session:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/users", response_model=User)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="E-Mail already registered")
    return create_user(db=db, user=user)


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail="Incorrect username or password")

    return {
        'access_token': 'a_token',
        'token_type': 'bearer'
    }


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
