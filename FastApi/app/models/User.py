from pydantic import BaseModel
# This imports the `BaseModel` class from the `pydantic` library. `BaseModel` is the base class that all Pydantic models must inherit from.

class User(BaseModel):
    # This defines a class named `User` that inherits from `BaseModel`. It represents the Pydantic model for user-related data.

    idUsers: int
    # This is a class attribute (field) named `idUsers`, representing the user's unique ID. It's expected to be of type `int` (integer).

    name: str
    # This is a class attribute (field) named `name`, representing the user's name. It's expected to be of type `str` (string).

    email: str
    # This is a class attribute (field) named `email`, representing the user's email address. It's expected to be of type `str`.

    password: str
    # This is a class attribute (field) named `password`, representing the user's password. It's expected to be of type `str`.

    photoProfile: str
    # This is a class attribute (field) named `photoProfile`, representing the URL or file path to the user's profile picture. It's expected to be of type `str`.
