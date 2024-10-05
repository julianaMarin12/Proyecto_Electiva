from pydantic import BaseModel, date

class BuyList(BaseModel):
    idBuys: int
    category: str 
    purchaseDate: date

