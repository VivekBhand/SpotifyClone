# this file will have declaration of all table structures

from pydantic import BaseModel

class UserCreate(BaseModel):    
    name : str
    email : str
    password : str