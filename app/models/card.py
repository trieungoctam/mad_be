from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, DateTime, func
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Card(Base):
    """User payment settings - card details, preferred payment methods"""
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    card_holder_name = Column(String(50), nullable=False)
    card_number = Column(String(50), nullable=False)  # credit_card, paypal, etc.
    expiry_month = Column(Integer, nullable=False)
    expiry_year = Column(Integer, nullable=False)
    is_default = Column(Boolean, default=False)

    # Relationships
    user = relationship("User", back_populates="cards")