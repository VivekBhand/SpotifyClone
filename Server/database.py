# region dbconnection

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



DATABASE_URL = 'postgresql://postgres:password1234@localhost:5432/musicapp'
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind=engine)

db = SessionLocal()
# endregion dbconnection


