from sqlalchemy.orm import Session
from app.models.destinataire import Destinataire
from app.schemas.destinataire_schema import DestinataireCreate

def create_destinataire(db:Session , obj_in: DestinataireCreate):

    db_obj=Destinataire(**obj_in.model_dump())

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj