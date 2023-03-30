from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:postgres@192.168.29.143/api_learn_db')

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()