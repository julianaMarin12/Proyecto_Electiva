from pydantic import BaseModel

class Recipe(BaseModel):
    idRecipe: int
    nameRecipe: str
    instructions: str
    timePreparation: int
    difficulty: str
    category: str
    nutrients: str
    calories: int