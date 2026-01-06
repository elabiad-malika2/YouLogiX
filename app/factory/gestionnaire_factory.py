from sqlalchemy.orm import Session
from app.models.gestionnaire import Gestionnaire
from app.core.database import SessionLocal


def create_gestionnaires(db: Session):
    """Create sample managers"""
    gestionnaires_data = [
        {
            "nom": "Idrissi",
            "prenom": "Fatima",
            "telephone": "0678901234"
        },
        {
            "nom": "Jalal",
            "prenom": "Nadia",
            "telephone": "0689012345"
        },
        {
            "nom": "Khaldi",
            "prenom": "Rachid",
            "telephone": "0690123456"
        },
    ]

    gestionnaires = []
    for gestionnaire_data in gestionnaires_data:
        # Check if gestionnaire already exists
        existing = db.query(Gestionnaire).filter(
            Gestionnaire.telephone == gestionnaire_data["telephone"]
        ).first()
        if not existing:
            gestionnaire = Gestionnaire(**gestionnaire_data)
            db.add(gestionnaire)
            gestionnaires.append(gestionnaire)
        else:
            gestionnaires.append(existing)
    
    db.commit()
    for gestionnaire in gestionnaires:
        db.refresh(gestionnaire)
    
    print(f"✓ Created {len(gestionnaires_data)} gestionnaires")
    return gestionnaires


if __name__ == "__main__":
    db = SessionLocal()
    try:
        create_gestionnaires(db)
    finally:
        db.close()
