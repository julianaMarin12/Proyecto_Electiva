"""
This module defines the Pydantic model for a pantry.
"""
from pydantic import BaseModel

class Pantry(BaseModel):
    """
    This class represents a Pydantic model for a pantry.
    """
    idPantry: int
 