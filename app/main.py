from fastapi import FastAPI

app = FastAPI(
    title="YouExpress API",
    description="Système de gestion logistique pour YouExpress Maroc",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API YouExpress"}