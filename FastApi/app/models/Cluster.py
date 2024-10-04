from pydantic import BaseModel

class Clusters(BaseModel):
    idClusters: int
    nameClusters: str
    amount: int