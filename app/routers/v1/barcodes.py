from typing import Any, List

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status, Body
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.deps import get_current_active_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.barcode import (
    BarcodeScan,
    BarcodeScanCreate,
    BarcodeScanHistoryPaginated,
    BarcodeScanResult,
)
from app.schemas.base import PaginationParams
from app.services.barcode import (
    create_barcode_scan_history,
    get_barcode_scan_history,
    process_barcode,
    scan_barcode_from_image,
)

router = APIRouter()


@router.post("/scan", response_model=BarcodeScanResult)
async def scan_barcode(
    image: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Scan barcode from uploaded image (Deprecated)
    """
    try:
        # Process the image and scan barcode
        result = await scan_barcode_from_image(image, db)

        # Record the scan in history only if barcode was found
        if result.barcode:
            scan_in = BarcodeScanCreate(
                barcode=result.barcode,
                product_id=result.product.id if result.product_found else None,
            )
            await create_barcode_scan_history(db=db, user_id=current_user.id, scan_in=scan_in)

        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to process barcode: {str(e)}",
        )


@router.post("/process", response_model=BarcodeScanResult)
async def process_barcode_string(
    barcode: str = Body(..., embed=True),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Process barcode string (pre-processed by mobile device)
    """
    try:
        # Process the barcode string
        result = await process_barcode(barcode, db)

        # Record the scan in history
        if result.barcode:
            scan_in = BarcodeScanCreate(
                barcode=result.barcode,
                product_id=result.product.id if result.product_found else None,
            )
            await create_barcode_scan_history(db=db, user_id=current_user.id, scan_in=scan_in)

        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to process barcode: {str(e)}",
        )


@router.post("/manual", response_model=BarcodeScanResult)
async def scan_barcode_manual(
    barcode: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Manual barcode input
    """
    # Look up product by barcode
    # ...

    # Record the scan in history
    scan_in = BarcodeScanCreate(barcode=barcode, product_id=None)  # Set product_id if found
    await create_barcode_scan_history(db=db, user_id=current_user.id, scan_in=scan_in)

    return BarcodeScanResult(
        barcode=barcode,
        product_found=False,  # Set to True if product found
        message="Barcode recorded",
    )


@router.get("/history", response_model=BarcodeScanHistoryPaginated)
async def read_barcode_history(
    pagination: PaginationParams = Depends(),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get current user's barcode scan history
    """
    return await get_barcode_scan_history(db=db, user_id=current_user.id, pagination=pagination)