from pydantic import BaseModel
import Recipe
import Ingredients

class SuggestionRecipe(BaseModel):
    idSuggestionRecipe: int
    Recipe: Recipe
    Ingredients: Ingredients
