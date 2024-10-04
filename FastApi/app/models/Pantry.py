from pydantic import BaseModel
import Ingredients

class Pantry(BaseModel):
    idPantry: int
    Ingredients: Ingredients    #Es una lista
    