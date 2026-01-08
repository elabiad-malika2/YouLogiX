from typing import Optional
from pydantic import BaseModel, EmailStr

class DestinataireBase(BaseModel):
    nom: str
    prenom: str
    telephone: str
    email: EmailStr
    adresse: str

class DestinataireCreate(DestinataireBase):
    pass

class DestinataireResponse(DestinataireBase):
    id: int

    class Config:
        from_attributes = True




class DestinataireUpdate(BaseModel):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    telephone: Optional[str] = None
    email: Optional[EmailStr] = None
    adresse: Optional[str] = None
