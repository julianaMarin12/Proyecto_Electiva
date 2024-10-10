from peewee import Model, MySQLDatabase, AutoField, CharField, IntegerField, ForeignKeyField
# This imports necessary classes and functions from the `peewee` ORM library for defining database models.
# - `Model`: Base class for all models.
# - `MySQLDatabase`: Class for connecting to a MySQL database.
# - `AutoField`: A primary key field that auto-increments.
# - `CharField`: A field for storing strings (text data).
# - `IntegerField`: A field for storing integers.
# - `ForeignKeyField`: A field that creates a foreign key relationship between models.

from config.settings import DATABASE
# This imports the `DATABASE` configuration from the settings module.

database = MySQLDatabase(
    DATABASE["name"],
    user=DATABASE["user"],
    passwd=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"],
)
# This creates a connection to the MySQL database using the settings defined in the `DATABASE` dictionary.
# It retrieves the database name, user, password, host, and port from the configuration.

class ClustersModel(Model):
    idClusters = AutoField(primary_key=True)
    # Defines an auto-incrementing primary key for the `ClustersModel`.

    nameClusters = CharField(max_length=50)
    # Defines a character field for the cluster name with a maximum length of 50 characters.

    amount = CharField(max_length=50)
    # Defines a character field for the amount associated with the cluster.

    class Meta:
        database = database
        table_name = "clusters"
    # Specifies that this model uses the defined database connection and maps to the "clusters" table.

class UserModel(Model):
    idUser = AutoField(primary_key=True)
    # Defines an auto-incrementing primary key for the `UserModel`.

    name = CharField(max_length=50, unique=True)
    # Defines a unique character field for the user's name, limited to 50 characters.

    email = CharField(max_length=50)
    # Defines a character field for the user's email, limited to 50 characters.

    password = CharField(max_length=50)
    # Defines a character field for the user's password, limited to 50 characters.

    photoProfile = CharField(max_length=50)
    # Defines a character field for the user's profile photo URL or path, limited to 50 characters.

    class Meta:
        database = database
        table_name = "users"
    # Specifies that this model uses the defined database connection and maps to the "users" table.

class CategoryIngredientsModel(Model):
    idCategoryIngredients = AutoField(primary_key=True)
    # Defines an auto-incrementing primary key for the `CategoryIngredientsModel`.

    nameCategoryIngredients = CharField(max_length=50)
    # Defines a character field for the category name of ingredients, limited to 50 characters.

    class Meta:
        database = database
        table_name = "categoryIngredients"
    # Specifies that this model uses the defined database connection and maps to the "categoryIngredients" table.

class IngredientsModel(Model):
    idIngredients = AutoField(primary_key=True)
    # Defines an auto-incrementing primary key for the `IngredientsModel`.

    nameIngredients = CharField(max_length=50)
    # Defines a character field for the ingredient name, limited to 50 characters.

    amount = CharField(max_length=50)
    # Defines a character field for the amount of the ingredient, limited to 50 characters.

    idCategoryIngredients = ForeignKeyField(CategoryIngredientsModel, backref='Ingredients')
    # Defines a foreign key field that links to the `CategoryIngredientsModel`, creating a relationship between ingredients and their category.

    class Meta:
        database = database
        table_name = "ingredients"
    # Specifies that this model uses the defined database connection and maps to the "ingredients" table.

class RecipeModel(Model):
    idRecipe = AutoField(primary_key=True)
    # Defines an auto-incrementing primary key for the `RecipeModel`.

    nameRecipe = CharField(max_length=50)
    # Defines a character field for the recipe name, limited to 50 characters.

    instructions = CharField(max_length=50)
    # Defines a character field for the recipe instructions, limited to 50 characters.

    timePreparation = CharField(max_length=50)
    # Defines a character field for the preparation time, limited to 50 characters.

    difficulty = CharField(max_length=50)
    # Defines a character field for the recipe's difficulty level, limited to 50 characters.

    category = CharField(max_length=50)
    # Defines a character field for the category of the recipe, limited to 50 characters.

    idIngredients = ForeignKeyField(IngredientsModel, backref='recipe')
    # Defines a foreign key field that links to the `IngredientsModel`, establishing a relationship between recipes and their ingredients.

    nutrients = CharField(max_length=50)
    # Defines a character field for the nutritional information, limited to 50 characters.

    calories = IntegerField()
    # Defines an integer field for the calorie count of the recipe.

    class Meta:
        database = database
        table_name = "recipe"
    # Specifies that this model uses the defined database connection and maps to the "recipe" table.

