from pydantic import BaseModel

class CategoryRecipe(BaseModel):
    idCategoryRecipe: str
    nameCategoryRecipe: str