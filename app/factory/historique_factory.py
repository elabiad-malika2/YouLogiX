from sqlalchemy.orm import Session
from app.models.historique import HistoriqueStatut
from app.models.colis import Colis
from app.core.database import SessionLocal
from datetime import datetime, timedelta
import random


def create_historique(db: Session):
    """Create sample status history for packages"""
    # Get existing colis
    colis_list = db.query(Colis).all()

    if not colis_list:
        print("⚠ No colis found. Please run colis_factory first.")
        return []

    # Status progression patterns
    status_flows = {
        "créé": [],
        "en_transit": [{"ancien": "créé", "nouveau": "en_transit"}],
        "en_cours_de_livraison": [
            {"ancien": "créé", "nouveau": "en_transit"},
            {"ancien": "en_transit", "nouveau": "en_cours_de_livraison"}
        ],
        "livré": [
            {"ancien": "créé", "nouveau": "en_transit"},
            {"ancien": "en_transit", "nouveau": "en_cours_de_livraison"},
            {"ancien": "en_cours_de_livraison", "nouveau": "livré"}
        ]
    }

    historiques = []
    for colis in colis_list:
        current_status = colis.statut
        flow = status_flows.get(current_status, [])
        
        # Create history entries based on the current status
        base_time = datetime.utcnow() - timedelta(days=random.randint(1, 7))
        
        for i, status_change in enumerate(flow):
            # Add some time between each status change
            timestamp = base_time + timedelta(hours=random.randint(2, 12) * (i + 1))
            
            historique = HistoriqueStatut(
                id_colis=colis.id,
                ancien_statut=status_change["ancien"],
                nouveau_statut=status_change["nouveau"],
                timestamp=timestamp
            )
            db.add(historique)
            historiques.append(historique)
    
    db.commit()
    for historique in historiques:
        db.refresh(historique)
    
    print(f"✓ Created {len(historiques)} historique entries")
    return historiques


if __name__ == "__main__":
    db = SessionLocal()
    try:
        create_historique(db)
    finally:
        db.close()
