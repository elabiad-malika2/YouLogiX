from sqlalchemy.orm import Session

from app.models.colis import Colis 
from app.schemas.colis_schema import ColisCreate


def create_colis_logic(db:Session, colis_in:ColisCreate):
    db_colis = Colis(
        description = colis_in.description,
        poids = colis_in.poids,
        ville_destination = colis_in.ville_destination,
        id_expediteur = colis_in.id_expediteur,
        id_destinataire = colis_in.id_destinataire,
        id_zone = colis_in.id_zone,
        id_gestionnaire = colis_in.id_gestionnaire,
        statut = "créé",
    )
    
    db.add(db_colis)
    db.commit()
    db.refresh(db_colis)
    
    return db_colis 