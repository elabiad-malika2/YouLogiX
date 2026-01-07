from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.colis_schema import ColisCreate,ColisResponse
from app.api.controllers import colis_controller


router = APIRouter(prefix="/colis", tags=["Colis"])

@router.post("/",response_model=ColisResponse)
def creat_new_colis(colis_in:ColisCreate, db:Session = Depends(get_db)):
    try:
        
        return colis_controller.create_colis_logic(db, colis_in)
    
    except Exception as e :
        raise HTTPException(status_code=400, detail=f"Error lors de la creation: {str(e)}")
    
    