from sqlalchemy.orm import Session
from app.models.destinataire import Destinataire
from app.schemas.destinataire_schema import DestinataireCreate ,DestinataireUpdate
from app.utlis.exception_handler import raise_not_found

def create_destinataire(db:Session , obj_in: DestinataireCreate):

    db_obj=Destinataire(**obj_in.model_dump())

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj


def update_destinatire(db:Session , dest_id:int , dest_in:DestinataireUpdate):

    db_obj=db.query(Destinataire).filter(Destinataire.id == dest_id).first()

    if not db_obj :
        raise_not_found("Destinataire",dest_id)

    data = dest_in.model_dump(exclude_unset=True)

    for field,value in data.items():
        setattr(db_obj,field,value)

    db.commit()
    db.refresh(db_obj)

    return db_obj


def delete_destinataire(db:Session,dest_id:int):
    db_obj=db.query(Destinataire).filter(Destinataire.id == dest_id).first()

    db.delete(db_obj)
    db.commit()

    return {"message":"Supprimé avec succès"}