from dotenv import load_dotenv
from peewee import *
from models.Cluster import Clusters
from models.Ingredients import Ingredients
from models.CategoryIngredients import CategoryIngredients
from models.Recipe import Recipe
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
    username = CharField(max_length=50)
    email = CharField(max_length=50)
    password = CharField(max_length=50)
    idClusters = ForeignKeyField(Clusters, backref='users')
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
    idIngredients = ForeignKeyField(Ingredients, backref='recipe')
    nutrients = CharField(max_length=50)
    calories = IntegerField(max_length = 50)

    class Meta:
        database = database
        table_name = "recipe"


class IngredientsModel(Model):
    idIngredients = AutoField(primary_key = True)
    nameIngredients = CharField(max_length=50)
    amount = CharField(max_length=50)
    idCategoryIngredients = ForeignKeyField(CategoryIngredients, backref='Ingredients')

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
    idRecipe = ForeignKeyField(Recipe, backref='suggestionRecipe')
    idIngredients = ForeignKeyField(Ingredients, backref='suggestionRecipe')

    class Meta:
        database = database
        table_name = "suggestionRecipe"


class PantryModel(Model):
    idPantry = AutoField(primary_key = True)
    idIngredients = ForeignKeyField(Ingredients, backref='pantry')

    class Meta:
        database = database
        table_name = "pantry"


class CategoryRecipeModel(Model):
    idCategoryRecipe = AutoField(primary_key = True)
    nameCategoryRecipe = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "categoryRecipe"

class NotificationModel(Model):
    idNotification = AutoField(primary_key = True)
    notificationType = CharField(max_length=50)
    message = CharField(max_length=50)
    shippingDate = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "notification"

        
class MenuModel(Model):
    idMenu = AutoField(primary_key = True)
    day = CharField(max_length=50)
    starTime = CharField(max_length=50)
    endTime = CharField(max_length=50)
    category = CharField(max_length=50)
    idRecipe = ForeignKeyField(Recipe, backref='menu')


    class Meta:
        database = database
        table_name = "menu"


class BuyListModel(Model):
    idBuys = AutoField(primary_key = True)
    category = CharField(max_length=50)
    purchaseDate = CharField(max_length=50)
    idIngredients = ForeignKeyField(Ingredients, backref='buysList')

    class Meta:
        database = database
        table_name = "buysList"



'''

class ShoppingList_Ingredient(Model):
    """
    Represents a table bridge between the shopping list and the ingredient in the database.
    
    Attributes:
        shoppingListId (int): The unique identifier of the shopping list.
        ingredientId (int): The unique identifier of the ingredient.
    """
    shoppingListId = ForeignKeyField(ShoppingList, backref='shopping_list_ingredients')
    ingredientId = ForeignKeyField(Ingredient, backref='shopping_list_ingredients')

    class Meta:
        """Defines the metadata for the ShoppingList_Ingredient model."""
        database = database
        db_table = "shopping_list_ingredients"

'''