
from fastapi import FastAPI
from routes import auth
from models.base import Base
from database import engine

app = FastAPI()

app.include_router(auth.router, prefix='/auth'); # this makes sure that main know that a router exists in the auth file. 
# prefix added prefix to all api urls

Base.metadata.create_all(engine)
