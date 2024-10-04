from pydantic import BaseModel

class CategoryRecipe(BaseModel):
    idCategoryRecipe: int
    nameCategoryRecipe: str