"""
This module contains the SQLAlchemy configuration for the FastAPI application.
It includes the database connection setup, engine configuration, and session creation
for interacting with the database.
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE

# Create a base class for the declarative models
Base = declarative_base()

class User(Base):
    """User model representing the users table."""
    __tablename__ = "users"  # Name of the table in the database
    idUser = Column(Integer, primary_key=True, index=True)  # Primary key with an index
    name = Column(String(50), unique=True, index=True)  # Unique username with a max length of 50.
    email = Column(String(100), unique=True, index=True)  # Unique email with a max length of 100.
    password = Column(String(255))  # User's password with a max length of 255
    photoProfile = Column(String(50))  # Profile photo path or URL with a max length of 50

class Post(Base):
    """Post model representing the posts table."""
    __tablename__ = "posts"  # Name of the table in the database
    id = Column(Integer, primary_key=True, index=True)  # Primary key with an index
    title = Column(String(50), index=True)  # Title of the post, indexed, with a max length of 50
    content = Column(String(50))  # Content of the post with a max length of 50
    user_id = Column(Integer)  # Foreign key referencing the user who created the post

# Define the database connection URL using the settings from the config
DATABASE_URL = f"mysql+pymysql://{DATABASE['user']}:{DATABASE['password']}@{DATABASE['host']}/{DATABASE['name']}"
engine = create_engine(DATABASE_URL)  # Create the engine to connect to the MySQL database

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# The session is not autocommitted or autoflushed; it needs manual control
