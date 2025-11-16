# backend/db/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_PATH = os.path.join(os.path.dirname(__file__), "../../data/pipeline.db")
DB_URI = f"sqlite:///{os.path.abspath(DB_PATH)}"

engine = create_engine(DB_URI, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
