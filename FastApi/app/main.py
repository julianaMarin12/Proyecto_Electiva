

from fastapi import FastAPI,Depends
from starlette.responses import RedirectResponse

from contextlib import asynccontextmanager
from config.database import database as connection

from helpers.auth import get_api_key
from routers.user import user_route




@asynccontextmanager
async def lifespan(app: FastAPI):
    # Conectar a la base de datos si la conexión está cerrada
    if connection.is_closed():
        connection.connect()
    try:
        yield  # Aquí es donde se ejecutará la aplicación
    finally:
        # Cerrar la conexión cuando la aplicación se detenga
        if not connection.is_closed():
            connection.close()


app = FastAPI(lifespan=lifespan)


app.include_router(
    user_route, 
    prefix="/api/user", 
    tags=["users"], 
    dependencies=[Depends(get_api_key)],
)# User routes
@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")
