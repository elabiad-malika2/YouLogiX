from sqlalchemy.orm import Session
from app.models.livreur import Livreur
from app .schemas.livreur_schema import LivreurCreate


def create_livreur(db:Session,obj_in:LivreurCreate):
    
    db_obj=Livreur(**obj_in.model_dump())

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj