from pydantic import BaseModel
# This imports the `BaseModel` class from the `pydantic` library. All Pydantic models must inherit from this class to enable automatic data validation and serialization.

class Recipe(BaseModel):
    # This defines a class named `Recipe` that inherits from `BaseModel`. This class represents the model for a recipe.

    idRecipe: int
    # This is a class attribute (field) named `idRecipe`, which holds the unique identifier for the recipe. It must be of type `int` (integer).

    nameRecipe: str
    # This is a class attribute named `nameRecipe`, which holds the name of the recipe. It must be of type `str` (string).

    instructions: str
    # This is a class attribute named `instructions`, which contains the cooking instructions or steps to prepare the recipe. It must be a string.

    timePreparation: int
    # This is a class attribute named `timePreparation`, which represents the time required to prepare the recipe. It must be of type `int` (integer), typically measured in minutes.

    difficulty: str
    # This is a class attribute named `difficulty`, which specifies the difficulty level of the recipe (e.g., "easy", "medium", "hard"). It must be of type `str` (string).

    category: str
    # This is a class attribute named `category`, which describes the type or category of the recipe (e.g., "dessert", "main course"). It must be of type `str`.

    nutrients: str
    # This is a class attribute named `nutrients`, which describes the nutritional content of the recipe (e.g., "high protein", "low fat"). It must be a string.

    calories: int
    # This is a class attribute named `calories`, which specifies the total number of calories in the recipe. It must be of type `int` (integer).