class SuggestionRecipeModel(Model):
    idSuggestionRecipe = AutoField(primary_key=True)
    # Defines an auto-incrementing primary key for the `SuggestionRecipeModel`.

    idRecipe = ForeignKeyField(RecipeModel, backref='suggestionRecipe')
    # Defines a foreign key field that links to the `RecipeModel`, establishing a relationship between suggestions and recipes.

    idIngredients = ForeignKeyField(IngredientsModel, backref='suggestionRecipe')
    # Defines a foreign key field that links to the `IngredientsModel`, establishing a relationship between suggestions and ingredients.

    class Meta:
        database = database
        table_name = "suggestionRecipe"
    # Specifies that this model uses the defined database connection and maps to the "suggestionRecipe" table.

class PantryModel(Model):
    idPantry = AutoField(primary_key=True)
    # Defines an auto-incrementing primary key for the `PantryModel`.

    idIngredients = ForeignKeyField(IngredientsModel, backref='pantry')
    # Defines a foreign key field that links to the `IngredientsModel`, establishing a relationship between the pantry and ingredients.

    class Meta:
        database = database
        table_name = "pantry"
    # Specifies that this model uses the defined database connection and maps to the "pantry" table.

class CategoryRecipeModel(Model):
    idCategoryRecipe = AutoField(primary_key=True)
    # Defines an auto-incrementing primary key for the `CategoryRecipeModel`.

    nameCategoryRecipe = CharField(max_length=50)
    # Defines a character field for the recipe category name, limited to 50 characters.

    class Meta:
        database = database
        table_name = "categoryRecipe"
    # Specifies that this model uses the defined database connection and maps to the "categoryRecipe" table.

class NotificationModel(Model):
    idNotification = AutoField(primary_key=True)
    # Defines an auto-incrementing primary key for the `NotificationModel`.

    notificationType = CharField(max_length=50)
    # Defines a character field for the type of notification, limited to 50 characters.

    message = CharField(max_length=50)
    # Defines a character field for the notification message, limited to 50 characters.

    shippingDate = CharField(max_length=50)
    # Defines a character field for the date the notification is sent, limited to 50 characters.

    class Meta:
        database = database
        table_name = "notification"
    # Specifies that this model uses the defined database connection and maps to the "notification" table.

class MenuModel(Model):
    idMenu = AutoField(primary_key=True)
    # Defines an auto-incrementing primary key for the `MenuModel`.

    day = CharField(max_length=50)
    # Defines a character field for the day associated with the menu, limited to 50 characters.

    starTime = CharField(max_length=50)  # Note: This should be corrected to 'startTime'
    # Defines a character field for the start time of the menu, limited to 50 characters.

    endTime = CharField(max_length=50)
    # Defines a character field for the end time of the menu, limited to 50 characters.

    category = CharField(max_length=50)
    # Defines a character field for the category of the menu, limited to 50 characters.

    idRecipe = ForeignKeyField(RecipeModel, backref='menu')
    # Defines a foreign key field that links to the `RecipeModel`, establishing a relationship between the menu and recipes.

    class Meta:
        database = database
        table_name = "menu"
    # Specifies that this model uses the defined database connection and maps to the "menu" table.

class BuyListModel(Model):
    idBuys = AutoField(primary_key=True)
    # Defines an auto-incrementing primary key for the `BuyListModel`.

    category = CharField(max_length=50)
    # Defines a character field for the category of items in the buy list, limited to 50 characters.

    purchaseDate = CharField(max_length=50)
    # Defines a character field for the purchase date, limited to 50 characters.

    idIngredients = ForeignKeyField(IngredientsModel, backref='buysList')
    # Defines a foreign key field that links to the `IngredientsModel`, establishing a relationship between the buy list and ingredients.

    class Meta:
        database = database
        table_name = "buysList"
    # Specifies that this model uses the defined database connection and maps to
