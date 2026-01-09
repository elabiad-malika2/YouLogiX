from typing import Optional
from pydantic import BaseModel

class ZoneBase(BaseModel):
    nom: str
    code_postal: int

class ZoneCreate(ZoneBase):
    pass

class ZoneResponse(ZoneBase):
    id: int

    class Config:
        from_attributes = True 

class ZoneUpdate(BaseModel):
    nom: Optional[str]=None
    code_postal: Optional[int]=None