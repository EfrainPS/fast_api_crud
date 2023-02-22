from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Date, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from ..config.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(75), unique=True, index=True)
    email = Column(String(255), unique=True,index=True)
    password = Column(String(75))
    type = Column(Enum("admin","writter","viewer"))
    created_date = Column(Date)
    last_login = Column(Date)
    
    # Relations 

    post = relationship("Post" , back_populates="user")
    comment = relationship("Comment", back_populates="user")  

class Comment(Base):
    __tablename__ = "comments"

    comment_id = Column(Integer, primary_key=True, index=True)
    content = Column(String(4000),index=True)
    publication_date = (Date)
    users_id = Column(Integer, ForeignKey("users.user_id"))
    posts_id = Column(Integer, ForeignKey("posts.post_id"))

    # Relations

    post = relationship("Post" , back_populates="comment")
    user = relationship("User", back_populates="comment")

class Post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255),index=True)
    content = Column(String(4000), index=True)
    created_date = Column(Date)
    updated_date = Column(Date)
    status = Column(Enum("traft","published","archived"))
    user_id = Column(Integer, ForeignKey ("users.user_id"))

    # Relations 

    comment = relationship("Comment", back_populates="post") 
    user = relationship("User", back_populates="post" )
    hashtag = relationship ("Hashtag",secondary="post_hashtags", back_populates= "post") 


post_hashtags = Table("post_hashtags", Base.metadata,

    Column("post_id", Integer, ForeignKey("posts.post_id")),
    Column("hashtag_id", Integer, ForeignKey("hashtags.hashtag_id"))
)
    # Relations

  
   
class Hashtag(Base):
    __tablename__ = "hashtags"

    hashtag_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(75), index=True)
    description = Column(String(255),index= True)  
    publication_date = Column(Date)

    # Relations 

    post = relationship ("Post", secondary="post_hashtags", back_populates= "hashtag")