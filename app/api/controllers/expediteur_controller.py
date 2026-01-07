from sqlalchemy.orm import Session
from app.models.expediteur import Expediteur
from app.schemas.expediteur_schema import ExpediteurCreate



def create_expediteur(db:Session , obj_in:ExpediteurCreate):
    db_obj=Expediteur(**obj_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj

def get_all(db:Session):
    return db.query(Expediteur).all()