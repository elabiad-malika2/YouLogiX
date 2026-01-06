from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class HistoriqueStatut(Base):
    __tablename__ = "historique_statuts"
    id = Column(Integer, primary_key=True, index=True)
    id_colis = Column(Integer, ForeignKey("colis.id"))
    ancien_statut = Column(String)
    nouveau_statut = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    colis = relationship("Colis", back_populates="historique")