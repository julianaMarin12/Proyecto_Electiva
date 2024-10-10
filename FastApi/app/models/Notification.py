from pydantic import BaseModel, date
# This imports the `BaseModel` class from the `pydantic` library for model creation and `date` for handling date fields.

class Notification(BaseModel):
    # This defines a class named `Notification` that inherits from `BaseModel`. The class represents a notification model.

    idNotification: int
    # This is a class attribute named `idNotification`, representing the unique identifier for the notification. It must be of type `int` (integer).

    notificationType: str
    # This is a class attribute named `notificationType`, representing the type of the notification (e.g., "email", "SMS"). It must be of type `str` (string).

    message: str
    # This is a class attribute named `message`, representing the content or message of the notification. It must be of type `str` (string).

    shippingDate: date
    # This is a class attribute named `shippingDate`, representing the date the notification is sent or scheduled to be sent. It uses the `date` type from the `pydantic` library to ensure it is a valid date.
