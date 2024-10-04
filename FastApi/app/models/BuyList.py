from pydantic import BaseModel, date
import Ingredients

class BuyList(BaseModel):
    idBuys: int
    category: str 
    purchaseDate: date
    Ingredients: Ingredients    #Es una lista

