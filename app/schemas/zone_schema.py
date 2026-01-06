from pydantic import BaseModel

# Champs communs pour la lecture et la création
class ZoneBase(BaseModel):
    nom: str
    code_postal: int

# Utilisé lors de la création (POST /zones)
class ZoneCreate(ZoneBase):
    pass

# Utilisé pour la réponse API (ce que le client voit)
class ZoneResponse(ZoneBase):
    id: int

    class Config:
        from_attributes = True # Permet de lire les objets SQLAlchemy