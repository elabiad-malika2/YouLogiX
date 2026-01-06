from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Expediteur(Base):
    __tablename__ = "expediteurs"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    prenom = Column(String)
    email = Column(String, unique=True)
    telephone = Column(String)
    adresse = Column(String)

    colis = relationship("Colis", back_populates="expediteur")