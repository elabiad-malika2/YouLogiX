from sqlalchemy.orm import Session
from app.models.expediteur import Expediteur
from app.schemas.expediteur_schema import ExpediteurUpdate
from app.utlis.exception_handler import raise_not_found

def update_expediteur_logic(db: Session, exp_id: int, exp_in: ExpediteurUpdate):
    # 1. Chercher l'objet existant
    db_obj = db.query(Expediteur).filter(Expediteur.id == exp_id).first()
    if not db_obj:
        raise_not_found("Expéditeur", exp_id)

    # 2. Convertir le schéma en dictionnaire en ignorant les champs non envoyés (None)
    update_data = exp_in.model_dump(exclude_unset=True)

    # 3. Mettre à jour l'objet dynamiquement
    for field, value in update_data.items():
        setattr(db_obj, field, value)

    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_expediteur_logic(db: Session, exp_id: int):
    db_obj = db.query(Expediteur).filter(Expediteur.id == exp_id).first()
    if not db_obj:
        raise_not_found("Expéditeur", exp_id)
    
    db.delete(db_obj)
    db.commit()
    return {"message": "Supprimé avec succès"}





# class ExpediteurUpdate(BaseModel):
#     nom: Optional[str] = None
#     prenom: Optional[str] = None
#     telephone: Optional[str] = None
#     email: Optional[EmailStr] = None
#     adresse: Optional[str] = None










from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.expediteur_schema import ExpediteurUpdate, ExpediteurResponse
from app.api.controllers import expediteur_controller

router = APIRouter(prefix="/acteurs", tags=["Acteurs"])

@router.patch("/expediteurs/{exp_id}", response_model=ExpediteurResponse)
def update_exp(exp_id: int, exp_in: ExpediteurUpdate, db: Session = Depends(get_db)):
    return expediteur_controller.update_expediteur(db, exp_id, exp_in)

@router.delete("/expediteurs/{exp_id}")
def delete_exp(exp_id: int, db: Session = Depends(get_db)):
    return expediteur_controller.delete_expediteur(db, exp_id)