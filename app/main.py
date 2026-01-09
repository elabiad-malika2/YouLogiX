from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.database import engine, Base, get_db
from app.factory.seed_all import seed_database
from app.api.routes import colis_routes
from app.utlis.logger import logger

# importation des models
from app.models.expediteur import Expediteur
from app.models.destinataire import Destinataire
from app.models.livreur import Livreur
from app.models.gestionnaire import Gestionnaire
from app.models.zone import Zone
from app.models.colis import Colis
from app.models.historique import HistoriqueStatut

# importation des routes

from app.api.routes import acteurs_routes,zone_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="YouExpress API",
    description="Système de gestion logistique pour YouExpress Maroc",
    version="1.0.0"
)


logger.success("L'API YouExpress est prête et en ligne")

app.include_router(colis_routes.router)
app.include_router(acteurs_routes.router)
app.include_router(zone_routes.router)


# Method 1: Startup Event - Automatically seed data when app starts
@app.on_event("startup")
async def startup_event():
    """
    This runs automatically when the FastAPI application starts.
    Uncomment the line below to enable automatic seeding on startup.
    """
    # seed_database()  # Uncomment to auto-seed on startup
    pass 




@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API YouExpress"}