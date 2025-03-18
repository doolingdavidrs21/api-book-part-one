"""Database configuration"""
from requests import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from chapter3.complete.database import SQLALCHEMY_DATABASE_URL, SessionLocal


SQLALCHEMY_DATABASE_URL = "sqlite:///./fantasy_data.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,
                           bind=engine)

Base = declarative_base()