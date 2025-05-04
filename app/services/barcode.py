import io
from typing import List, Optional

from fastapi import UploadFile
# Remove dependency on pyzbar
# from pyzbar.pyzbar import decode
# from PIL import Image
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.barcode_scan_history import BarcodeScanHistory
from app.models.product import Product
from app.schemas.barcode import BarcodeScan, BarcodeScanCreate, BarcodeScanHistoryPaginated, BarcodeScanResult
from app.schemas.base import PaginationParams


# Replace the image scanning function with one that accepts a string barcode
async def process_barcode(
    barcode: str,
    db: AsyncSession
) -> BarcodeScanResult:
    """
    Process barcode string (pre-processed by mobile device)
    """
    # Look up product by barcode
    result = await db.execute(select(Product).where(Product.barcode == barcode))
    product = result.scalars().first()

    # Create response
    return BarcodeScanResult(
        barcode=barcode,
        product_found=bool(product),
        product=product if product else None
    )


# Keep this for backwards compatibility but mark as deprecated
async def scan_barcode_from_image(
    image: UploadFile,
    db: AsyncSession
) -> BarcodeScanResult:
    """
    DEPRECATED: This function is kept for backwards compatibility.
    Instead of scanning, it returns an error indicating to use the process_barcode endpoint.
    """
    # Return an empty result with an error message
    return BarcodeScanResult(
        barcode="",
        product_found=False,
        product=None,
        error="Image scanning is not supported. Use process_barcode endpoint with the barcode string."
    )


async def create_barcode_scan_history(
    db: AsyncSession,
    user_id: int,
    scan_in: BarcodeScanCreate
) -> BarcodeScanHistory:
    """
    Create a new barcode scan history entry
    """
    scan = BarcodeScanHistory(
        user_id=user_id,
        barcode=scan_in.barcode,
        product_id=scan_in.product_id,
        added_to_list_id=scan_in.added_to_list_id,
    )

    db.add(scan)
    await db.commit()
    await db.refresh(scan)

    return scan


async def get_barcode_scan_history(
    db: AsyncSession,
    user_id: int,
    pagination: PaginationParams,
) -> BarcodeScanHistoryPaginated:
    """
    Get user's barcode scan history
    """
    # Get total count
    result = await db.execute(
        select(BarcodeScanHistory).where(
            BarcodeScanHistory.user_id == user_id
        )
    )
    total = len(result.scalars().all())

    # Get paginated results
    result = await db.execute(
        select(BarcodeScanHistory)
        .where(BarcodeScanHistory.user_id == user_id)
        .order_by(BarcodeScanHistory.scanned_at.desc())
        .offset((pagination.page - 1) * pagination.limit)
        .limit(pagination.limit)
    )

    history = result.scalars().all()

    # Convert to BarcodeScan schemas with additional product info
    scans = []
    for scan in history:
        scan_data = BarcodeScan(
            id=scan.id,
            user_id=scan.user_id,
            barcode=scan.barcode,
            product_id=scan.product_id,
            scanned_at=scan.scanned_at,
            added_to_list_id=scan.added_to_list_id,
        )

        # Add product info if available
        if scan.product_id:
            product = await db.get(Product, scan.product_id)
            if product:
                scan_data.product_name = product.product_name
                scan_data.product_image = product.image_url

        scans.append(scan_data)

    # Calculate total pages
    total_pages = (total + pagination.limit - 1) // pagination.limit

    return BarcodeScanHistoryPaginated(
        success=True,
        message="Barcode scan history",
        data=scans,
        page=pagination.page,
        limit=pagination.limit,
        total=total,
        pages=total_pages,
    )