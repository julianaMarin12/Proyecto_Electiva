"""
This module defines the Pydantic model for a clusters.
"""
from pydantic import BaseModel

class Clusters(BaseModel):
    """
    This class represents a Pydantic model for clusters.
    """
    idClusters: int
    nameClusters: str
    amount: int
