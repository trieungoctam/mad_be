import re
import json
import logging
import secrets
import hashlib
import urllib.parse
import hmac
from datetime import datetime, timedelta
import pytz
from typing import Dict, Any, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete

from app.models.payment import Payment
from app.models.card import Card
from app.models.order import Order
from app.models.transaction import TransactionStatus, TransactionType
from app.schemas.payment import (
    PaymentResponse,
    BankCardDetails
)
from app.schemas.card import NewCard, Card as CardSchema
from app.schemas.payment import PaymentSchema
from app.services.order import update_payment_status, create_transaction

# Set up logging
logger = logging.getLogger(__name__)


async def save_bank_card(db: AsyncSession, card_details: BankCardDetails, user_id: int) -> NewCard:
    """
    Save a bank card as a payment method

    Args:
        db: Database session
        card_details: Bank card details
        user_id: ID of the user

    Returns:
        Created payment setting

    Raises:
        ValueError: If card details are invalid
    """
    # Validate card details
    card_details_dict = {
        "card_number": card_details.card_number,
        "card_holder_name": card_details.card_holder_name,
        "expiry_month": card_details.expiry_month,
        "expiry_year": card_details.expiry_year,
        "cvv": card_details.cvv
    }
    is_valid, error_message = validate_bank_card(card_details_dict)
    if not is_valid:
        raise ValueError(f"Invalid card details: {error_message}")

    card = await db.execute(
        select(Card)
        .where(Card.user_id == user_id)
        .where(Card.card_number == card_details.card_number)
    )
    existing_card = card.scalars().first()

    if existing_card:
        raise ValueError("Card already exists")

    # Create card
    card = Card(
        user_id=user_id,
        card_holder_name=card_details.card_holder_name,
        card_number=card_details.card_number,
        expiry_month=int(card_details.expiry_month),
        expiry_year=int(card_details.expiry_year),
        is_default=False
    )

    db.add(card)
    await db.commit()
    await db.refresh(card)

    return NewCard(
        card_holder_name=card_details.card_holder_name,
        card_number=card_details.card_number,
        expiry_month=int(card_details.expiry_month),
        expiry_year=int(card_details.expiry_year)
    )


async def get_cards_by_user_id(db: AsyncSession, user_id: int) -> List[CardSchema]:
    """
    Get all cards for a user
    """
    result = await db.execute(
        select(Card)
        .where(Card.user_id == user_id)
    )

    cards = result.scalars().all()
    return [CardSchema(
        id=card.id,
        user_id=card.user_id,
        card_holder_name=card.card_holder_name,
        card_number=mask_card_number(card.card_number),
        expiry_month=card.expiry_month,
        expiry_year=card.expiry_year,
        is_default=card.is_default
    ) for card in cards]


async def get_card(db: AsyncSession, card_id: int) -> Optional[CardSchema]:
    """
    Get a card by ID
    """
    result = await db.execute(select(Card).where(Card.id == card_id))
    card = result.scalars().first()
    if card:
        return CardSchema(
            id=card.id,
            user_id=card.user_id,
            card_holder_name=card.card_holder_name,
            card_number=mask_card_number(card.card_number),
            expiry_month=card.expiry_month,
            expiry_year=card.expiry_year,
            is_default=card.is_default
        )
    return None


def validate_bank_card(card_details: Dict[str, str]) -> tuple[bool, str]:
    """
    Validate bank card details

    Args:
        card_details: BankCardDetails object

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Extract card details
    card_number = card_details.get("card_number").replace(" ", "")
    card_holder = card_details.get("card_holder_name")
    expiry_month = card_details.get("expiry_month")
    expiry_year = card_details.get("expiry_year")
    cvv = card_details.get("cvv")

    # Basic validation
    if not card_number or not card_number.isdigit():
        return False, "Invalid card number"

    if not card_holder:
        return False, "Card holder name is required"

    # Validate expiry date
    try:
        month = int(expiry_month)
        year = int(expiry_year)

        if not (1 <= month <= 12):
            return False, "Invalid expiry month"

        # Check if card is expired
        current_year = datetime.now().year
        current_month = datetime.now().month

        if year < current_year or (year == current_year and month < current_month):
            return False, "Card has expired"

    except ValueError:
        return False, "Invalid expiry date format"

    # Validate CVV (3-4 digits)
    cvv = str(cvv)
    if not cvv or not cvv.isdigit() or not (3 <= len(cvv) <= 4):
        return False, "Invalid CVV"

    # Luhn algorithm for card number validation (ISO/IEC 7812)
    # This is a standard checksum formula used by credit/debit card issuers
    # to validate card numbers and detect data entry errors
    digits = [int(d) for d in card_number]
    checksum = 0

    for i, digit in enumerate(reversed(digits)):
        if i % 2 == 1:  # Odd position (0-indexed from right)
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit

    if checksum % 10 != 0:
        return False, "Invalid card number (checksum failed)"

    return True, ""


def mask_card_number(card_number: str) -> str:
    """
    Mask a card number for secure logging and storage

    Args:
        card_number: Full card number

    Returns:
        Masked card number (e.g., "411111******1111")
    """
    if not card_number or len(card_number) < 13:
        return "****"

    # Keep first 6 and last 4 digits, mask the rest
    return f"{card_number[:6]}{'*' * (len(card_number) - 10)}{card_number[-4:]}"


async def process_bank_card_payment(
    db: AsyncSession,
    card_dict: dict,
    total_amount: int,
    user_id: int
) -> PaymentResponse:
    """
    Process a bank card payment

    Args:
        db: Database session
        order: Order to process payment for
        card_details: Bank card details
        user_id: ID of the user making the payment

    Returns:
        Payment response
    """
    # Validate card details
    is_valid, error_message = validate_bank_card(card_dict)

    if not is_valid:
        logger.warning(f"Invalid card details for card {card_dict['card_number']}: {error_message}")
        return PaymentResponse(
            success=False,
            message=f"Payment failed: {error_message}",
            payment_status="failed"
        )

    # In a real implementation, this would call a payment gateway API
    # For this simulation, we'll generate a transaction ID and assume success

    # Generate a transaction reference (in real app, this would come from payment gateway)

    # Mask card number for logging and storage
    masked_card = mask_card_number(card_dict.get("card_number", ""))

    # Log the payment attempt (with masked card number)
    logger.info(
        f"Processing bank card payment for card {card_dict['card_number']}: "
        f"Amount: {total_amount},"
        f"Card: {masked_card}"
    )

    # Store minimal card details for reference
    payment_details = {
        "card_last4": card_dict.get("card_number", "")[-4:],
        "card_brand": card_dict.get("card_number", "").split(" ")[0],
    }

    # Payment
    # Implement payment gateway API call here

    return PaymentResponse(
        success=True,
        message="Bank card payment successful",
        payment_status="completed",
    )

async def process_cod_payment(db: AsyncSession, order: Order, user_id: int) -> PaymentResponse:
    """
    Process a COD payment
    """
    await update_payment_status(db, order, "completed", user_id)

    return PaymentResponse(
        success=True,
        message="COD payment successful",
        transaction_id=None,
        payment_status="completed",
        order_id=order.id
    )



async def get_order_transactions(db: AsyncSession, order_id: int) -> List[PaymentSchema]:
    """
    Get all transactions for an order
    """
    result = await db.execute(select(Payment).where(Payment.order_id == order_id))
    return [PaymentSchema(
        id=payment.id,
        user_id=payment.user_id,
        card_id=payment.card_id,
        amount=payment.amount,
        status=payment.status,
        created_at=payment.created_at,
        updated_at=payment.updated_at
    ) for payment in result.scalars().all()]
