from app.utlis.exception_handler import raise_not_found
from app.schemas.zone_schema import ZoneCreate,ZoneUpdate
from app.models.zone import Zone
from sqlalchemy.orm import Session

def create_zone(db:Session,obj_in:ZoneCreate):
    db_obj=Zone(**obj_in.model_dump())

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj

def update_zone(db:Session,zone_id:int,obj_in:ZoneUpdate):

    obj_db=db.query(Zone).filter(Zone.id == zone_id).first()

    if not obj_db :
         raise_not_found("Zone",zone_id)
    
    data = obj_in.model_dump(exclude_unset=True) 

    for field,value in data.items():
        setattr(obj_db,field,value)

    db.commit()
    db.refresh(obj_db)

    return obj_db

def delete_zone(db:Session,zone_id:int):
    obj_db=db.query(Zone).filter(Zone.id == zone_id).first()

    if not obj_db:
        raise_not_found("Zone",zone_id)

    db.delete(obj_db)
    db.commit()

    return {"message": "Supprimé avec succès"}
