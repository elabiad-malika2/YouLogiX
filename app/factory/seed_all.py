"""
Main script to seed all tables with sample data
Run this script to populate the database with test data
"""
from app.core.database import SessionLocal, engine, Base
from app.factory.zone_factory import create_zones
from app.factory.livreur_factory import create_livreurs
from app.factory.gestionnaire_factory import create_gestionnaires
from app.factory.expediteur_factory import create_expediteurs
from app.factory.destinataire_factory import create_destinataires
from app.factory.colis_factory import create_colis
from app.factory.historique_factory import create_historique

# Import all models to ensure they're registered with Base
from app.models.zone import Zone
from app.models.livreur import Livreur
from app.models.gestionnaire import Gestionnaire
from app.models.expediteur import Expediteur
from app.models.destinataire import Destinataire
from app.models.colis import Colis
from app.models.historique import HistoriqueStatut


def seed_database():
    """Seed the database with all sample data"""
    print("=" * 60)
    print("🌱 Starting database seeding...")
    print("=" * 60)
    
    # Create tables if they don't exist
    print("\n📋 Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✓ Tables created successfully\n")
    
    db = SessionLocal()
    try:
        # Seed in order of dependencies
        print("1️⃣  Seeding Zones...")
        create_zones(db)
        
        print("\n2️⃣  Seeding Livreurs...")
        create_livreurs(db)
        
        print("\n3️⃣  Seeding Gestionnaires...")
        create_gestionnaires(db)
        
        print("\n4️⃣  Seeding Expediteurs...")
        create_expediteurs(db)
        
        print("\n5️⃣  Seeding Destinataires...")
        create_destinataires(db)
        
        print("\n6️⃣  Seeding Colis...")
        create_colis(db)
        
        print("\n7️⃣  Seeding Historique Statuts...")
        create_historique(db)
        
        print("\n" + "=" * 60)
        print("✅ Database seeding completed successfully!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Error during seeding: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
