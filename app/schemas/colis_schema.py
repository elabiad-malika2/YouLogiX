from pydantic import BaseModel
from typing import Optional
from enum import Enum

# On définit les statuts autorisés pour éviter les erreurs de saisie
class StatutColis(str, Enum):
    CREE = "créé"
    COLLECTE = "collecté"
    EN_STOCK = "en stock"
    EN_TRANSIT = "en transit"
    LIVRE = "livré"

# Champs de base communs
class ColisBase(BaseModel):
    description: str
    poids: float
    ville_destination: str

# Schéma pour la création (User Story : Gestionnaire crée un colis)
class ColisCreate(ColisBase):
    id_expediteur: int
    id_destinataire: int
    id_zone: int
    id_gestionnaire: int
    

# Schéma pour la mise à jour (User Story : Livreur change le statut)
class ColisUpdate(BaseModel):
    statut: Optional[StatutColis] = None
    id_livreur: Optional[int] = None

# Schéma pour la réponse API (Lecture du colis)
class ColisResponse(ColisBase):
    id: int
    statut: str
    id_expediteur: int
    id_destinataire: int
    id_zone: int
    id_gestionnaire: int
    id_livreur: Optional[int] = None

    class Config:
        from_attributes = True # Indispensable pour lire le modèle SQLAlchemy