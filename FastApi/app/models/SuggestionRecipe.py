from pydantic import BaseModel
import Recipe
import Ingredients

class SuggestionRecipe(BaseModel):
    idSuggestionRecipe: str
    Recipe: Recipe
    Ingredients: Ingredients
