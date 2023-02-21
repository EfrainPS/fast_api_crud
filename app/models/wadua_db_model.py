from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..config.database import Base

class User(Base):
    __tablename__ = "users_"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    ...

    comment = relationship("Comment", back_populates="user")  


class Comment(Base):
    __tablename__ = "comments"

    comment_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users_.user_id"))
    ...

    user = relationship("User", back_populates="comment")