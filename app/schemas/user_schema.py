from pydantic import BaseModel
from .posts_schema import Post


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    post: list[Post] = []

    class Config:
        orm_mode = True