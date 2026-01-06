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