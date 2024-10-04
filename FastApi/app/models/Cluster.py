from pydantic import BaseModel

class Clusters(BaseModel):
    idClusters: str
    nameClusters: str
    amount: int