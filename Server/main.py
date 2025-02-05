import bcrypt
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import TEXT, VARCHAR, Column, LargeBinary, create_engine # function which is used to create engine to connect to db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid

app = FastAPI()

# region dbconnection

DATABASE_URL = 'postgresql://postgres:password1234@localhost:5432/musicapp'
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind=engine)

db = SessionLocal()
# endregion dbconnection

Base = declarative_base() # this is used for Creating Table and stuff

class UserCreate(BaseModel):    
    name : str
    email : str
    password : str


# region Table defination

# this blocks defines the table
#creates a new table with given parameters if table not exists

class User(Base):

    __tablename__ = 'users'

    id = Column(TEXT, primary_key=True)
    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100))
    password = Column(LargeBinary)

# endregion Table defination

Base.metadata.create_all(engine)

# Any function parameter passed directly is considered as a query param ?
# To use request body we have import and use request from fastapi

@app.post('/signup')
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
