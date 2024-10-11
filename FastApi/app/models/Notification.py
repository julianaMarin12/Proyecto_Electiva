"""
This module defines the Pydantic model for a notification.
"""
from pydantic import BaseModel, date

class Notification(BaseModel):
    """
    Defines a Pydantic model for a notification.
    """
    idNotification: int
    notificationType: str
    message: str
    shippingDate: date
