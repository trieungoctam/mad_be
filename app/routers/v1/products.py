from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status, Body
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.deps import get_current_active_user, get_current_superuser, get_current_active_user_optional
from app.db.session import get_db
from app.models.user import User
from app.models.product import ProductImage
from app.schemas.base import PaginationParams
from app.schemas.product import (
    Product,
    ProductCompare,
    ProductCreate,
    ProductPaginated,
    ProductUpdate,
    ProductVariantCreate,
    ProductVariantUpdate,
    ProductImageCreate
)
from app.services.product import (
    add_product_variant,
    add_product_image,
    add_to_favorites,
    compare_product_prices,
    create_product,
    delete_product,
    get_product_variant,
    get_user_favorites,
    get_product,
    get_products,
    get_product_by_barcode,
    get_product_by_category,
    is_favorite,
    update_product_variant,
    remove_from_favorites,
    update_product,
    search_products
)

router = APIRouter()


@router.get("/", response_model=None)
async def read_products(
    pagination: PaginationParams = Depends(),
    category_id: Optional[int] = None,
    brand_id: Optional[int] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    search: Optional[str] = None,
    db: AsyncSession = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_active_user_optional),
) -> Any:
    """
    Get all products with filtering and pagination
    """
    return await get_products(
        db=db,
        skip=(pagination.page - 1) * pagination.limit,
        limit=pagination.limit,
        category_id=category_id,
        brand_id=brand_id,
        min_price=min_price,
        max_price=max_price,
        search=search,
    )


@router.post(
    "/", response_model=None, status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(get_current_superuser)]
)
async def create_new_product(
    db: AsyncSession = Depends(get_db),
    product_in: ProductCreate = Body(...),
    current_user: User = Depends(get_current_active_user),
):
    """
    Create a new product
    """
    # TODO: Add validation for admin/staff role

    try:
        product = await create_product(db=db, product=product_in, user_id=current_user.id)
        return product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get("/{product_id}", response_model=None)
async def read_product(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_active_user_optional),
) -> Any:
    """
    Get product by ID
    """
    product = await get_product(db=db, product_id=product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    return product


@router.put(
    "/{product_id}", response_model=None,
    dependencies=[Depends(get_current_superuser)]
)
async def update_product_details(
    product_id: int,
    product_update: ProductUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_superuser),
) -> Any:
    """
    Update a product (admin only)
    """
    product = await get_product(db=db, product_id=product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    try:
        updated_product = await update_product(
            db=db,
            product=product,
            product_update=product_update,
            user_id=current_user.id
        )
        return updated_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.delete(
    "/{product_id}", status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(get_current_superuser)]
)
async def delete_product_item(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_superuser),
) -> None:
    """
    Delete a product (admin only)
    """
    product = await get_product(db=db, product_id=product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    await delete_product(db=db, product=product, user_id=current_user.id)

@router.get("/{product_id}/variants", response_model=None)
async def get_product_variants_endpoint(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_active_user_optional),
) -> Any:
    """
    Get all variants of a product
    """
    product = await get_product(db=db, product_id=product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    variants = await get_product_variants(db=db, product_id=product_id)
    return variants


@router.post("/{product_id}/variants", response_model=None, status_code=status.HTTP_201_CREATED)
async def add_product_variant_endpoint(
    product_id: int,
    variant_in: ProductVariantCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_superuser),
) -> Any:
    """
    Add a variant to a product (admin only)
    """
    # Ensure the product_id in the path matches the one in the request body
    if variant_in.product_id != product_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product ID in path does not match product ID in request body"
        )

    try:
        variant = await add_product_variant(db=db, variant=variant_in, user_id=current_user.id)
        return variant
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.put("/{product_id}/variants/{variant_id}", response_model=None)
async def update_product_variant_endpoint(
    product_id: int,
    variant_id: int,
    variant_update: ProductVariantUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_superuser),
) -> Any:
    """
    Update a product variant (admin only)
    """
    variant = await get_product_variant(db=db, variant_id=variant_id)
    if not variant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Variant not found",
        )

    # Check if the variant belongs to the specified product
    if variant.product_id != product_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Variant does not belong to the specified product"
        )

    try:
        updated_variant = await update_product_variant(
            db=db,
            variant=variant,
            variant_update=variant_update,
            user_id=current_user.id
        )
        return updated_variant
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.delete("/{product_id}/variants/{variant_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product_variant_endpoint(
    product_id: int,
    variant_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_superuser),
) -> None:
    """
    Delete a product variant (admin only)
    """
    variant = await get_product_variant(db=db, variant_id=variant_id)
    if not variant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Variant not found",
        )

    # Check if the variant belongs to the specified product
    if variant.product_id != product_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Variant does not belong to the specified product"
        )

    await delete_product_variant(db=db, variant=variant, user_id=current_user.id)


