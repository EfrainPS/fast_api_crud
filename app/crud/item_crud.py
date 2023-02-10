from sqlalchemy.orm import Session

from ..models import user_item_model

from ..schemas import item_schema


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_item_model.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: item_schema.ItemCreate, user_id: int):
    db_item = user_item_model.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item