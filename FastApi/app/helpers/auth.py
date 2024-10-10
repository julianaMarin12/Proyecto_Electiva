"""
This module initializes the FastAPI application and sets up the database connection
"""
# pylint: disable=import-error
import os
from fastapi import HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader
from dotenv import load_dotenv
# pylint: enable=import-error

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_KEY_NAME = "x-api-key"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_api_key(api_key: str = Security(api_key_header)):
    """
    Obtain the API key stored in the .env file

    Returns:
        api_key_header: The stored api key.
    """

    if api_key == API_KEY:
        return api_key
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail={
            "status": False,
            "status_code": status.HTTP_403_FORBIDDEN,
            "message": "Unauthorized",
        },
    )

"""
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

# Configuración de JWT
SECRET_KEY = "secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Configuración de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Lógica para autenticar usuarios
def authenticate_user(username: str, password: str):
    # Obtener el usuario de una "base de datos" (aquí simulada)
    user = get_user_from_db(username)
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user


# Obtener el usuario actual desde el token JWT
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return get_user_from_db(username)  # Simulación de obtener usuario
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
"""