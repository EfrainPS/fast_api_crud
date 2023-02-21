from sqlalchemy.orm import Session
from ..models import user_posts_model
from ..schemas import user_schema

from ..utilities.encrypt_and_compare import encrypt_and_compare


def get_user(db: Session, user_id: int):
    return db.query(user_posts_model.User).filter(user_posts_model.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(user_posts_model.User).filter(user_posts_model.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_posts_model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schema.UserCreate):
    hashed_password = encrypt_and_compare.generate_hash(user.password)
    db_user = user_posts_model.User(email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user