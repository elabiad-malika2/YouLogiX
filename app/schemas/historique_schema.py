from pydantic import BaseModel
from datetime import datetime

class HistoriqueBase(BaseModel):
    id_colis: int
    ancien_statut: str
    nouveau_statut: str

# On ne définit que la réponse car l'historique est créé automatiquement 
# par le système lors d'un changement de statut, pas par l'utilisateur.
class HistoriqueResponse(HistoriqueBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True