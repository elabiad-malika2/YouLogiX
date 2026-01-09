from sqlalchemy.orm import Session
from app.models.expediteur import Expediteur
from app.schemas.expediteur_schema import ExpediteurCreate
from app.utlis.exception_handler import raise_not_found



def create_expediteur(db:Session , obj_in:ExpediteurCreate):
    db_obj=Expediteur(**obj_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj

def get_all(db:Session):
    return db.query(Expediteur).all()

def update_expediteur(db:Session,expd_id:int , obj_in:ExpediteurCreate):

    db_obj=db.query(Expediteur).filter(Expediteur.id == expd_id).first()

    if not db_obj:
        raise_not_found("Expéditeur",expd_id)

    # Convertir schema en dictionnaire et ignorer les champs None
    data=obj_in.model_dump(exclude_unset=True)

    for field,value in data.items():
        setattr(db_obj,field,value)
    
    db.commit()
    db.refresh(db_obj)

    return db_obj


def delete_expediteur(db:Session,exp_id:int):
    db_obj= db.query(Expediteur).filter(Expediteur.id == exp_id).first()

    if not db_obj:
        raise_not_found("Expéditeur",exp_id)

    db.delete(db_obj)
    db.commit()

    return {"message":"Supprimé avec succès"}






