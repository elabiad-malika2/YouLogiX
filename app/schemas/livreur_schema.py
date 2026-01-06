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