import re
import json
import logging
import secrets
from datetime import datetime
from typing import Dict, Any, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete

from app.models.payment_setting import PaymentSettings as PaymentSetting
from app.models.order import Order
from app.models.transaction import TransactionHistory, TransactionStatus, TransactionType
from app.schemas.payment import (
    PaymentSettingCreate,
    PaymentSettingUpdate,
    PaymentRequest,
    PaymentResponse,
    BankCardDetails
)
from app.services.order import update_payment_status, create_transaction

# Set up logging
logger = logging.getLogger(__name__)


async def get_order_transactions(db: AsyncSession, order_id: int) -> List[TransactionHistory]:
    """
    Get all transactions for a specific order
    """
    result = await db.execute(
        select(TransactionHistory)
        .where(TransactionHistory.order_id == order_id)
    )
    return result.scalars().all()


async def get_user_transactions(db: AsyncSession, user_id: int, limit: int = 10, offset: int = 0) -> List[TransactionHistory]:
    """
    Get transactions for a specific user
    """
    # Get all orders for the user
    order_result = await db.execute(
        select(Order.id)
        .where(Order.user_id == user_id)
    )
    order_ids = [order_id for order_id, in order_result]

    if not order_ids:
        return []

    # Get transactions for these orders
    result = await db.execute(
        select(TransactionHistory)
        .where(TransactionHistory.order_id.in_(order_ids))
        .order_by(TransactionHistory.transaction_date.desc())
        .limit(limit)
        .offset(offset)
    )
    return result.scalars().all()


async def create_payment_setting(db: AsyncSession, payment_setting: PaymentSettingCreate, user_id: int) -> PaymentSetting:
    """
    Create a new payment setting for a user
    """
    # Check if this is the first payment method for the user
    result = await db.execute(
        select(PaymentSetting)
        .where(PaymentSetting.user_id == user_id)
    )
    existing_settings = result.scalars().all()

    # Set as default if this is the first payment method
    is_default = len(existing_settings) == 0

    # Create the payment setting
    db_payment_setting = PaymentSetting(
        user_id=user_id,
        payment_method=payment_setting.payment_method,
        payment_details=payment_setting.payment_details,  # Note: These should be encrypted in a real app
        is_default=is_default
    )
    db.add(db_payment_setting)
    await db.commit()
    await db.refresh(db_payment_setting)

    return db_payment_setting


async def save_bank_card(db: AsyncSession, card_details: Dict[str, str], user_id: int) -> PaymentSetting:
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
    is_valid, error_message = validate_bank_card(card_details)
    if not is_valid:
        raise ValueError(f"Invalid card details: {error_message}")

    # Mask card number for storage
    masked_card = mask_card_number(card_details.get("card_number", ""))

    # Store minimal card details for reference
    payment_details = {
        "card_last4": card_details.get("card_number", "")[-4:],
        "card_holder": card_details.get("card_holder_name", ""),
        "card_brand": detect_card_brand(card_details.get("card_number", "")),
        "expiry_month": card_details.get("expiry_month", ""),
        "expiry_year": card_details.get("expiry_year", ""),
        # Store masked card number for display purposes
        "masked_card_number": masked_card
    }

    # Create payment setting
    payment_setting = PaymentSettingCreate(
        payment_method="bank_card",
        payment_details=json.dumps(payment_details)
    )

    return await create_payment_setting(db, payment_setting, user_id)


async def get_payment_settings(db: AsyncSession, user_id: int) -> List[PaymentSetting]:
    """
    Get all payment settings for a user
    """
    result = await db.execute(
        select(PaymentSetting)
        .where(PaymentSetting.user_id == user_id)
    )
    return result.scalars().all()


async def get_payment_setting(db: AsyncSession, payment_setting_id: int) -> Optional[PaymentSetting]:
    """
    Get a payment setting by ID
    """
    result = await db.execute(select(PaymentSetting).where(PaymentSetting.id == payment_setting_id))
    return result.scalars().first()


async def update_payment_setting(
    db: AsyncSession, payment_setting: PaymentSetting, payment_setting_update: PaymentSettingUpdate, user_id: int
) -> PaymentSetting:
    """
    Update a payment setting
    """
    update_data = payment_setting_update.dict(exclude_unset=True)

    # If setting this as default, unset other default settings
    if update_data.get("is_default") == True:
        await db.execute(
            update(PaymentSetting)
            .where(PaymentSetting.user_id == user_id)
            .where(PaymentSetting.id != payment_setting.id)
            .values(is_default=False)
        )

    for field, value in update_data.items():
        setattr(payment_setting, field, value)

    await db.commit()
    await db.refresh(payment_setting)

    return payment_setting


async def delete_payment_setting(db: AsyncSession, payment_setting: PaymentSetting, user_id: int) -> None:
    """
    Delete a payment setting
    """
    # If this is the default payment method, set another one as default if available
    if payment_setting.is_default:
        result = await db.execute(
            select(PaymentSetting)
            .where(PaymentSetting.user_id == user_id)
            .where(PaymentSetting.id != payment_setting.id)
        )
        other_settings = result.scalars().all()

        if other_settings:
            other_settings[0].is_default = True

    # Delete the payment setting
    await db.delete(payment_setting)
    await db.commit()


