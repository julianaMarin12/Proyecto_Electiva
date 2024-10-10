"""
This module loads environment variables and sets up the database configuration 
based on the current environment (development or production).
"""

import os
#This imports the `os` module, which provides functions to interact with the operating system (e.g., accessing environment variables).

from dotenv import load_dotenv
#This imports the `load_dotenv` function from the `dotenv` library, which is used to load environment variables from a `.env` file.

load_dotenv()
#This loads the environment variables from the `.env` file into the current application's environment.

ENV = os.getenv("ENV", "dev")
#This retrieves the value of the `ENV` environment variable. If the variable is not set, it defaults to "dev". 
#`ENV` is typically used to distinguish between different application environments (e.g., development, production).

if ENV == "production":
    # This checks if the environment (`ENV`) is set to "production".  
    DATABASE = {
        "name": os.getenv("MYSQL_DATABASE"),
        # Retrieves the MySQL database name from the `MYSQL_DATABASE` environment variable.

        "engine": "peewee.MySQLDatabase",
        # Specifies that the database engine being used is `peewee.MySQLDatabase`.

        "user": os.getenv("MYSQL_USER"),
        # Retrieves the MySQL username from the `MYSQL_USER` environment variable.

        "password": os.getenv("MYSQL_PASSWORD"),
        # Retrieves the MySQL password from the `MYSQL_PASSWORD` environment variable.

        "host": os.getenv("MYSQL_HOST"),
        # Retrieves the MySQL host from the `MYSQL_HOST` environment variable.

        "port": int(os.getenv("MYSQL_PORT")),
       # Retrieves the MySQL port from the `MYSQL_PORT` environment variable, casting it to an integer.
    }
else:
   # If the environment is not set to "production" (e.g., it's in development), this block is executed.
   
    DATABASE = {
        "name": os.getenv("MYSQL_DATABASE"),
       # Retrieves the MySQL database name from the `MYSQL_DATABASE` environment variable, just like in the production block.

        "engine": "peewee.MySQLDatabase",
        # Specifies the `peewee.MySQLDatabase` engine.

        "user": os.getenv("MYSQL_USER"),
        # Retrieves the MySQL username from the `MYSQL_USER` environment variable.

        "password": os.getenv("MYSQL_PASSWORD"),
        # Retrieves the MySQL password from the `MYSQL_PASSWORD` environment variable.

        "host": os.getenv("MYSQL_HOST"),
        # Retrieves the MySQL host from the `MYSQL_HOST` environment variable.

        "port": int(os.getenv("MYSQL_PORT")),
       # Retrieves the MySQL port from the `MYSQL_PORT` environment variable, casting it to an integer.
    }
