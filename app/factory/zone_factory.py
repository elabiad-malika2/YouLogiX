from sqlalchemy.orm import Session
from app.models.zone import Zone
from app.core.database import SessionLocal


def create_zones(db: Session):
    """Create sample zones"""
    zones_data = [
        {"nom": "Centre Ville", "code_postal": 10000},
        {"nom": "Agdal", "code_postal": 10090},
        {"nom": "Hassan", "code_postal": 10020},
        {"nom": "Hay Riad", "code_postal": 10100},
        {"nom": "Souissi", "code_postal": 10170},
        {"nom": "Yacoub El Mansour", "code_postal": 10050},
        {"nom": "Takaddoum", "code_postal": 10110},
        {"nom": "Akkari", "code_postal": 10150},
    ]

    zones = []
    for zone_data in zones_data:
        # Check if zone already exists
        existing_zone = db.query(Zone).filter(Zone.nom == zone_data["nom"]).first()
        if not existing_zone:
            zone = Zone(**zone_data)
            db.add(zone)
            zones.append(zone)
        else:
            zones.append(existing_zone)
    
    db.commit()
    for zone in zones:
        db.refresh(zone)
    
    print(f"✓ Created {len(zones_data)} zones")
    return zones


if __name__ == "__main__":
    db = SessionLocal()
    try:
        create_zones(db)
    finally:
        db.close()
