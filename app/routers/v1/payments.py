from typing import Any, List, Dict

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.deps import get_current_active_user
from app.db.session import get_db
from app.models.order import Order
from app.models.transaction import TransactionStatus
from app.models.user import User
from app.schemas.base import BaseAPIResponse
from app.schemas.payment import (
    BankCardDetails,
    PaymentResponse,
    Transaction,
    TransactionPaginated,
)
from app.schemas.order import OrderIn, OrderCreate
from app.schemas.card import NewCard, Card
from app.schemas.payment import PaymentSchema
from app.models.payment import Payment
from app.services.payment import (
    get_order_transactions,
    process_bank_card_payment as service_process_bank_card_payment,
    save_bank_card,
    get_cards_by_user_id,
)
from app.services.order import get_order
from app.services.order import create_order

router = APIRouter()


@router.post("/bank-card", response_model=NewCard, status_code=status.HTTP_201_CREATED)
async def save_bank_card_setting(
    card_details: BankCardDetails,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Save a bank card as a payment method

    This endpoint validates the card details and saves them securely.
    Only minimal card information is stored for reference.
    """
    try:
        # Save the bank card
        return await save_bank_card(db=db, card_details=card_details, user_id=current_user.id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/cards", response_model=List[Card])
async def get_cards(db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_active_user)) -> Any:
    """
    Get all cards for a user
    """
    return await get_cards_by_user_id(db=db, user_id=current_user.id)

@router.post("/process-payment/card/{card_id}", response_model=PaymentResponse)
async def process_bank_card_payment(
    card_id: int,
    order_in: OrderIn,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Process a bank card payment for an order

    This endpoint provides a dedicated path for bank card payments with proper validation.
    """
    # Get the order
    result = await db.execute(select(Card).where(Card.id == card_id))
    card = result.scalar_one_or_none()
    if not card:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Card not found"
        )
    # Check if card belongs to current user
    if card.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to use this card"
        )

    # Check for existing payment with same idempotency key
    payment_result = await db.execute(select(Payment).where(Payment.idempotency_key == order_in.idempotency_key))
    payment = payment_result.scalar_one_or_none()
    if not payment:
        # No existing payment found, create a new one
        try:
            # Create card_dict for payment processing
            card_dict = {
                "card_number": card.card_number,
                "card_holder_name": card.card_holder_name,
                "expiry_month": card.expiry_month,
                "expiry_year": card.expiry_year,
                "cvv": order_in.cvv
            }

            # Create initial payment record with pending status
            payment = Payment(
                idempotency_key=order_in.idempotency_key,
                amount=order_in.total_amount,
                status='pending',
                user_id=current_user.id,
                card_id=card_id,
                order_id=None  # Will be updated after order creation
            )
            db.add(payment)
            await db.commit()
            await db.refresh(payment)

            # Process the payment
            payment_result = await service_process_bank_card_payment(
                db=db,
                card_dict=card_dict,
                total_amount=order_in.total_amount,
                user_id=current_user.id
            )

            # Update payment status based on processing result
            payment.status = payment_result['payment_status']
            await db.commit()
            await db.refresh(payment)

            return {
                'success': payment_result['success'],
                'status': payment_result['payment_status'],
                'message': payment_result['message'],
                'amount': payment.amount,
                'idempotency_key': payment.idempotency_key
            }

        except Exception as e:
            # If any error occurs during processing, roll back and mark as failed
            await db.rollback()

            if payment and payment.id:
                payment.status = 'failed'
                payment.error_message = str(e)
                await db.commit()

            return {
                'success': False,
                'status': 'failed',
                'message': f"Payment processing failed: {str(e)}",
                'amount': order_in.total_amount,
                'idempotency_key': order_in.idempotency_key
            }
    else:
        # Payment with this idempotency key already exists
        # Return its current status without reprocessing
        if payment.status == 'pending':
            # Payment still being processed, inform client
            return {
                'success': False,
                'status': 'pending',
                'message': 'Payment is being processed',
                'amount': payment.amount,
                'idempotency_key': payment.idempotency_key
            }

        elif payment.status == 'failed':
            # Previous attempt failed
            return {
                'success': False,
                'status': 'failed',
                'message': payment.error_message or 'Previous payment attempt failed',
                'amount': payment.amount,
                'idempotency_key': payment.idempotency_key
            }
        else:
            # Payment succeeded previously
            payment_result = {
                'success': True,
                'status': payment.status,
                'amount': payment.amount,
                'idempotency_key': payment.idempotency_key
            }

    # If payment successful, create order if not already created
    if payment_result.get('status') == 'success' or payment.status == 'success':
        try:
            if not payment.order_id:
                order_create = OrderCreate(
                    items=order_in.items,
                    shipping_address_id=order_in.shipping_address_id,
                    payment_method='card',
                    payment_status='pending',
                    user_id=current_user.id
                )
                order = await create_order(db=db, order_in=order_create, user_id=current_user.id)
                # Update payment with order ID
                payment.order_id = order.id
                await db.commit()

            return {
                'success': True,
                'status': 'success',
                'message': 'Payment processed successfully',
                'amount': payment.amount,
                'order_id': payment.order_id,
                'idempotency_key': payment.idempotency_key
            }
        except Exception as e:
            # Order creation failed
            return {
                'success': False,
                'status': 'payment_succeeded_order_failed',
                'message': f"Payment succeeded but order creation failed: {str(e)}",
                'amount': payment.amount,
                'idempotency_key': payment.idempotency_key
            }

    # Payment failed
    return {
        'success': False,
        'status': payment_result.get('status', 'failed'),
        'message': payment_result.get('message', 'Payment processing failed'),
        'amount': payment.amount,
        'idempotency_key': payment.idempotency_key
    }


# @router.post("/process-payment/cod", response_model=PaymentResponse)
# async def process_cod_payment(
#     order_in: OrderIn,
#     db: AsyncSession = Depends(get_db),
#     current_user: User = Depends(get_current_active_user),
# ) -> Any:
#     """
#     Process a COD payment for an order
#     """
#     # Get the order
#     order = await get_order(db=db, order_id=order_id)
#     if not order:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Order not found"
#         )

#     # Check if order belongs to the current user
#     if order.user_id != current_user.id:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Not authorized to access this order"
#         )

#     # Check if order is already paid
#     if order.payment_status == "completed":
#         return PaymentResponse(
#             success=False,
#             message="Order is already paid",
#             transaction_id=None,
#             payment_status="completed",
#             order_id=order.id
#         )

#     return PaymentResponse(
#         success=True,
#         message="COD payment processed successfully",
#         transaction_id=None,
#         payment_status="pending",
#         order_id=order.id
#     )

@router.get("/transactions/order/{order_id}", response_model=List[PaymentSchema])
async def read_order_transactions(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get transactions for a specific order
    """
    return await get_order_transactions(db=db, order_id=order_id)