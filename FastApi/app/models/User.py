"""
This module defines the Pydantic model for a user.
"""

from pydantic import BaseModel

class User(BaseModel):
    """
    Pydantic model for a user.
    """

    idUsers: int
    name: str
    email: str
    password: str
    photoProfile: str
