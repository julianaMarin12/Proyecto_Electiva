from pydantic import BaseModel
# This imports the `BaseModel` class from the `pydantic` library for creating data models with validation.

class Clusters(BaseModel):
    # This defines a class named `Clusters` that inherits from `BaseModel`. The class represents a model for clusters.

    idClusters: int
    # This is a class attribute named `idClusters`, which holds the unique identifier for the cluster. It must be of type `int` (integer).

    nameClusters: str
    # This is a class attribute named `nameClusters`, which holds the name of the cluster. It must be of type `str` (string).

    amount: int
    # This is a class attribute named `amount`, which represents the quantity or number associated with the cluster. It must be of type `int` (integer).
