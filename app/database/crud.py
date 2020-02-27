from sqlalchemy.orm import Session

from app.database.models import UserModel
from app.schemas import UserCreate


def get_user(db: Session, user_id: int) -> UserModel:
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> UserModel:
    user = db.query(UserModel).filter(UserModel.email == email).first()
    return user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate) -> UserModel:
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = UserModel(username= user.username,
                        email=user.email,
                        hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
