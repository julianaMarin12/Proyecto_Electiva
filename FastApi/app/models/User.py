from pydantic import BaseModel

class User(BaseModel):
    idUsers: int
    name: str
    email: str
    password: str
    photoProfile: str
