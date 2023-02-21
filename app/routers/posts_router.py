from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from ..models import user_posts_model

from ..crud import posts_crud
from ..schemas import posts_schema
from ..config.database import SessionLocal, engine

user_posts_model.Base.metadata.create_all(bind=engine)

posts_router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@posts_router.post("/users/{user_id}/posts/", response_model=posts_schema.Post)
def create_post_for_user(
    user_id: int, post: posts_schema.PostCreate, db: Session = Depends(get_db)
):
    return posts_crud.create_user_post(db=db, post=post, user_id=user_id)


@posts_router.get("/posts/", response_model=list[posts_schema.Post])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = posts_crud.get_posts(db, skip=skip, limit=limit)
    return posts
