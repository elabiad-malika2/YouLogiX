from fastapi import FastAPI
from app.core.database import engine , Base

from app.models.expediteur import Expediteur
from app.models.destinataire import Destinataire
from app.models.livreur import Livreur
from app.models.gestionnaire import Gestionnaire
from app.models.zone import Zone
from app.models.colis import Colis
from app.models.historique import HistoriqueStatut

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="YouExpress API",
    description="Système de gestion logistique pour YouExpress Maroc",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API YouExpress"}