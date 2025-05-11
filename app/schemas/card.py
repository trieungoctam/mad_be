from app.schemas.base import BaseModel

class NewCard(BaseModel):
    card_holder_name: str
    card_number: str
    expiry_month: int
    expiry_year: int
    is_default: bool = False

class Card(BaseModel):
    id: int
    user_id: int
    card_holder_name: str
    card_number: str
    expiry_month: int
    expiry_year: int
    is_default: bool = False

