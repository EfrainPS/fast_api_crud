from fastapi import FastAPI
from .routers.user_router import user_router
from .routers.posts_router import posts_router

app = FastAPI()

app.include_router(user_router)
app.include_router(posts_router)

#if __name__ == '__main__':
#    uvicorn.run(app)