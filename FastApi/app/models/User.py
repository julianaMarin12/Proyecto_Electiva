"""This module defines the Pydantic  model for users"""

from pydantic import BaseModel

class User(BaseModel):
    """Pydantic model for users"""
    idUsers: int
    name: str
    email: str
    password: str
    photoProfile: str
