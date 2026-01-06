from sqlalchemy.orm import Session
from app.models.destinataire import Destinataire
from app.core.database import SessionLocal


def create_destinataires(db: Session):
    """Create sample recipients"""
    destinataires_data = [
        {
            "nom": "Mansouri",
            "prenom": "Leila",
            "email": "leila.mansouri@gmail.com",
            "telephone": "0665678901",
            "adresse": "34 Rue Ibn Rochd, Centre Ville, Rabat"
        },
        {
            "nom": "Tazi",
            "prenom": "Mehdi",
            "email": "mehdi.tazi@yahoo.fr",
            "telephone": "0676789012",
            "adresse": "89 Rue Ahmed El Mansour, Agdal, Rabat"
        },
        {
            "nom": "Bennani",
            "prenom": "Sophia",
            "email": "sophia.bennani@outlook.com",
            "telephone": "0687890123",
            "adresse": "12 Avenue Moulay Hassan, Hassan, Rabat"
        },
        {
            "nom": "Ouahbi",
            "prenom": "Karim",
            "email": "karim.ouahbi@gmail.com",
            "telephone": "0698901234",
            "adresse": "45 Rue Laayoune, Hay Riad, Rabat"
        },
        {
            "nom": "Ziani",
            "prenom": "Yasmine",
            "email": "yasmine.ziani@hotmail.com",
            "telephone": "0609012345",
            "adresse": "67 Boulevard Ahl Loghlam, Souissi, Rabat"
        },
        {
            "nom": "Sabri",
            "prenom": "Hicham",
            "email": "hicham.sabri@gmail.com",
            "telephone": "0610123456",
            "adresse": "23 Rue Nador, Yacoub El Mansour, Rabat"
        },
        {
            "nom": "Rifai",
            "prenom": "Sara",
            "email": "sara.rifai@yahoo.com",
            "telephone": "0621234568",
            "adresse": "78 Avenue Al Qods, Takaddoum, Rabat"
        },
        {
            "nom": "Benjelloun",
            "prenom": "Omar",
            "email": "omar.benjelloun@gmail.com",
            "telephone": "0632345679",
            "adresse": "90 Rue Ghandi, Akkari, Rabat"
        },
    ]

    destinataires = []
    for destinataire_data in destinataires_data:
        # Check if destinataire already exists
        existing = db.query(Destinataire).filter(
            Destinataire.email == destinataire_data["email"]
        ).first()
        if not existing:
            destinataire = Destinataire(**destinataire_data)
            db.add(destinataire)
            destinataires.append(destinataire)
        else:
            destinataires.append(existing)
    
    db.commit()
    for destinataire in destinataires:
        db.refresh(destinataire)
    
    print(f"✓ Created {len(destinataires_data)} destinataires")
    return destinataires


if __name__ == "__main__":
    db = SessionLocal()
    try:
        create_destinataires(db)
    finally:
        db.close()
