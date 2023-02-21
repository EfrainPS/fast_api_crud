from fastapi import FastAPI
from .routers.user_router import user_router
from .routers.posts_router import posts_router

app = FastAPI()


from .config.database import engine
from .models import wadua_db_model #test

wadua_db_model.Base.metadata.create_all(bind=engine)
