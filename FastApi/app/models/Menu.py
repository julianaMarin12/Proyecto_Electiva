"""
This module defines the Pydantic model for a menu.
"""

from pydantic import BaseModel, date, time

class Menu(BaseModel):
    """
    A Pydantic model for a menu.
    """
    idMenu: int
    day: date
    startTime: time
    endTime: time
    category: str
