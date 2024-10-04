from pydantic import BaseModel
import Ingredients

class BuyList(BaseModel):
    idBuys: str
    category: str 
    purchaseDate: str   #Es una fecha
    Ingredients: Ingredients    #Es una lista

