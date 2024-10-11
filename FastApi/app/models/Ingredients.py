"""
This module defines the Pydantic model for a ingredientes.
"""
from pydantic import BaseModel

class Ingredients(BaseModel):
    """
    This defines a class named `Ingredients` that inherits from `BaseModel`.
    The class represents a model for ingredients.
    """
    idIngredients: int
    nameIngredients: str
    amount: int
