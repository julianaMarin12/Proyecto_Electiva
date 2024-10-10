from dotenv import load_dotenv
from peewee import  Model, MySQLDatabase, AutoField, CharField, IntegerField,ForeignKeyField
import os

load_dotenv()
database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),  # The name of the MySQL database
    user=os.getenv("MYSQL_USER"),  # MySQL username
    passwd=os.getenv("MYSQL_PASSWORD"),  # MySQL password
    host=os.getenv("MYSQL_HOST")  # MySQL host (can be localhost or a remote server)
)

class ClustersModel(Model):
    idClusters = AutoField(primary_key = True)
    nameClusters = CharField(max_length=50)
    amount = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "clusters"

class UserModel(Model):
    idUser = AutoField(primary_key = True)
    name = CharField(max_length=50)
    email = CharField(max_length=50)
    password = CharField(max_length=50)
    photoProfile = CharField(max_length=50)
    idClusters = ForeignKeyField(ClustersModel, backref='users')

    class Meta:
        database = database
        table_name = "users"

class CategoryIngredientsModel(Model):
    idCategoryIngredients = AutoField(primary_key = True)
    nameCategoryIngredients = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "categoryIngredients"


class IngredientsModel(Model):
    idIngredients = AutoField(primary_key = True)
    nameIngredients = CharField(max_length=50)
    amount = CharField(max_length=50)
    idCategoryIngredients = ForeignKeyField(CategoryIngredientsModel, backref='Ingredients')

    class Meta:
        database = database
        table_name = "ingredients"

class RecipeModel(Model):
    idRecipe = AutoField(primary_key = True)
    nameRecipe = CharField(max_length=50)
    instructions = CharField(max_length=50)
    timePreparation = CharField(max_length=50)
    difficulty = CharField(max_length=50)
    category = CharField(max_length=50)
    idIngredients = ForeignKeyField(IngredientsModel, backref='recipe')
    nutrients = CharField(max_length=50)
    calories = IntegerField()

    class Meta:
        database = database
        table_name = "recipe"

class SuggestionRecipeModel(Model):
    idSuggestionRecipe = AutoField(primary_key = True)
    idRecipe = ForeignKeyField(RecipeModel, backref='suggestionRecipe')
    idIngredients = ForeignKeyField(IngredientsModel, backref='suggestionRecipe')

    class Meta:
        database = database
        table_name = "suggestionRecipe"


class PantryModel(Model):
    idPantry = AutoField(primary_key = True)
    idIngredients = ForeignKeyField(IngredientsModel, backref='pantry')

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
    idRecipe = ForeignKeyField(RecipeModel, backref='menu')


    class Meta:
        database = database
        table_name = "menu"


class BuyListModel(Model):
    idBuys = AutoField(primary_key = True)
    category = CharField(max_length=50)
    purchaseDate = CharField(max_length=50)
    idIngredients = ForeignKeyField(IngredientsModel, backref='buysList')

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