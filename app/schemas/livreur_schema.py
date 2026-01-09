from typing import Optional
from pydantic import BaseModel

class LivreurBase(BaseModel):
    nom: str
    prenom: str
    telephone: str
    vehicule: str
    zone_assignee: str

class LivreurCreate(LivreurBase):
    pass

class LivreurResponse(LivreurBase):
    id: int

    class Config:
        from_attributes = True


class LivreurUpdate(BaseModel):
    nom: Optional[str] =None
    prenom: Optional[str] =None
    telephone: Optional[str] =None
    vehicule: Optional[str] =None
    zone_assignee: Optional[str] =None
 