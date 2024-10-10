"""
This module defines the routes for user-related operations in the FastAPI application.
Routes:
    - POST /users/: Create a new user.
    - GET /users: Retrieve a list of all users.
    - GET /{idUser}: Retrieve a specific user by their ID.
    - PUT /{idUser}: Update a specific user by their ID.
    - DELETE /{idUser}: Delete a specific user by their ID.
Functions:
    - create_users(user: User): Creates a new user with the provided details.
    - get_users(): Retrieves a list of all users from the database.
    - get_user(idUser: int): Retrieves a specific user by their ID. 
      Returns an error message if the user is not found.
    - update_useridUser: int, user: User): Updates a specific user by their ID.
    - delete_user(idUser int): Deletes a specific user by their ID.
Dependencies:
    - UserModel: The database model for users.
    - User: The Pydantic model for user data validation.
    - APIRouter: FastAPI router for defining routes.
    - Body: FastAPI dependency for parsing request bodies.
"""

from fastapi import APIRouter, Body

from config.database import UserModel
from models.User import User

user_route = APIRouter()

@user_route.post("/users/")
def create_users(user: User = Body(...)):
    """
    Create a new user.

    Args:
        user (User): The user object containing the name, email,
        password and photo profile.

    Returns:
        None
    """
    UserModel.create(
        name=user.name,
        email=user.email,
        password=user.password,
        photoProfile=user.photoProfile,
    )
    return {"message": "User created successfully"}

    
@user_route.get("/users")
def get_users():
    """
    Retrieve a list of users from the database.

    This function queries the UserModel to select all users with an ID greater than 0,
    converts the result to a dictionary format, and returns it as a list.

    Returns:
        list: A list of dictionaries, each representing a user.
    """
    user = UserModel.select().where(UserModel.idUser > 0).dicts()
    return list(user)

@user_route.get("/{idUser}")
def get_user(id_user: int):
    """
    Retrieve a user by their ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        UserModel: The user object if found.
        dict: An error message if the user is not found.
    """
    try:
        user = UserModel.get(UserModel.idUser == id_user)
        return user
    except UserModel.DoesNotExist:
        return {"error": "User not found"}
    
@user_route.put("/{idUser}")
def update_user(idUser: int, user: User = Body(...)):
    """
    Update a user by their ID.

    Args:
        user_id (int): The ID of the user to update.
        user (User): The user object containing the updated details.

    Returns:
        None
    """
    UserModel.update(
        name=user.name,
        password=user.password,
        photoProfile=user.photoProfile,
    ).where(UserModel.idUser == idUser).execute()
    return {"message": "User updated successfully"}

@user_route.delete("/{idUser}")
def delete_user(id_user: int):
    """
    Delete a user by their ID.

    Args:
        idUser (int): The ID of the user to delete.

    Returns:
        None
    """
    UserModel.delete().where(UserModel.idUser == id_user).execute()
    return {"message": "User deleted successfully"}


