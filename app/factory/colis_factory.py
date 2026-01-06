from sqlalchemy.orm import Session
from app.models.colis import Colis
from app.models.zone import Zone
from app.models.livreur import Livreur
from app.models.expediteur import Expediteur
from app.models.destinataire import Destinataire
from app.models.gestionnaire import Gestionnaire
from app.core.database import SessionLocal
import random


def create_colis(db: Session):
    """Create sample packages"""
    # Get existing records
    zones = db.query(Zone).all()
    livreurs = db.query(Livreur).all()
    expediteurs = db.query(Expediteur).all()
    destinataires = db.query(Destinataire).all()
    gestionnaires = db.query(Gestionnaire).all()

    if not all([zones, livreurs, expediteurs, destinataires, gestionnaires]):
        print("⚠ Missing required data. Please run other factories first.")
        return []

    colis_data = [
        {
            "description": "Vêtements - Robe de soirée",
            "poids": 0.8,
            "statut": "en_transit",
            "ville_destination": "Rabat"
        },
        {
            "description": "Électronique - Smartphone",
            "poids": 0.5,
            "statut": "créé",
            "ville_destination": "Rabat"
        },
        {
            "description": "Livres - Collection de 5 livres",
            "poids": 2.5,
            "statut": "en_cours_de_livraison",
            "ville_destination": "Rabat"
        },
        {
            "description": "Parfum - Coffret luxe",
            "poids": 1.2,
            "statut": "créé",
            "ville_destination": "Rabat"
        },
        {
            "description": "Chaussures - Paire de baskets",
            "poids": 1.5,
            "statut": "livré",
            "ville_destination": "Rabat"
        },
        {
            "description": "Accessoires - Montre connectée",
            "poids": 0.3,
            "statut": "en_transit",
            "ville_destination": "Rabat"
        },
        {
            "description": "Cosmétiques - Produits de beauté",
            "poids": 1.0,
            "statut": "créé",
            "ville_destination": "Rabat"
        },
        {
            "description": "Jouets - Jeu de société",
            "poids": 1.8,
            "statut": "en_cours_de_livraison",
            "ville_destination": "Rabat"
        },
        {
            "description": "Électronique - Écouteurs sans fil",
            "poids": 0.2,
            "statut": "livré",
            "ville_destination": "Rabat"
        },
        {
            "description": "Vêtements - Ensemble sport",
            "poids": 0.7,
            "statut": "créé",
            "ville_destination": "Rabat"
        },
        {
            "description": "Cuisine - Ustensiles de cuisson",
            "poids": 3.0,
            "statut": "en_transit",
            "ville_destination": "Rabat"
        },
        {
            "description": "Décoration - Cadre photo",
            "poids": 1.5,
            "statut": "livré",
            "ville_destination": "Rabat"
        },
    ]

    colis_list = []
    for i, colis_data_item in enumerate(colis_data):
        # Assign random relationships
        colis_data_item["id_expediteur"] = random.choice(expediteurs).id
        colis_data_item["id_destinataire"] = random.choice(destinataires).id
        colis_data_item["id_zone"] = random.choice(zones).id
        colis_data_item["id_gestionnaire"] = random.choice(gestionnaires).id
        
        # Assign livreur only if status is not "créé"
        if colis_data_item["statut"] != "créé":
            colis_data_item["id_livreur"] = random.choice(livreurs).id
        else:
            colis_data_item["id_livreur"] = None

        colis = Colis(**colis_data_item)
        db.add(colis)
        colis_list.append(colis)
    
    db.commit()
    for colis in colis_list:
        db.refresh(colis)
    
    print(f"✓ Created {len(colis_data)} colis")
    return colis_list


if __name__ == "__main__":
    db = SessionLocal()
    try:
        create_colis(db)
    finally:
        db.close()
