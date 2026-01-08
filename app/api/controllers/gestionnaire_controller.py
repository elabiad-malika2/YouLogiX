from sqlalchemy.orm import Session
from app.models.gestionnaire import Gestionnaire
from app.schemas.gestionnaire_schema import GestionnaireCreate,GestionnaireUpdate
from app.utlis.exception_handler import raise_not_found


def create_gestionnaire(db:Session,obj_in:GestionnaireCreate):
    db_obj=Gestionnaire(**obj_in.model_dump())

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj


def update_gestionnaire(db: Session, exp_id: int, exp_in: GestionnaireUpdate):

    db_obj = db.query(Gestionnaire).filter(Gestionnaire.id == exp_id).first()
    if not db_obj:
        raise_not_found("Expéditeur", exp_id)


    update_data = exp_in.model_dump(exclude_unset=True)


    for field, value in update_data.items():
        setattr(db_obj, field, value)

    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_gestionnaire(db: Session, exp_id: int):
    db_obj = db.query(Gestionnaire).filter(Gestionnaire.id == exp_id).first()
    if not db_obj:
        raise_not_found("Expéditeur", exp_id)
    
    db.delete(db_obj)
    db.commit()
    return {"message": "Supprimé avec succès"}
