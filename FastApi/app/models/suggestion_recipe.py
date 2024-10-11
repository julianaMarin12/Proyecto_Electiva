"""
This module defines the Pydantic model for aggestionRecipe.
"""

from pydantic import BaseModel

class SuggestionRecipe(BaseModel):
    """
    This class represents a suggestion recipe Pydantic model.
    """
    idSuggestionRecipe: int
