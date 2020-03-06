from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED

from app.authentication import Token, authenticate_user, create_access_token
from app.database import get_db_session
from app.database.crud import get_user_by_email, create_user
from app.schemas import User, UserCreate

app = FastAPI()


@app.post("/users", response_model=User)
def create_user(user: UserCreate,
                db: Session = Depends(get_db_session)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="E-Mail already registered")
    return create_user(db=db, user=user)


@app.post("/token", response_model=Token)
async def login(db: Session = Depends(get_db_session),
                form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db,
                             username=form_data.username,
                             password=form_data.password)
    if not user:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password",
                            headers={"WWW-Authenticate": "Bearer"})
    access_token = create_access_token(data={'sub': user.username})
    return {'access_token': access_token, 'token_type': 'bearer'}
