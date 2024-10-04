from dotenv import load_dotenv
from peewee import *
import os

load_dotenv()

database = MySQLDatabase(
    os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST')
)

class UserModel(Model):
    idUsers = AutoField(primary_key = True)
    nameUsers = CharField(max_length=50)
    email = CharField(max_length=50)
    password = CharField(max_length=50)
    # Falta la relacion con la tabla de clusters
    photoProfile = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "users"


class RecipeModel(Model):
    idRecipe = AutoField(primary_key = True)
    nameRecipe = CharField(max_length=50)
    instructions = CharField(max_length=50)
    timePreparation = CharField(max_length=50)
    difficulty = CharField(max_length=50)
    category = CharField(max_length=50)
    # Falta la relacion con la tabla de ingredients
    nutrients = CharField(max_length=50)
    calories = IntegerField(max_length = 50)

    class Meta:
        database = database
        table_name = "recipe"


class IngredientsModel(Model):
    idIngredients = AutoField(primary_key = True)
    nameIngredients = CharField(max_length=50)
    amount = CharField(max_length=50)
    # Falta la relacion con la tabla CategoryIngredients

    class Meta:
        database = database
        table_name = "ingredients"


class CategoryIngredientsModel(Model):
    idCategoryIngredients = AutoField(primary_key = True)
    nameCategoryIngredients = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "categoryIngredients"


class ClustersModel(Model):
    idClusters = AutoField(primary_key = True)
    nameClusters = CharField(max_length=50)
    amount = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "clusters"


class SuggestionRecipeModel(Model):
    idSuggestionRecipe = AutoField(primary_key = True)
    # Falta la relacion con la tabla Recipe
    # Falta la relacion con la tabla Ingredients

    class Meta:
        database = database
        table_name = "suggestionRecipe"


class PantryModel(Model):
    idPantry = AutoField(primary_key = True)
    # Falta la relacion con la tabla Ingredients

    class Meta:
        database = database
        table_name = "suggestionRecipe"


class CategoryRecipeModel(Model):
    idCategoryRecipe = AutoField(primary_key = True)
    nameCategoryRecipe = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "categoryRecipe"