from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Destinataire(Base):
    __tablename__ = "destinataires"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    prenom = Column(String)
    email = Column(String)
    telephone = Column(String)
    adresse = Column(String)

    colis = relationship("Colis", back_populates="destinataire")