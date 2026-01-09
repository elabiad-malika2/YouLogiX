from sqlalchemy.orm import Session
from app.models.livreur import Livreur
from app .schemas.livreur_schema import LivreurCreate ,LivreurUpdate
from app.utlis.exception_handler import raise_not_found


def create_livreur(db:Session,obj_in:LivreurCreate):
    
    db_obj=Livreur(**obj_in.model_dump())

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj

def get_all(db:Session):
    return db.query(Livreur).all()


def update_livreur(db:Session,livr_id:int,livr_in:LivreurUpdate):
    db_obj=db.query(Livreur).filter(Livreur.id == livr_id).first()

    if not db_obj:
        raise_not_found("Livreur",livr_id)
    data=livr_in.model_dump(exclude_unset=True)

    for field,value in data.items():
        setattr(db_obj,field,value)
    
    db.commit()
    db.refresh(db_obj)

    return db_obj



def delete_livreur(db:Session,livr_id:int):
    db_obj=db.query(Livreur).filter(Livreur.id == livr_id).first()

    if not db_obj:
        raise_not_found("Livreur",livr_id)

    db.delete(db_obj)
    db.commit()

    return {"message":"Supprimé avec succès"}







