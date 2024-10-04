from pydantic import BaseModel
import CategoryIngredients

class Ingredients(BaseModel):
    idIngredients: int
    nameIngredients: str
    amount: int
    CategoryIngredients: CategoryIngredients