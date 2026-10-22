import uuid

from database.database_connection import engine
from sqlalchemy import Table,Column,Integer,String,UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#declarative_base() creates the Base class that you use to define your SQLAlchemy database models.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base=declarative_base()
class User(Base):
    __tablename__='users'
    id=Column(Integer, primary_key=True, index=True,autoincrement=True)
    name=Column(String(100),nullable=False)
    email=Column(String(100),nullable=False,unique=True) 
    password=Column(String(100),nullable=False)



#creates all tables defined in your SQLAlchemy models in the 
# database connected through engine, if they don't already exist.
Base.metadata.create_all(engine) 

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()  

get_db()
