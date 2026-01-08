from sqlalchemy.orm import Session
from datetime import datetime
from app.models.colis import Colis 
from app.models.historique import HistoriqueStatut
from app.schemas.colis_schema import ColisCreate
from app.models.zone import Zone   

# Module Colis (Le plus gros morceau) :
# Controller colis_controller.py : 
# Fonction creer_colis : Création simple. d
# Fonction assigner_livreur : Lier un colis à un livreur. d
# Fonction mettre_a_jour_statut : Trés important -> Cette fonction doit aussi créer automatiquement une ligne dans la table HistoriqueStatut à chaque changement.
# Filtres avancés : Pouvoir lister les colis par Statut ou par Zone.



def create_colis_logic(db:Session, colis_in:ColisCreate):
    
    db_colis = Colis(**colis_in.model_dump())
    
    db.add(db_colis)
    db.commit()
    db.refresh(db_colis)

    return db_colis 


def assign_colis(db:Session, colis_id:int, livreur_id:int):
    
    colis = db.query(Colis).filter(Colis.id == colis_id).first()
    historique = db.query(HistoriqueStatut).filter(HistoriqueStatut.id_colis == colis_id).first()
    
    colis.id_livreur = livreur_id 
    colis.statut = "en_transit"
    
    # HistoriqueStatut.nouveau_statut
    if historique.nouveau_statut != colis.statut :
        historique.ancien_statut = historique.nouveau_statut
        historique.nouveau_statut = colis.statut
    historique.timestamp = datetime.utcnow()
    

    db.commit()
    db.refresh(colis)
    db.refresh(historique)
    
    return colis


def update_statut(db:Session, new_statut:str, colis_id:int):
    
    colis = db.query(Colis).filter(Colis.id == colis_id).first()
    historique = db.query(HistoriqueStatut).filter(HistoriqueStatut.id_colis == colis_id).first()
    
    colis.statut = new_statut
    
    if historique.nouveau_statut != colis.statut :
        historique.ancien_statut = historique.nouveau_statut
        historique.nouveau_statut = colis.statut
    historique.timestamp = datetime.utcnow()
    

    db.commit()
    db.refresh(colis)
    db.refresh(historique)
    
    return colis
    
    
    
    
    
def colis_search(db:Session, zone_name:str):
    return db.query(Colis).join(Zone).filter(Zone.nom == zone_name).all()
    
    
     
    
    
    
    
    
    
    