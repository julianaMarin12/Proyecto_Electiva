from pydantic import BaseModel
import CategoryIngredients

class Ingredients(BaseModel):
    idIngredients: str
    nameIngredients: str
    amount: int
    CategoryIngredients: CategoryIngredients