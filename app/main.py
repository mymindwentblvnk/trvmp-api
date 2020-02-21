from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.crud import get_user_by_email, create_user
from app.database import SessionLocal, engine
from app.database import Base
from app.schemas import User, UserCreate


Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db() -> Session:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=User)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="E-Mail already registered")
    return create_user(db=db, user=user)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
