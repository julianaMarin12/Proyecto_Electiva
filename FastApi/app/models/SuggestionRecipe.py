from pydantic import BaseModel
# This imports the `BaseModel` class from the `pydantic` library. All Pydantic models must inherit from this base class to enable data validation and serialization.

class SuggestionRecipe(BaseModel):
    # This defines a class named `SuggestionRecipe` that inherits from `BaseModel`. The class represents a Pydantic model for a suggestion recipe.

    idSuggestionRecipe: int
    # This is a class attribute (field) named `idSuggestionRecipe`, which represents the unique ID of a suggestion recipe. It is expected to be of type `int` (integer).
