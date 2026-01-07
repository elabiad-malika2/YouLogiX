from sqlalchemy.orm import Session
from app.models.gestionnaire import Gestionnaire
from app.schemas.gestionnaire_schema import GestionnaireCreate


def create_gestionnaire(db:Session,obj_in:GestionnaireCreate):
    db_obj=Gestionnaire(**obj_in.model_dump())

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj