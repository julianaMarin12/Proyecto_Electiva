from pydantic import BaseModel
import Recipe

class Menu(BaseModel):
    idMenu: str
    day: str    #Es una fecha
    startTime: str  #Es una hora
    endTime: str    #Es una hora
    category: str
    Recipe: Recipe  #Es una lista