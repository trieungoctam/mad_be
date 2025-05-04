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
    PaymentRequest,
    PaymentResponse,
    PaymentSetting,
    PaymentSettingCreate,
    PaymentSettingUpdate,
    Transaction,
    TransactionPaginated,
)
from app.services.payment import (
    create_payment_setting,
    delete_payment_setting,
    get_order_transactions,
    get_payment_settings,
    get_user_transactions,
    process_payment,
    process_bank_card_payment,
    save_bank_card,
    update_payment_setting,
)
from app.services.order import get_order

router = APIRouter()


@router.get("/settings", response_model=List[PaymentSetting])
async def read_payment_settings(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get user's saved payment settings
    """
    return await get_payment_settings(db=db, user_id=current_user.id)


@router.post("/settings", response_model=PaymentSetting, status_code=status.HTTP_201_CREATED)
async def create_new_payment_setting(
    payment_in: PaymentSettingCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Create a new payment setting
    """
    return await create_payment_setting(db=db, user_id=current_user.id, payment_setting=payment_in)


@router.post("/settings/bank-card", response_model=PaymentSetting, status_code=status.HTTP_201_CREATED)
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
        # Convert Pydantic model to dict
        card_details_dict = card_details.dict()

        # Save the bank card
        return await save_bank_card(db=db, card_details=card_details_dict, user_id=current_user.id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.put("/settings/{setting_id}", response_model=PaymentSetting)
async def update_payment_settings(
    setting_id: int,
    payment_in: PaymentSettingUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Update a payment setting
    """
    return await update_payment_setting(
        db=db, user_id=current_user.id, setting_id=setting_id, payment_in=payment_in
    )


@router.delete("/settings/{setting_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_payment_settings(
    setting_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> None:
    """
    Delete a payment setting
    """
    await delete_payment_setting(db=db, user_id=current_user.id, setting_id=setting_id)


@router.post("/process", response_model=PaymentResponse)
async def process_order_payment(
    payment_request: PaymentRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Process payment for an order using the specified payment method
    """
    # Get the order
    order = await get_order(db=db, order_id=payment_request.order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )

    # Check if order belongs to the current user
    if order.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this order"
        )

    # Process payment
    payment_result = await process_payment(
        db=db,
        order=order,
        payment_request=payment_request,
        user_id=current_user.id
    )

    # Return payment response
    return payment_result


@router.post("/bank-card", response_model=PaymentResponse)
async def process_bank_card_payment_endpoint(
    order_id: int,
    card_details: BankCardDetails,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Process a bank card payment for an order

    This endpoint provides a dedicated path for bank card payments with proper validation.
    """
    # Get the order
    order = await get_order(db=db, order_id=order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )

    # Check if order belongs to the current user
    if order.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this order"
        )

    # Check if order is already paid
    if order.payment_status == "completed":
        return PaymentResponse(
            success=False,
            message="Order is already paid",
            transaction_id=None,
            payment_status="completed",
            order_id=order.id
        )

    # Convert Pydantic model to dict
    card_details_dict = card_details.dict()

    # Process bank card payment
    payment_result = await process_bank_card_payment(
        db=db,
        order=order,
        card_details=card_details_dict,
        user_id=current_user.id
    )

    return payment_result


@router.get("/transactions", response_model=TransactionPaginated)
async def read_transactions(
    pagination: int = 1,
    limit: int = 10,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get user's transaction history
    """
    return await get_user_transactions(
        db=db, user_id=current_user.id, limit=limit, offset=(pagination-1)*limit
    )


@router.get("/transactions/order/{order_id}", response_model=List[Transaction])
async def read_order_transactions(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get transactions for a specific order
    """
    return await get_order_transactions(db=db, order_id=order_id)