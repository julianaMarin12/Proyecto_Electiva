from pydantic import BaseModel
# This imports the `BaseModel` class from the `pydantic` library, which allows the creation of data models with built-in validation.

class Pantry(BaseModel):
    # This defines a class named `Pantry` that inherits from `BaseModel`. This class represents the Pydantic model for a pantry.

    idPantry: int
    # This is a class attribute (field) named `idPantry`, which holds the unique identifier for the pantry. It is expected to be of type `int` (integer).
 