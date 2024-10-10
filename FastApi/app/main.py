from fastapi import FastAPI, Depends
# Imports the `FastAPI` class to create the API application and `Depends` for dependency injection.
from starlette.responses import RedirectResponse
# Imports `RedirectResponse` from Starlette to handle HTTP redirects.
from contextlib import asynccontextmanager
# Imports `asynccontextmanager` to manage asynchronous resource setup and teardown.
from config.database import database as connection
# Imports the `database` connection object from the config module and aliases it as `connection`.
from helpers.auth import get_api_key
# Imports the `get_api_key` function from the helpers.auth module, which handles API key authentication.
from routers.user import user_route
# Imports `user_route`, which contains user-related routes (e.g., user registration, login).
from config.database import UserModel
# Imports the `UserModel` class from the database config, representing the user table in the database.

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manages the lifespan of the FastAPI app, handling database connections and disconnections.
    """
    if connection.is_closed():
        connection.connect()
        # Opens the database connection if it's currently closed.

        connection.create_tables([UserModel])
        # Creates the `UserModel` table in the database if it doesn't already exist.

    try:
        yield
        # The `try` block allows the app to run while the database connection is active.

    finally:
        if not connection.is_closed():
            connection.close()
            # Ensures the database connection is properly closed when the app shuts down.

app = FastAPI(lifespan=lifespan)
# Creates a FastAPI app instance and attaches the `lifespan` function to manage the app’s startup and shutdown.

app.include_router(
    user_route, 
    prefix="/api/user", 
    tags=["users"], 
    dependencies=[Depends(get_api_key)],
)
# Includes the `user_route` router for handling user-related API routes.
# The routes will be prefixed with `/api/user`.
# The `get_api_key` dependency is used to authenticate requests based on API keys.

@app.get("/")
def read_root():
    """
    Redirects the root URL ("/") to the API documentation page ("/docs").
    """
    return RedirectResponse(url="/docs")
# Defines a route for the root URL ("/") that redirects users to the FastAPI documentation page at "/docs".
