from fastapi import FastAPI


app = FastAPI()


from .config.database import engine
from .models import wadua_db_model #test

wadua_db_model.Base.metadata.create_all(bind=engine)
