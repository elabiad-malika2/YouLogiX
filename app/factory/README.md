# Factory Module

This module contains factory files to seed the database with sample data for testing and development.

## Structure

- `zone_factory.py` - Creates sample zones/delivery areas
- `livreur_factory.py` - Creates sample delivery drivers
- `gestionnaire_factory.py` - Creates sample managers
- `expediteur_factory.py` - Creates sample senders
- `destinataire_factory.py` - Creates sample recipients
- `colis_factory.py` - Creates sample packages with relationships
- `historique_factory.py` - Creates status history for packages
- `seed_all.py` - Main script to seed all tables in correct order

## Usage

### Seed All Tables

To populate all tables with sample data, run:

```bash
python -m app.factory.seed_all
```

This will:
1. Create database tables if they don't exist
2. Insert sample data in the correct order (respecting foreign key dependencies)
3. Avoid duplicates (checks before inserting)

### Seed Individual Tables

You can also seed individual tables:

```bash
# Seed only zones
python -m app.factory.zone_factory

# Seed only livreurs
python -m app.factory.livreur_factory

# Seed only colis (requires other tables to be populated first)
python -m app.factory.colis_factory
```

## Sample Data Overview

- **8 Zones**: Different areas in Rabat with postal codes
- **6 Livreurs**: Delivery drivers with different vehicle types
- **3 Gestionnaires**: Package managers
- **5 Expediteurs**: Senders (shops and individuals)
- **8 Destinataires**: Recipients with contact information
- **12 Colis**: Packages with various statuses and relationships
- **Historique**: Status change history for all packages

## Notes

- Factories check for existing records to avoid duplicates
- Run `seed_all.py` to ensure proper order of insertion
- Foreign key relationships are automatically created
- All data uses Moroccan names, addresses, and phone numbers
