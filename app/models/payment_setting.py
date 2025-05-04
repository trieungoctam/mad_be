from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, DateTime, func
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class PaymentSettings(Base):
    """User payment settings - card details, preferred payment methods"""
    __tablename__ = "payment_settings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    payment_method = Column(String(50), nullable=False)  # credit_card, paypal, etc.
    payment_details = Column(Text, nullable=True)  # encrypted details
    is_default = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="payments")