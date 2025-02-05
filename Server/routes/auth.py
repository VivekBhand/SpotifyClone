# this file would deal with user creation and authentication flad
import uuid
import bcrypt
from fastapi import HTTPException

from models.user import User
from pydantic_schemas.user_create import UserCreate
from fastapi import APIRouter
from database import db


# Any function parameter passed directly is considered as a query param ?
# To use request body we have import and use request from fastapi

router = APIRouter()

@router.post('/signup')
def signup_user(user: UserCreate):
    

    # check if user exists in table

    #  db.query(User).all()

    user_db = db.query(User).filter(User.email == user.email).first()
    if user_db:
        raise HTTPException(400, 'User already exists in the database with the same email')
    
    hash_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())  # this is to encrypt password to store as large binary
    # gensalt is used to ensure that no two passwords (either same) will not have same hash_pw
    
    user_db = User(id=str(uuid.uuid4()), name=user.name, email=user.email, password=hash_pw)
    db.add(user_db)
    db.commit() # we have to manually write this because we had set autoCommit to as false while declaring SessionLocal
    db.refresh(user_db)
    return user_db
