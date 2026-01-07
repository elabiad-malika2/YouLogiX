from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.core.database import get_db

# Importation des fonctions schemas

from app.schemas.livreur_schema import LivreurCreate,LivreurResponse
from app.schemas.destinataire_schema import DestinataireCreate,DestinataireResponse
from app.schemas.gestionnaire_schema import GestionnaireCreate,GestionnaireResponse
from app.schemas.expediteur_schema import ExpediteurCreate,ExpediteurResponse

# Importation des controllers

from app.api.controllers import(
    expediteur_controller,destinataire_controller,
    gestionnaire_controller,livreur_controller
)


router=APIRouter(tags=['Acteurs System'])

@router.post('/expediteurs',response_model=ExpediteurResponse)
def create_exp(obj_in:ExpediteurCreate,db:Session=Depends(get_db)):
    return expediteur_controller.create_expediteur(db,obj_in)


@router.post("/destinataires",response_model=DestinataireResponse)
def create_dest(obj_in:DestinataireCreate,db:Session=Depends(get_db)):
    return destinataire_controller.create_destinataire(db,obj_in)

@router.post("/livreurs",response_model=LivreurResponse)
def create_liv(obj_in:LivreurCreate,db:Session=Depends(get_db)):
    return livreur_controller.create_livreur(db,obj_in)


@router.post("/gestionnaires",response_model=GestionnaireResponse)
def create_gest(obj_in:GestionnaireCreate,db:Session=Depends(get_db)):
    return livreur_controller.create_livreur(db,obj_in)
