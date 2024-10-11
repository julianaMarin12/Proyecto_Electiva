"""
This module defines the Pydantic model for a buyList.
"""
from pydantic import BaseModel, date

class BuyList(BaseModel):
    """
    Pydantic model for a buyList.
    """

    idBuys: int
    category: str
    purchaseDate: date
