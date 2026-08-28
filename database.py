from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:root@localhost:5432/1stApp"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)  