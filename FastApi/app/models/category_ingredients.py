"""
This module defines the Pydantic model for a categoryIngredients.
"""
from pydantic import BaseModel

class CategoryIngredients(BaseModel):
    """
    This class represents a model for an ingredient category.
    """

    idCategoryIngredients: int
    nameCategoryIngredients: str
