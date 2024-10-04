from pydantic import BaseModel
import Ingredients

class Pantry(BaseModel):
    idPantry: str
    Ingredients: Ingredients    #Es una lista
    