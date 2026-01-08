from typing import Optional
from pydantic import BaseModel

class GestionnaireBase(BaseModel):
    nom: str
    prenom: str
    telephone: str

class GestionnaireCreate(GestionnaireBase):
    pass

class GestionnaireResponse(GestionnaireBase):
    id: int

    class Config:
        from_attributes = True

class GestionnaireUpdate(BaseModel):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    telephone: Optional[str] = None