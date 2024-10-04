from pydantic import BaseModel

class User(BaseModel):
    idUsers: int
    nameUsers: str
    email: str
    password: str
    photoProfile: str
