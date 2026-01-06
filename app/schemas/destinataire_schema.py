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