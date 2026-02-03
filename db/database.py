import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
Database = os.getenv("DATABASE_URL")
engine = create_engine(Database)
sessionloacl = sessionmaker(autocommit =  False, autoflush = False,bind = engine)
base = declarative_base()

def get_db():
    db = sessionloacl()
    try:
        yield db
    finally:
        db.close()
