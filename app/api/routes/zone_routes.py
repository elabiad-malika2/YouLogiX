from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.core.database import get_db

# Importation de schemas

from app.schemas.zone_schema import ZoneCreate , ZoneResponse , ZoneUpdate

# importation de controller

from app.api.controllers import zone_controller

router=APIRouter(tags=["Zone System"])

# CRUD zones routes

@router.post("/zones",response_model=ZoneResponse)
def create_zone(obj_in:ZoneCreate,db:Session=Depends(get_db)):
    return zone_controller.create_zone(db,obj_in)

@router.patch("/zones/{zone_id}",response_model=ZoneResponse)
def update_zone(zone_id:int,zone_in:ZoneUpdate,db:Session=Depends(get_db)):
    return zone_controller.update_zone(db,zone_id,zone_in)

@router.delete("/zones/{zone_id}")
def delete_zone(zone_id:int,db:Session=Depends(get_db)):
    return zone_controller.delete_zone(db,zone_id)

