from fastapi import FastAPI
from app.core.database import engine , Base

from app.models.zone import Zone

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="YouExpress API",
    description="Système de gestion logistique pour YouExpress Maroc",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API YouExpress"}