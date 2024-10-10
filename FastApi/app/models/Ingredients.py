from pydantic import BaseModel
# This imports the `BaseModel` class from the `pydantic` library for creating data models with automatic validation.

class Ingredients(BaseModel):
    # This defines a class named `Ingredients` that inherits from `BaseModel`. The class represents a model for ingredients.

    idIngredients: int
    # This is a class attribute named `idIngredients`, which holds the unique identifier for the ingredient. It must be of type `int` (integer).

    nameIngredients: str
    # This is a class attribute named `nameIngredients`, which holds the name of the ingredient. It must be of type `str` (string).

    amount: int
    # This is a class attribute named `amount`, which represents the quantity of the ingredient. It must be of type `int` (integer).
