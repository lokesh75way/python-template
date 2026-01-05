from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# 3.7 Database Integration
# 3.7 SQLAlchemy ORM (sync & async)
# We are using Sync SQLAlchemy here for simplicity, but FastAPI supports async too.
# For PostgreSQL: ensure DATABASE_URL starts with postgresql://
SQLACHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")

# 3.7 Raw SQL when required
# create_engine connects to the database.
engine = create_engine(
    SQLACHEMY_DATABASE_URL
)

# 3.7 Transaction handling (Implicit in Session usage)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
