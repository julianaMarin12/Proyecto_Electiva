"""
    This imports classes and functions from the `peewee` ORM library for defining database.
     `Model`: Base class for all models.
     `MySQLDatabase`: Class for connecting to a MySQL database.
     `AutoField`: A primary key field that auto-increments.
     `CharField`: A field for storing strings (text data).
     `IntegerField`: A field for storing integers.
     `ForeignKeyField`: A field that creates a foreign key relationship between models.
"""
from peewee import Model, MySQLDatabase, AutoField, CharField, IntegerField, ForeignKeyField

"""
    This imports the `DATABASE` configuration from the settings module.
"""
from config.settings import DATABASE

# Create the connection to the MySQL database using the settings in the config file
database = MySQLDatabase(
    DATABASE["name"],
    user=DATABASE["user"],
    passwd=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"],
)

class ClustersModel(Model):
    """Model to represent clusters."""
    idClusters = AutoField(primary_key=True)  # Auto-incrementing primary key
    nameClusters = CharField(max_length=50)  # Cluster name, limited to 50 characters
    amount = CharField(max_length=50)  # Amount, limited to 50 characters

    class Meta:
        """Meta options for ClustersModel."""
        database = database  # Use the connected database
        table_name = "clusters"  # Table name in the database

class UserModel(Model):
    """Model to represent users."""
    idUser = AutoField(primary_key=True)  # Auto-incrementing primary key
    name = CharField(max_length=50, unique=True)  # User name, unique and max 50 characters
    email = CharField(max_length=50)  # User email, max 50 characters
    password = CharField(max_length=50)  # User password, max 50 characters
    photoProfile = CharField(max_length=50)  # User profile picture path or URL

    class Meta:
        """Meta options for UserModel."""
        database = database  # Use the connected database
        table_name = "users"  # Table name in the database

class CategoryIngredientsModel(Model):
    """Model to represent ingredient categories."""
    idCategoryIngredients = AutoField(primary_key=True)  # Auto-incrementing primary key
    nameCategoryIngredients = CharField(max_length=50)  # Category name, max 50 characters

    class Meta:
        """Meta options for CategoryIngredientsModel."""
        database = database  # Use the connected database
        table_name = "categoryIngredients"  # Table name in the database

class IngredientsModel(Model):
    """Model to represent ingredients."""
    idIngredients = AutoField(primary_key=True)  # Auto-incrementing primary key
    nameIngredients = CharField(max_length=50)  # Ingredient name, max 50 characters
    amount = CharField(max_length=50)  # Amount of ingredient, max 50 characters
    idCategoryIngredients = ForeignKeyField(CategoryIngredientsModel, backref='Ingredients')  
    # Foreign key to the ingredient category

    class Meta:
        """Meta options for IngredientsModel."""
        database = database  # Use the connected database
        table_name = "ingredients"  # Table name in the database

class RecipeModel(Model):
    """Model to represent recipes."""
    idRecipe = AutoField(primary_key=True)  # Auto-incrementing primary key
    nameRecipe = CharField(max_length=50)  # Recipe name, max 50 characters
    instructions = CharField(max_length=50)  # Instructions for the recipe
    timePreparation = CharField(max_length=50)  # Time needed to prepare the recipe
    difficulty = CharField(max_length=50)  # Difficulty level of the recipe
    category = CharField(max_length=50)  # Recipe category, max 50 characters
    idIngredients = ForeignKeyField(IngredientsModel, backref='recipe')  
    # Foreign key to ingredients used in the recipe
    nutrients = CharField(max_length=50)  # Nutritional information
    calories = IntegerField()  # Number of calories in the recipe

    class Meta:
        """Meta options for RecipeModel."""
        database = database  # Use the connected database
        table_name = "recipe"  # Table name in the database

class SuggestionRecipeModel(Model):
    """Model to represent recipe suggestions."""
    idSuggestionRecipe = AutoField(primary_key=True)  # Auto-incrementing primary key
    idRecipe = ForeignKeyField(RecipeModel, backref='suggestionRecipe')  # Foreign key to recipe
    idIngredients = ForeignKeyField(IngredientsModel, backref='suggestionRecipe')  
    # Foreign key to ingredients for suggestions

    class Meta:
        """Meta options for SuggestionRecipeModel."""
        database = database  # Use the connected database
        table_name = "suggestionRecipe"  # Table name in the database

class PantryModel(Model):
    """Model to represent the pantry."""
    idPantry = AutoField(primary_key=True)  # Auto-incrementing primary key
    idIngredients = ForeignKeyField(IngredientsModel, backref='pantry')  # Foreign key to ingredients in the pantry

    class Meta:
        """Meta options for PantryModel."""
        database = database  # Use the connected database
        table_name = "pantry"  # Table name in the database

class CategoryRecipeModel(Model):
    """Model to represent recipe categories."""
    idCategoryRecipe = AutoField(primary_key=True)  # Auto-incrementing primary key
    nameCategoryRecipe = CharField(max_length=50)  # Recipe category name, max 50 characters

    class Meta:
        """Meta options for CategoryRecipeModel."""
        database = database  # Use the connected database
        table_name = "categoryRecipe"  # Table name in the database

class NotificationModel(Model):
    """Model to represent notifications."""
    idNotification = AutoField(primary_key=True)  # Auto-incrementing primary key
    notificationType = CharField(max_length=50)  # Type of notification, max 50 characters
    message = CharField(max_length=50)  # Notification message, max 50 characters
    shippingDate = CharField(max_length=50)  # Date the notification was sent, max 50 characters

    class Meta:
        """Meta options for NotificationModel."""
        database = database  # Use the connected database
        table_name = "notification"  # Table name in the database

class MenuModel(Model):
    """Model to represent menus."""
    idMenu = AutoField(primary_key=True)  # Auto-incrementing primary key
    day = CharField(max_length=50)  # Day associated with the menu
    starTime = CharField(max_length=50)  # Start time for the menu (note: typo, should be startTime)
    endTime = CharField(max_length=50)  # End time for the menu
    category = CharField(max_length=50)  # Menu category
    idRecipe = ForeignKeyField(RecipeModel, backref='menu')  # Foreign key to the recipe associated with the menu

    class Meta:
        """Meta options for MenuModel."""
        database = database  # Use the connected database
        table_name = "menu"  # Table name in the database

class BuyListModel(Model):
    """Model to represent shopping lists."""
    idBuys = AutoField(primary_key=True)  # Auto-incrementing primary key
    category = CharField(max_length=50)  # Category of items in the shopping list
    purchaseDate = CharField(max_length=50)  # Date of purchase
    idIngredients = ForeignKeyField(IngredientsModel, backref='buysList')  
    # Foreign key to ingredients in the shopping list

    class Meta:
        """Meta options for BuyListModel."""
        database = database  # Use the connected database
        table_name = "buysList"  # Table name in the database
