from pydantic import BaseModel
import Ingredients

class Recipe(BaseModel):
    idRecipe: str
    nameRecipe: str
    instructions: str
    timePreparation: int
    difficulty: str
    category: str
    Ingredients: Ingredients    #Es una lista
    nutrients: str
    calories: int