from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.colis_schema import ColisCreate,ColisResponse
from app.api.controllers import colis_controller
from app.utlis.exception_handler import raise_error_creation, raise_error_update


router = APIRouter(prefix="/colis", tags=["Colis"])

@router.post("/create",response_model=ColisResponse)
def creat_new_colis(colis_in:ColisCreate, db:Session = Depends(get_db)):
    try:
        
        return colis_controller.create_colis_logic(db, colis_in)
    
    except Exception as e :
        raise_error_creation(e)
        


@router.patch("/assign",response_model=ColisResponse)
def assign_colis(livreur_id:int, colis_id:int, db:Session = Depends(get_db)):
    try:
        return colis_controller.assign_colis(db, colis_id, livreur_id)
        
    except Exception as e:
        raise_error_update(e)
