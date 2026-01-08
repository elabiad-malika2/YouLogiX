from typing import Optional
from pydantic import BaseModel, EmailStr

class ExpediteurBase(BaseModel):
    nom: str
    prenom: str
    telephone: str
    email: EmailStr
    adresse: str

class ExpediteurCreate(ExpediteurBase):
    pass

class ExpediteurResponse(ExpediteurBase):
    id: int

    class Config:
        from_attributes = True


class ExpediteurUpdate(BaseModel):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    telephone: Optional[str] = None
    email: Optional[EmailStr] = None
    adresse: Optional[str] = None









