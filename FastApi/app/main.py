"""Main module 
FastAPI: This is the main class from FastAPI, used to create the web application.
asynccontextmanager: Contextlib module is used to create asynchronous context managers.
connection: Imported from database, representing the database connection.
"""

from contextlib import asynccontextmanager

from helpers.auth import get_api_key
from config.database import database as connection
from config.database import UserModel

from starlette.responses import RedirectResponse
from routers.user import user_route
from fastapi import FastAPI, Depends

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
# Creates a FastAPI app instance and attaches the `lifespan` function.

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
# Defines a route for the root URL ("/") that redirects user to  page at "/docs".
