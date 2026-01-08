from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.core.database import get_db

# Importation des fonctions schemas

from app.schemas.livreur_schema import LivreurCreate,LivreurResponse,LivreurUpdate
from app.schemas.destinataire_schema import DestinataireCreate,DestinataireResponse,DestinataireUpdate
from app.schemas.gestionnaire_schema import GestionnaireCreate,GestionnaireResponse,GestionnaireUpdate
from app.schemas.expediteur_schema import ExpediteurCreate,ExpediteurResponse,ExpediteurUpdate

# Importation des controllers

from app.api.controllers import(
    expediteur_controller,destinataire_controller,
    gestionnaire_controller,livreur_controller
)


router=APIRouter(tags=['Acteurs System'])

# CRUD expediteurs routes
@router.post('/expediteurs',response_model=ExpediteurResponse)
def create_exp(obj_in:ExpediteurCreate,db:Session=Depends(get_db)):
    return expediteur_controller.create_expediteur(db,obj_in)

@router.patch("/expediteurs/{exp_id}", response_model=ExpediteurResponse)
def update_exp(exp_id: int, exp_in: ExpediteurUpdate, db: Session = Depends(get_db)):
    return expediteur_controller.update_expediteur(db, exp_id, exp_in)

@router.delete("/expediteurs/{exp_id}")
def delete_exp(exp_id:int,db:Session=Depends(get_db)):
    return expediteur_controller.delete_expediteur(db,exp_id)



# CRUD destinataires routes
@router.post("/destinataires",response_model=DestinataireResponse)
def create_dest(obj_in:DestinataireCreate,db:Session=Depends(get_db)):
    return destinataire_controller.create_destinataire(db,obj_in)

@router.patch("/destinataire/{dest_id}",response_model=DestinataireUpdate)
def update_dest(dest_id:int,dest_in:DestinataireUpdate,db:Session=Depends(get_db)):
    return destinataire_controller.update_destinatire(db,dest_id,dest_in)

@router.delete("/destinataire/{dist_id}")
def delete_liv(dist_id:int,db:Session=Depends(get_db)):
    return destinataire_controller.delete_destinataire(db,dist_id)


# CRUD livreurs routes
@router.post("/livreurs",response_model=LivreurResponse)
def create_liv(obj_in:LivreurCreate,db:Session=Depends(get_db)):
    return livreur_controller.create_livreur(db,obj_in)

@router.patch("/livreurs/{livr_id}",response_model=LivreurUpdate)
def update_liv(livr_id:int,obj_in:LivreurUpdate,db:Session=Depends(get_db)):
    return livreur_controller.update_livreur(db,livr_id,obj_in)

@router.delete("/livreurs/{livr_id}")
def delete_liv(livr_id:int,db:Session=Depends(get_db)):
    return livreur_controller.delete_livreur(db,livr_id)

# CRUD gestionnaires routes
@router.post("/gestionnaires",response_model=GestionnaireResponse)
def create_gest(obj_in:GestionnaireCreate,db:Session=Depends(get_db)):
    return gestionnaire_controller.create_livreur(db,obj_in)

@router.patch("/gestionnaire/{gest_id}", response_model=GestionnaireResponse)
def update_exp(gest_id: int, exp_in: GestionnaireUpdate, db: Session = Depends(get_db)):
    return gestionnaire_controller.update_gestionnaire(db, gest_id, exp_in)

@router.delete("/gestionnaire/{gest_id}")
def delete_exp(gest_id: int, db: Session = Depends(get_db)):
    return gestionnaire_controller.delete_gestionnaire(db, gest_id)
