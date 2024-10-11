"""
This module defines the Pydantic model for a Recipe.
"""
from pydantic import BaseModel

class Recipe(BaseModel):
    """
    Pydantic model for a recipe.
    """
    idRecipe: int
    nameRecipe: str
    instructions: str
    timePreparation: int
    difficulty: str
    category: str
    nutrients: str
    calories: int
