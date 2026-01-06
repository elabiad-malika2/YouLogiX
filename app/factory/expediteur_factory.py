from sqlalchemy.orm import Session
from app.models.expediteur import Expediteur
from app.core.database import SessionLocal


def create_expediteurs(db: Session):
    """Create sample senders"""
    expediteurs_data = [
        {
            "nom": "Boutique",
            "prenom": "Mode Elite",
            "email": "contact@modeelite.ma",
            "telephone": "0520123456",
            "adresse": "12 Avenue Mohammed V, Rabat"
        },
        {
            "nom": "Hamza",
            "prenom": "Said",
            "email": "said.hamza@gmail.com",
            "telephone": "0621234567",
            "adresse": "45 Rue Oued Fes, Agdal, Rabat"
        },
        {
            "nom": "Technologies",
            "prenom": "Digital Store",
            "email": "info@digitalstore.ma",
            "telephone": "0532345678",
            "adresse": "78 Boulevard Hassan II, Rabat"
        },
        {
            "nom": "Lahlou",
            "prenom": "Amina",
            "email": "amina.lahlou@hotmail.com",
            "telephone": "0643456789",
            "adresse": "23 Rue Al Amir Fal Ould Oumair, Hassan, Rabat"
        },
        {
            "nom": "Parfums",
            "prenom": "Luxe Orient",
            "email": "contact@luxeorient.ma",
            "telephone": "0554567890",
            "adresse": "56 Avenue Annakhil, Hay Riad, Rabat"
        },
    ]

    expediteurs = []
    for expediteur_data in expediteurs_data:
        # Check if expediteur already exists
        existing = db.query(Expediteur).filter(
            Expediteur.email == expediteur_data["email"]
        ).first()
        if not existing:
            expediteur = Expediteur(**expediteur_data)
            db.add(expediteur)
            expediteurs.append(expediteur)
        else:
            expediteurs.append(existing)
    
    db.commit()
    for expediteur in expediteurs:
        db.refresh(expediteur)
    
    print(f"✓ Created {len(expediteurs_data)} expediteurs")
    return expediteurs


if __name__ == "__main__":
    db = SessionLocal()
    try:
        create_expediteurs(db)
    finally:
        db.close()
