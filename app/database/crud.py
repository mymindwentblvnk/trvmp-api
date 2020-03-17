from typing import List

from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.database.models import UserModel
from app.schemas import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password) -> str:
    return pwd_context.hash(password)


def get_user(db: Session, user_id: int) -> UserModel:
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> UserModel:
    return db.query(UserModel).filter(UserModel.email == email).first()


def get_user_by_username(db: Session, username: str) -> UserModel:
    return db.query(UserModel).filter(UserModel.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[UserModel]:
    return db.query(UserModel).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate) -> UserModel:
    hashed_password = get_password_hash(user.password)
    db_user = UserModel(username=user.username,
                        email=user.email,
                        hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
