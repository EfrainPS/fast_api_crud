from sqlalchemy.orm import Session

from ..models import user_posts_model

from ..schemas import posts_schema


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_posts_model.Post).offset(skip).limit(limit).all()


def create_user_post(db: Session, post: posts_schema.PostCreate, user_id: int):
    db_post = user_posts_model.Post(**post.dict(), owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post