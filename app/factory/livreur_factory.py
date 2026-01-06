from sqlalchemy.orm import Session
from app.models.livreur import Livreur
from app.core.database import SessionLocal


def create_livreurs(db: Session):
    """Create sample delivery drivers"""
    livreurs_data = [
        {
            "nom": "Alami",
            "prenom": "Mohammed",
            "telephone": "0612345678",
            "vehicule": "Moto",
            "zone_assignee": "Centre Ville"
        },
        {
            "nom": "Benali",
            "prenom": "Ahmed",
            "telephone": "0623456789",
            "vehicule": "Voiture",
            "zone_assignee": "Agdal"
        },
        {
            "nom": "Chakir",
            "prenom": "Karim",
            "telephone": "0634567890",
            "vehicule": "Moto",
            "zone_assignee": "Hassan"
        },
        {
            "nom": "Driss",
            "prenom": "Youssef",
            "telephone": "0645678901",
            "vehicule": "Camionnette",
            "zone_assignee": "Hay Riad"
        },
        {
            "nom": "El Fassi",
            "prenom": "Omar",
            "telephone": "0656789012",
            "vehicule": "Moto",
            "zone_assignee": "Souissi"
        },
        {
            "nom": "Fathi",
            "prenom": "Hassan",
            "telephone": "0667890123",
            "vehicule": "Voiture",
            "zone_assignee": "Yacoub El Mansour"
        },
    ]

    livreurs = []
    for livreur_data in livreurs_data:
        # Check if livreur already exists
        existing = db.query(Livreur).filter(
            Livreur.telephone == livreur_data["telephone"]
        ).first()
        if not existing:
            livreur = Livreur(**livreur_data)
            db.add(livreur)
            livreurs.append(livreur)
        else:
            livreurs.append(existing)
    
    db.commit()
    for livreur in livreurs:
        db.refresh(livreur)
    
    print(f"✓ Created {len(livreurs_data)} livreurs")
    return livreurs


if __name__ == "__main__":
    db = SessionLocal()
    try:
        create_livreurs(db)
    finally:
        db.close()
