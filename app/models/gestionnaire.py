from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Gestionnaire(Base):
    __tablename__ = "gestionnaires"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    prenom = Column(String)
    telephone = Column(String)

    colis_crees = relationship("Colis", back_populates="gestionnaire")