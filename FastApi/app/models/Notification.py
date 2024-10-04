from pydantic import BaseModel

class Notification(BaseModel):
    idNotification: str
    notificationType: str
    message: str
    shippingDate: str   #Es una fecha