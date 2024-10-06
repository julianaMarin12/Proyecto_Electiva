from pydantic import BaseModel

class User(BaseModel):
    idUsers: int
    username: str
    email: str
    password: str
    photoProfile: str
