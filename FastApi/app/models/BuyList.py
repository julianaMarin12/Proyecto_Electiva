from pydantic import BaseModel, date
# This imports the `BaseModel` class from the `pydantic` library for model creation and the `date` type for handling date fields.

class BuyList(BaseModel):
    # This defines a class named `BuyList` that inherits from `BaseModel`. This class represents a model for a buying list.

    idBuys: int
    # This is a class attribute named `idBuys`, which holds the unique identifier for the buying list. It must be of type `int` (integer).

    category: str
    # This is a class attribute named `category`, which holds the category of the items in the buying list (e.g., "groceries", "electronics"). It must be of type `str` (string).

    purchaseDate: date
    # This is a class attribute named `purchaseDate`, which represents the date when the purchase was made. It uses the `date` type to ensure that it is a valid date.
