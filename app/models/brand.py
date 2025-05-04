from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Brand(Base):
    """Product brands information"""
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True, index=True)
    brand_name = Column(String(100), nullable=False, index=True)
    description = Column(Text)
    logo_url = Column(String(255))
    website = Column(String(255))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    products = relationship("Product", back_populates="brand")