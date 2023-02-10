from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from ..models import user_item_model

from ..crud import item_crud
from ..schemas import item_schema
from ..config.database import SessionLocal, engine

user_item_model.Base.metadata.create_all(bind=engine)

item_router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@item_router.post("/users/{user_id}/items/", response_model=item_schema.Item)
def create_item_for_user(
    user_id: int, item: item_schema.ItemCreate, db: Session = Depends(get_db)
):
    return item_crud.create_user_item(db=db, item=item, user_id=user_id)


@item_router.get("/items/", response_model=list[item_schema.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = item_crud.get_items(db, skip=skip, limit=limit)
    return items
