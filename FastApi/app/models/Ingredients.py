from pydantic import BaseModel

class Ingredients(BaseModel):
    idIngredients: int
    nameIngredients: str
    amount: int