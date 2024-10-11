"""
This module defines the Pydantic model for a categoryRecipe.
"""
from pydantic import BaseModel

class CategoryRecipe(BaseModel):
    """
    This defines a Pydantic model for a categoryRecipe.
    """

    idCategoryRecipe: int
    nameCategoryRecipe: str
