from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv


# Charger les vatiables d'env

load_dotenv()

DATABASE_URL=os.getenv("DATABASE_URL")

engine=create_engine(DATABASE_URL)

# Creer une session 
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()