from sqlalchemy.orm import Session
from app.models.destinataire import Destinataire
from app.schemas.destinataire_schema import DestinataireCreate ,DestinataireUpdate
from app.utlis.exception_handler import raise_not_found
from app.utlis.logger import logger

def create_destinataire(db:Session , obj_in: DestinataireCreate):

    logger.info(f"Tentative de création d'un destinataire : {obj_in.email}")

    db_obj=Destinataire(**obj_in.model_dump())

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    logger.success(f"Destinataire créé avec succès (ID: {db_obj.id})")


    return db_obj


def update_destinatire(db:Session , dest_id:int , dest_in:DestinataireUpdate):

    logger.info(f"Mise à jour demandée pour  destinataire ID {dest_id}")


    db_obj=db.query(Destinataire).filter(Destinataire.id == dest_id).first()

    if not db_obj :
        raise_not_found("Destinataire",dest_id)

    data = dest_in.model_dump(exclude_unset=True)

    for field,value in data.items():
        setattr(db_obj,field,value)

    db.commit()
    db.refresh(db_obj)

    logger.success(f"Destinataire ID {dest_id} mis à jour avec succès")


    return db_obj


def delete_destinataire(db:Session,dest_id:int):

    db_obj=db.query(Destinataire).filter(Destinataire.id == dest_id).first()

    db.delete(db_obj)
    db.commit()

    logger.warning(f"ACTION CRITIQUE : Destinataire ID {dest_id} supprimé de la base")


    return {"message":"Supprimé avec succès"}