from sqlalchemy import TEXT, VARCHAR, Column, LargeBinary
from models.base import Base

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