from pydantic import BaseModel
# This imports the `BaseModel` class from the `pydantic` library, which provides data validation and model creation.

class CategoryIngredients(BaseModel):
    # This defines a class named `CategoryIngredients` that inherits from `BaseModel`. This class represents a model for an ingredient category.

    idCategoryIngredients: int
    # This is a class attribute named `idCategoryIngredients`, which holds the unique identifier for the ingredient category. It must be of type `int` (integer).

    nameCategoryIngredients: str
    # This is a class attribute named `nameCategoryIngredients`, which holds the name of the ingredient category (e.g., "spices", "vegetables"). It must be of type `str` (string).
