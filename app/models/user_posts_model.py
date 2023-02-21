from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    is_active = Column(Boolean, default=True)

    ## First param is the class and the second is the relationship created in the children table (class)
    post = relationship("Post", back_populates="owner")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    short_description =  Column(String(255), index=True)
    content = Column(String(4000), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    ## First param is the class and the second is the relationship created in the children table (class)
    owner = relationship("User", back_populates="post")
