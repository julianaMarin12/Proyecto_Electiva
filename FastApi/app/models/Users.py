from pydantic import BaseModel
import Cluster

class User(BaseModel):
    idUsers: str
    nameUsers: str
    email: str
    password: str
    Cluster: Cluster    #Es una lista
    photoProfile: str