def validate_bank_card(card_details: Dict[str, str]) -> tuple[bool, str]:
    """
    Validate bank card details

    Args:
        card_details: Dictionary containing card details

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Extract card details
    card_number = card_details.get("card_number", "").replace(" ", "")
    card_holder = card_details.get("card_holder_name", "")
    expiry_month = card_details.get("expiry_month", "")
    expiry_year = card_details.get("expiry_year", "")
    cvv = card_details.get("cvv", "")

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
    order: Order,
    card_details: Dict[str, str],
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
    is_valid, error_message = validate_bank_card(card_details)

    if not is_valid:
        logger.warning(f"Invalid card details for order {order.id}: {error_message}")
        return PaymentResponse(
            success=False,
            message=f"Payment failed: {error_message}",
            order_id=order.id,
            payment_status=order.payment_status
        )

    # In a real implementation, this would call a payment gateway API
    # For this simulation, we'll generate a transaction ID and assume success

    # Generate a transaction reference (in real app, this would come from payment gateway)
    transaction_ref = f"BANK-{secrets.token_hex(6).upper()}"

    # Mask card number for logging and storage
    masked_card = mask_card_number(card_details.get("card_number", ""))

    # Log the payment attempt (with masked card number)
    logger.info(
        f"Processing bank card payment for order {order.id}: "
        f"Amount: {order.total_amount}, Card: {masked_card}, Ref: {transaction_ref}"
    )

    # Store minimal card details for reference
    payment_details = {
        "card_last4": card_details.get("card_number", "")[-4:],
        "card_brand": detect_card_brand(card_details.get("card_number", "")),
        "transaction_ref": transaction_ref
    }

    # Create transaction record
    transaction = await create_transaction(
        db=db,
        transaction=dict(
            order_id=order.id,
            transaction_type=TransactionType.PAYMENT,
            amount=order.total_amount,
            payment_method="bank_card",
            status=TransactionStatus.SUCCESS,
            # Store minimal card details as JSON string
            payment_details=json.dumps(payment_details)
        ),
        user_id=user_id
    )

    # Update order payment status
    await update_payment_status(db, order, "completed", user_id)

    return PaymentResponse(
        success=True,
        message="Bank card payment successful",
        transaction_id=transaction.id,
        payment_status="completed",
        order_id=order.id
    )


def detect_card_brand(card_number: str) -> str:
    """
    Detect the card brand based on the card number

    Args:
        card_number: Card number

    Returns:
        Card brand name
    """
    card_number = card_number.replace(" ", "")

    # Common card brand patterns
    patterns = {
        "Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",
        "Mastercard": r"^5[1-5][0-9]{14}$",
        "American Express": r"^3[47][0-9]{13}$",
        "Discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$",
        "JCB": r"^(?:2131|1800|35\d{3})\d{11}$"
    }

    for brand, pattern in patterns.items():
        if re.match(pattern, card_number):
            return brand

    return "Unknown"


async def process_payment(
    db: AsyncSession, order: Order, payment_request: PaymentRequest, user_id: int
) -> PaymentResponse:
    """
    Process a payment for an order

    This function routes the payment to the appropriate processor based on the payment method.

    Args:
        db: Database session
        order: Order to process payment for
        payment_request: Payment request details
        user_id: ID of the user making the payment

    Returns:
        Payment response
    """
    # Check if the order is already paid
    if order.payment_status == "completed":
        return PaymentResponse(
            success=False,
            message="Order is already paid",
            transaction_id=None,
            payment_status="completed",
            order_id=order.id
        )

    # Get the payment method details if using saved payment method
    payment_method = payment_request.payment_method
    payment_details = payment_request.payment_details

    if payment_request.payment_setting_id:
        result = await db.execute(
            select(PaymentSetting)
            .where(PaymentSetting.id == payment_request.payment_setting_id)
            .where(PaymentSetting.user_id == user_id)
        )
        payment_setting = result.scalars().first()

        if payment_setting:
            payment_method = payment_setting.payment_method
            payment_details = json.loads(payment_setting.payment_details)

    # Route to appropriate payment processor based on payment method
    if payment_method == "bank_card":
        return await process_bank_card_payment(db, order, payment_details, user_id)
    elif payment_method == "cod":
        # Cash on delivery - mark as pending payment
        transaction = await create_transaction(
            db=db,
            transaction=dict(
                order_id=order.id,
                transaction_type=TransactionType.PAYMENT,
                amount=order.total_amount,
                payment_method="cod",
                status=TransactionStatus.PENDING
            ),
            user_id=user_id
        )

        return PaymentResponse(
            success=True,
            message="Order placed with Cash on Delivery",
            transaction_id=transaction.id,
            payment_status="pending",
            order_id=order.id
        )
    else:
        # Generic payment processor for other methods
        # In a real app, this would integrate with various payment gateways

        # Create a transaction record
        transaction = await create_transaction(
            db=db,
            transaction=dict(
                order_id=order.id,
                transaction_type=TransactionType.PAYMENT,
                amount=order.total_amount,
                payment_method=payment_method,
                status=TransactionStatus.SUCCESS
            ),
            user_id=user_id
        )

        # Update the order payment status
        await update_payment_status(db, order, "completed", user_id)

        return PaymentResponse(
            success=True,
            message=f"Payment successful via {payment_method}",
            transaction_id=transaction.id,
            payment_status="completed",
            order_id=order.id
        )