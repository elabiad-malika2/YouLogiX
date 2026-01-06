from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.database import engine, Base, get_db
from app.factory.seed_all import seed_database
import sys

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


# Method 1: Startup Event - Automatically seed data when app starts
@app.on_event("startup")
async def startup_event():
    """
    This runs automatically when the FastAPI application starts.
    Uncomment the line below to enable automatic seeding on startup.
    """
    seed_database()  # Uncomment to auto-seed on startup
    pass


# Method 2: Admin API Endpoint - Trigger seeding via HTTP request
# @app.post("/admin/seed", tags=["Admin"])
# async def seed_via_api(db: Session = Depends(get_db)):
#     """
#     Seed the database with sample data.
#     Access: POST http://localhost:8000/admin/seed
#     """
#     try:
#         from app.factory.seed_all import seed_database
#         result = seed_database()
#         return {
#             "status": "success",
#             "message": "Database seeded successfully",
#             "data": result
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Seeding failed: {str(e)}")


# Method 3: Check if data exists endpoint
# @app.get("/admin/check-data", tags=["Admin"])
# async def check_data(db: Session = Depends(get_db)):
#     """
#     Check if database has data.
#     """
#     counts = {
#         "zones": db.query(Zone).count(),
#         "expediteurs": db.query(Expediteur).count(),
#         "destinataires": db.query(Destinataire).count(),
#         "livreurs": db.query(Livreur).count(),
#         "gestionnaires": db.query(Gestionnaire).count(),
#         "colis": db.query(Colis).count(),
#         "historiques": db.query(HistoriqueStatut).count()
#     }
#     return {
#         "status": "success",
#         "counts": counts,
#         "total_records": sum(counts.values())
#     }


@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API YouExpress"}