@router.get("/{product_id}/images", response_model=None)
async def get_product_images_endpoint(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_active_user_optional),
) -> Any:
    """
    Get all images of a product
    """
    product = await get_product(db=db, product_id=product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    images = await get_product_image(db=db, product_id=product_id)
    return images


@router.post("/{product_id}/images", response_model=None, status_code=status.HTTP_201_CREATED)
async def add_product_image_endpoint(
    product_id: int,
    image_data: ProductImageCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_superuser),
) -> Any:
    """
    Add an image to a product (admin only)
    """
    # Ensure the product_id in the path matches the one in the request body
    if image_data.product_id != product_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product ID in path does not match product ID in request body"
        )

    # Check if product exists
    product = await get_product(db=db, product_id=product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    try:
        # Create a new ProductImage instance
        db_image = ProductImage(
            product_id=product_id,
            image_url=image_data.image_url,
            is_primary=image_data.is_primary
        )
        db.add(db_image)
        await db.commit()
        await db.refresh(db_image)

        return {
            "id": db_image.id,
            "product_id": db_image.product_id,
            "image_url": db_image.image_url,
            "is_primary": db_image.is_primary,
            "upload_date": db_image.upload_date
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get("/barcode/{barcode}", response_model=None)
async def read_product_by_barcode(
    barcode: str,
    db: AsyncSession = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_active_user_optional),
) -> Any:
    """
    Get product by barcode
    """
    product = await get_product_by_barcode(db=db, barcode=barcode)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    return product


@router.get("/compare/", response_model=Any)
async def compare_multiple_products(
    product_ids: List[int] = Query(..., description="List of product IDs to compare"),
    currency: str = Query("VND", description="Currency for price comparison"),
    db: AsyncSession = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_active_user),
) -> Any:
    """
    Compare prices of multiple products across different stores
    """
    if not product_ids:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="At least one product ID is required"
        )

    comparison = await compare_product_prices(
        db=db,
        product_ids=product_ids,
        currency=currency
    )

    return comparison


@router.get("/search/", response_model=None)
async def search_product(
    query: str,
    category_id: Optional[int] = None,
    brand_id: Optional[int] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    sort_by: Optional[str] = "name",
    sort_order: Optional[str] = "asc",
    include_details: bool = False,
    pagination: PaginationParams = Depends(),
    db: AsyncSession = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_active_user_optional),
) -> Any:
    """
    Search for products with detailed filtering
    """
    return await search_products(
        db=db,
        query=query,
        category_id=category_id,
        brand_id=brand_id,
        min_price=min_price,
        max_price=max_price,
        sort_by=sort_by,
        sort_order=sort_order,
        include_details=include_details,
        limit=pagination.limit,
        offset=(pagination.page - 1) * pagination.limit,
    )


@router.get("/category/{category_id}", response_model=None)
async def get_products_by_category(
    category_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_active_user_optional),
) -> Any:
    """
    Get all products in a category, its parent category (if exists), and its subcategories

    This endpoint returns:
    - Products from the specified category
    - Products from the parent category (if exists)
    - Products from all subcategories
    - Information about the category, its parent, and its subcategories
    """
    result = await get_product_by_category(db=db, category_id=category_id)

    if not result["category"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )

    return result


# Favorites endpoints
@router.get("/favorites/", response_model=None)
async def read_favorite_products(
    pagination: PaginationParams = Depends(),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get current user's favorite products
    """
    return await get_user_favorites(
        db=db,
        user_id=current_user.id,
        skip=(pagination.page - 1) * pagination.limit,
        limit=pagination.limit
    )


@router.post("/favorites/{product_id}", response_model=None)
async def add_product_to_favorites(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Add a product to favorites
    """
    # Check if product exists
    product = await get_product(db=db, product_id=product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    # Check if already in favorites
    if await is_favorite(db=db, user_id=current_user.id, product_id=product_id):
        return {"success": True, "message": "Product already in favorites"}

    await add_to_favorites(db=db, user_id=current_user.id, product_id=product_id)
    return {"success": True, "message": "Product added to favorites"}


@router.delete("/favorites/{product_id}", response_model=None)
async def remove_product_from_favorites(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Remove a product from favorites
    """
    # Check if in favorites
    if not await is_favorite(db=db, user_id=current_user.id, product_id=product_id):
        return {"success": True, "message": "Product not in favorites"}

    await remove_from_favorites(db=db, user_id=current_user.id, product_id=product_id)
    return {"success": True, "message": "Product removed from favorites"}