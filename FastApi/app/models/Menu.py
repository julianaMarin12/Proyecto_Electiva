from pydantic import BaseModel, date, time
# This imports the `BaseModel` class from the `pydantic` library for model creation, and `date` and `time` types to handle date and time fields.

class Menu(BaseModel):
    # This defines a class named `Menu` that inherits from `BaseModel`. The class represents a menu model.

    idMenu: int
    # This is a class attribute named `idMenu`, representing the unique identifier for the menu. It must be of type `int` (integer).

    day: date
    # This is a class attribute named `day`, representing the date of the menu. It uses the `date` type, ensuring that the value is a valid date.

    startTime: time
    # This is a class attribute named `startTime`, representing the start time of the menu. It uses the `time` type to ensure it is a valid time.

    endTime: time
    # This is a class attribute named `endTime`, representing the end time of the menu. It must also be of type `time`.

    category: str
    # This is a class attribute named `category`, representing the category of the menu (e.g., "breakfast", "lunch", "dinner"). It must be of type `str` (string).
