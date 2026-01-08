from sqlalchemy.orm import Session

from app.models.colis import Colis 
from app.schemas.colis_schema import ColisCreate

# Module Colis (Le plus gros morceau) :
# Controller colis_controller.py :
# Fonction creer_colis : Création simple.
# Fonction assigner_livreur : Lier un colis à un livreur.
# Fonction mettre_a_jour_statut : Trés important -> Cette fonction doit aussi créer automatiquement une ligne dans la table HistoriqueStatut à chaque changement.
# Filtres avancés : Pouvoir lister les colis par Statut ou par Zone.



def create_colis_logic(db:Session, colis_in:ColisCreate):
    db_colis = Colis(
        description = colis_in.description,
        poids = colis_in.poids,
        ville_destination = colis_in.ville_destination,
        id_expediteur = colis_in.id_expediteur,
        id_destinataire = colis_in.id_destinataire,
        id_zone = colis_in.id_zone,
        id_gestionnaire = colis_in.id_gestionnaire,
        statut = "créé",
    )
    
    db.add(db_colis)
    db.commit()
    db.refresh(db_colis)
    
    return db_colis 


def assign_colis(db:Session, colis_id:int, livreur_id:int):
    
    colis = db.query(Colis).filter(Colis.id == colis_id).first()
    
    if not colis:
        return False
    
    colis.id_livreur = livreur_id 
    colis.statut = "en_cours_de_livraison"
    db.commit()
    db.refresh(colis)
    
    return colis