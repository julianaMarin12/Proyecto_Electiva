from pydantic import BaseModel, date

class Notification(BaseModel):
    idNotification: int
    notificationType: str
    message: str
    shippingDate: date   #Es una fecha