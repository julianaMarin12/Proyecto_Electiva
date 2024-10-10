from pydantic import BaseModel
# This imports the `BaseModel` class from the `pydantic` library, which allows for the creation of data models with validation.

class CategoryRecipe(BaseModel):
    # This defines a class named `CategoryRecipe` that inherits from `BaseModel`. The class represents a model for a recipe category.

    idCategoryRecipe: int
    # This is a class attribute named `idCategoryRecipe`, which holds the unique identifier for the recipe category. It must be of type `int` (integer).

    nameCategoryRecipe: str
    # This is a class attribute named `nameCategoryRecipe`, which holds the name of the recipe category (e.g., "dessert", "main course"). It must be of type `str` (string).
