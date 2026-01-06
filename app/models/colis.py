from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Colis(Base):
    __tablename__ = "colis"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    poids = Column(Float)
    statut = Column(String, default="créé")
    ville_destination = Column(String)

    # Foreign Keys
    id_expediteur = Column(Integer, ForeignKey("expediteurs.id"))
    id_destinataire = Column(Integer, ForeignKey("destinataires.id"))
    id_livreur = Column(Integer, ForeignKey("livreurs.id"), nullable=True)
    id_zone = Column(Integer, ForeignKey("zones.id"))
    id_gestionnaire = Column(Integer, ForeignKey("gestionnaires.id"))

    # Relationships
    expediteur = relationship("Expediteur", back_populates="colis")
    destinataire = relationship("Destinataire", back_populates="colis")
    livreur = relationship("Livreur", back_populates="colis")
    zone = relationship("Zone", back_populates="colis")
    gestionnaire = relationship("Gestionnaire", back_populates="colis_crees")
    historique = relationship("HistoriqueStatut", back_populates="colis")