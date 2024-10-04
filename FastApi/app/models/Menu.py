from pydantic import BaseModel, date, time
import Recipe

class Menu(BaseModel):
    idMenu: int
    day: date    
    startTime: time
    endTime: time
    category: str
    Recipe: Recipe  #Es una lista