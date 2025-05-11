import fastapi
from typing import List, Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import or_, and_, func, desc, update, delete
from sqlalchemy.orm import selectinload
from math import ceil

from app.models.product import Product, ProductVariant, ProductImage
from app.models.user import User
from app.models.category import Category
from app.models.brand import Brand
from app.schemas.product import (
    ProductCreate, ProductUpdate,
    CategoryCreate, CategoryUpdate, BrandCreate, BrandUpdate,
    ProductVariantCreate, ProductVariantUpdate, ProductVariant as ProductVariantSchema
)

async def get_all_brands(db: AsyncSession) -> List[Dict[str, Any]]:
    """
    Get all brands
    """
    result = await db.execute(select(Brand))
    brands = result.scalars().all()
    return [
        {
            "id": brand.id,
            "name": brand.brand_name,
            "description": brand.description,
        }
        for brand in brands
    ]

async def get_all_categories(db: AsyncSession) -> List[Dict[str, Any]]:
    """
    Get all categories
    """
    result = await db.execute(select(Category).where(Category.parent_id == None).order_by(Category.category_name))
    categories = result.scalars().all()
    return [
        {
            "id": category.id,
            "name": category.category_name,
            "description": category.description,
        }
        for category in categories
    ]


async def get_product_variants(db: AsyncSession, product_id: int) -> List[Dict[str, Any]]:
    """
    Get all variants for a product

    Args:
        db: Database session
        product_id: ID of the product to get variants for

    Returns:
        List of dictionaries containing product variant data
    """
    result = await db.execute(select(ProductVariant).where(ProductVariant.product_id == product_id))
    variants = result.scalars().all()

    # Convert SQLAlchemy objects to dictionaries
    return [
        {
            "id": variant.id,
            "product_id": variant.product_id,
            "size": variant.size,
            "stock": variant.stock,
            "created_at": variant.created_at,
            "updated_at": variant.updated_at
        }
        for variant in variants
    ]

async def get_product_variant(db: AsyncSession, variant_id: int) -> Optional[Dict[str, Any]]:
    """
    Get a product variant by ID

    Args:
        db: Database session
        variant_id: ID of the variant to get

    Returns:
        Dictionary containing product variant data or None if not found
    """
    result = await db.execute(select(ProductVariant).where(ProductVariant.id == variant_id))
    variant = result.scalars().first()

    if not variant:
        return None

    # Convert SQLAlchemy object to dictionary
    return {
        "id": variant.id,
        "product_id": variant.product_id,
        "size": variant.size,
        "stock": variant.stock,
        "created_at": variant.created_at,
        "updated_at": variant.updated_at
    }

async def add_product_variant(db: AsyncSession, variant: ProductVariantCreate, user_id: int) -> Dict[str, Any]:
    """
    Add a variant for a product

    Args:
        db: Database session
        variant: Product variant data
        user_id: ID of the user performing the action

    Returns:
        Dictionary containing created product variant data

    Raises:
        ValueError: If product does not exist or variant with same size already exists
    """
    # Check if product exists
    product = await get_product(db, variant.product_id)
    if not product:
        raise ValueError(f"Product with ID {variant.product_id} does not exist")

    # Check if variant with same size already exists
    existing_variants = await get_product_variants(db, variant.product_id)
    for existing in existing_variants:
        if existing["size"].lower() == variant.size.lower():
            raise ValueError(f"Variant with size '{variant.size}' already exists for this product")

    db_variant = ProductVariant(
        product_id=variant.product_id,
        size=variant.size,
        stock=variant.stock
    )
    db.add(db_variant)
    await db.commit()
    await db.refresh(db_variant)

    # Convert SQLAlchemy object to dictionary
    return {
        "id": db_variant.id,
        "product_id": db_variant.product_id,
        "size": db_variant.size,
        "stock": db_variant.stock,
        "created_at": db_variant.created_at,
        "updated_at": db_variant.updated_at
    }

async def update_product_variant(
    db: AsyncSession, variant: ProductVariant, variant_update: ProductVariantUpdate, user_id: int
) -> Dict[str, Any]:
    """
    Update a product variant

    Args:
        db: Database session
        variant: Product variant to update
        variant_update: Updated variant data
        user_id: ID of the user performing the action

    Returns:
        Dictionary containing updated product variant data

    Raises:
        ValueError: If trying to update to a size that already exists
    """
    update_data = variant_update.model_dump(exclude_unset=True)

    # If size is being updated, check for duplicates
    if "size" in update_data and update_data["size"] != variant.size:
        existing_variants = await get_product_variants(db, variant.product_id)
        for existing in existing_variants:
            if existing["id"] != variant.id and existing["size"].lower() == update_data["size"].lower():
                raise ValueError(f"Variant with size '{update_data['size']}' already exists for this product")

    for field, value in update_data.items():
        setattr(variant, field, value)

    await db.commit()
    await db.refresh(variant)

    # Convert SQLAlchemy object to dictionary
    return {
        "id": variant.id,
        "product_id": variant.product_id,
        "size": variant.size,
        "stock": variant.stock,
        "created_at": variant.created_at,
        "updated_at": variant.updated_at
    }

async def delete_product_variant(db: AsyncSession, variant: ProductVariant, user_id: int) -> None:
    """
    Delete a product variant

    Args:
        db: Database session
        variant: Product variant to delete
        user_id: ID of the user performing the action
    """
    await db.execute(delete(ProductVariant).where(ProductVariant.id == variant.id))
    await db.commit()

# Product methods
async def create_product(db: AsyncSession, product: ProductCreate, user_id: int) -> Product:
    """
    Create a new product
    """
    # Check if barcode already exists (if provided)
    if product.barcode:
        existing_product = await get_product_by_barcode(db, product.barcode)
        if existing_product:
            raise ValueError(f"Product with barcode {product.barcode} already exists")

    db_product = Product(
        barcode=product.barcode,
        brand_id=product.brand_id,
        product_name=product.product_name,
        description=product.description,
        price=product.price,
        category_id=product.category_id
    )
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)

    # Fetch the newly created product with all related data
    result = await db.execute(
        select(Product)
        .where(Product.id == db_product.id)
        .options(
            selectinload(Product.variants),
            selectinload(Product.images)
        )
    )
    created_product = result.scalars().first()

    # Convert to Pydantic model
    return created_product


async def get_product(db: AsyncSession, product_id: int) -> Optional[Product]:
    """
    Get a product by ID
    """
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalars().first()

    product_variants = await get_product_variants(db, product.id)
    product_images = await get_product_image(db, product.id)
    # Create a dictionary from product
    product_dict = {
        "id": product.id,
        "barcode": product.barcode,
        "product_name": product.product_name,
        "description": product.description,
        "price": product.price,
        "category_id": product.category_id,
        "brand_id": product.brand_id,
        "created_at": product.created_at,
        "updated_at": product.updated_at,
        "quantity": product.quantity,
        "variants": product_variants,
        "images": product_images
    }

    return product_dict


async def get_products(
    db: AsyncSession,
    skip: int = 0,
    limit: int = 10,
    category_id: Optional[int] = None,
    brand_id: Optional[int] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    search: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get all products with filtering and pagination
    """
    query = select(Product)

    # Apply filters if provided
    if category_id is not None:
        query = query.where(Product.category_id == category_id)
    if brand_id is not None:
        query = query.where(Product.brand_id == brand_id)
    if min_price is not None:
        query = query.where(Product.price >= min_price)
    if max_price is not None:
        query = query.where(Product.price <= max_price)
    if search is not None and search.strip():
        query = query.where(Product.product_name.ilike(f"%{search}%"))

    # Count total results
    count_query = select(func.count()).select_from(query.subquery())
    total_count = await db.execute(count_query)
    total = total_count.scalar() or 0

    # Calculate total pages
    pages = ceil(total / limit) if limit > 0 else 0

    # Apply pagination
    query = query.offset(skip).limit(limit)

    result = await db.execute(query)
    products = result.scalars().all()

    # Create a list of products with complete information
    product_list = []
    for product in products:
        # Get variants and images
        product_variants = await get_product_variants(db, product.id)
        print("Done get product variants")
        product_images = await get_product_image(db, product.id)
        print("Done get product images")

        # Create a dictionary from product
        product_dict = {
            "id": product.id,
            "barcode": product.barcode,
            "product_name": product.product_name,
            "description": product.description,
            "price": product.price,
            "category_id": product.category_id,
            "brand_id": product.brand_id,
            "created_at": product.created_at,
            "updated_at": product.updated_at,
            "quantity": product.quantity,
            "variants": product_variants,
            "images": product_images
        }
        product_list.append(product_dict)

    # Format the response to match the expected ProductPaginated schema
    return {
        "data": product_list,
        "page": skip // limit + 1 if limit > 0 else 1,
        "limit": limit,
        "total": total,
        "pages": pages
    }


async def add_product_image(db: AsyncSession, product_id: int, image_url: str) -> Product:
    """
    Add an image to a product
    """
    product = await db.get(Product, product_id)
    if not product:
        raise ValueError(f"Product with ID {product_id} not found")

    db_image = ProductImage(product_id=product_id, image_url=image_url)
    db.add(db_image)
    await db.commit()
    await db.refresh(product)
    return product

async def get_product_image(db: AsyncSession, product_id: int) -> List[Dict[str, Any]]:
    """
    Get images for a product
    """
    result = await db.execute(select(ProductImage).where(ProductImage.product_id == product_id))
    images = result.scalars().all()

    # Convert SQLAlchemy objects to dictionaries
    return [
        {
            "id": image.id,
            "product_id": image.product_id,
            "image_url": image.image_url,
            "is_primary": image.is_primary,
            "upload_date": image.upload_date
        }
        for image in images
    ]

async def get_product_by_barcode(db: AsyncSession, barcode: str) -> Optional[Dict[str, Any]]:
    """
    Get a product by barcode

    Args:
        db: Database session
        barcode: Product barcode to search for

    Returns:
        Dictionary with product information and variants, or None if not found
    """
    result = await db.execute(select(Product).where(Product.barcode == barcode))
    product = result.scalars().first()

    if not product:
        return None

    # Get variants and images
    variants = await get_product_variants(db, product.id)
    images = await get_product_image(db, product.id)

    # Create a dictionary with product data
    return {
        "id": product.id,
        "barcode": product.barcode,
        "product_name": product.product_name,
        "description": product.description,
        "price": product.price,
        "category_id": product.category_id,
        "brand_id": product.brand_id,
        "created_at": product.created_at,
        "updated_at": product.updated_at,
        "quantity": product.quantity,
        "variants": variants,
        "images": images
    }


async def update_product(
    db: AsyncSession, product: Product, product_update: ProductUpdate, user_id: int
) -> Product:
    """
    Update a product
    """
    update_data = product_update.dict(exclude_unset=True)

    # Validate foreign keys if they are provided
    if "brand_id" in update_data and update_data["brand_id"] is not None:
        brand_id = update_data["brand_id"]
        if brand_id != 0:  # Skip validation if 0
            brand = await db.execute(select(Brand).where(Brand.id == brand_id))
            if not brand.scalars().first():
                raise ValueError(f"Brand with ID {brand_id} does not exist")
        else:
            # Set to None if 0 to avoid foreign key constraint violation
            update_data["brand_id"] = None

    if "category_id" in update_data and update_data["category_id"] is not None:
        category_id = update_data["category_id"]
        if category_id != 0:  # Skip validation if 0
            category = await db.execute(select(Category).where(Category.id == category_id))
            if not category.scalars().first():
                raise ValueError(f"Category with ID {category_id} does not exist")
        else:
            # Set to None if 0 to avoid foreign key constraint violation
            update_data["category_id"] = None

    # Apply updates
    for field, value in update_data.items():
        setattr(product, field, value)

    await db.commit()
    await db.refresh(product)

    return product


async def delete_product(db: AsyncSession, product: Product, user_id: int) -> None:
    """
    Delete a product
    """
    product_name = product.product_name
    product_id = product.id

    await db.execute(delete(Product).where(Product.id == product_id))
    await db.commit()


# Comment out favorites-related functions
"""
async def is_favorite(db: AsyncSession, user_id: int, product_id: int) -> bool:
    '''
    Check if a product is in user's favorites
    '''
    result = await db.execute(
        select(Favorite)
        .where(Favorite.user_id == user_id)
        .where(Favorite.product_id == product_id)
    )
    return result.scalars().first() is not None


async def add_to_favorites(db: AsyncSession, user_id: int, product_id: int) -> Favorite:
    '''
    Add a product to user's favorites
    '''
    # Check if already in favorites
    result = await db.execute(
        select(Favorite)
        .where(Favorite.user_id == user_id)
        .where(Favorite.product_id == product_id)
    )
    existing = result.scalars().first()
    if existing:
        return existing

    # Add to favorites
    db_favorite = Favorite(
        user_id=user_id,
        product_id=product_id
    )
    db.add(db_favorite)
    await db.commit()
    await db.refresh(db_favorite)

    return db_favorite


async def remove_from_favorites(db: AsyncSession, user_id: int, product_id: int) -> None:
    '''
    Remove a product from user's favorites
    '''
    await db.execute(
        delete(Favorite)
        .where(Favorite.user_id == user_id)
        .where(Favorite.product_id == product_id)
    )
    await db.commit()


async def get_user_favorites(
    db: AsyncSession,
    user_id: int,
    skip: int = 0,
    limit: int = 10
) -> Dict[str, Any]:
    '''
    Get all favorite products for a user with pagination
    '''
    # Get favorites with products
    query = (
        select(Product)
        .join(Favorite, Favorite.product_id == Product.id)
        .where(Favorite.user_id == user_id)
        .order_by(Favorite.added_at.desc())
        .offset(skip)
        .limit(limit)
    )

    # Count total favorites
    count_query = (
        select(func.count())
        .select_from(Favorite)
        .where(Favorite.user_id == user_id)
    )

    result = await db.execute(query)
    products = result.scalars().all()

    count_result = await db.execute(count_query)
    total = count_result.scalar()

    # Get additional details for each product
    result_products = []
    for product in products:
        product_variant = await get_product_variants(db, product.id)
        product_dict = {
            "id": product.id,
            "barcode": product.barcode,
            "product_name": product.product_name,
            "description": product.description,
            "price": product.price,
            "category_id": product.category_id,
            "brand_id": product.brand_id,
            "created_at": product.created_at,
            "updated_at": product.updated_at,
            "quantity": product.quantity,
            "variants": product_variant
        }
        result_products.append(product_dict)

    # Calculate pagination details
    pages = ceil(total / limit) if limit > 0 else 0

    return {
        "data": result_products,
        "total": total,
        "page": skip // limit + 1 if limit > 0 else 1,
        "pages": pages,
        "limit": limit
    }
"""

# Category and Brand methods
async def create_category(db: AsyncSession, category: CategoryCreate, user_id: int) -> Category:
    """
    Create a new product category
    """
    db_category = Category(
        category_name=category.name,
        description=category.description,
        parent_id=category.parent_id,
        image_url=category.image_url
    )
    db.add(db_category)
    await db.commit()
    await db.refresh(db_category)

    return db_category


async def create_brand(db: AsyncSession, brand: BrandCreate, user_id: int) -> Brand:
    """
    Create a new product brand
    """
    db_brand = Brand(
        brand_name=brand.name,
        description=brand.description,
        logo_url=brand.logo_url,
        website=brand.website
    )
    db.add(db_brand)
    await db.commit()
    await db.refresh(db_brand)

    return db_brand


async def compare_product_prices(
    db: AsyncSession,
    product_ids: List[int],
    currency: str = "VND"
) -> Dict[str, Any]:
    """
    Compare prices of multiple products across different stores

    Args:
        db: Database session
        product_ids: List of product IDs to compare
        currency: Filter prices by currency (default: VND)

    Returns:
        Dictionary with product information and price comparison across stores
    """
    if not product_ids:
        return {"products": [], "comparison": {}}

    # Get product details
    products = {}
    for product_id in product_ids:
        product = await get_product(db, product_id)
        if product:
            products[product_id] = product

    if not products:
        return {"products": [], "comparison": {}}

    # Get all prices for these products
    all_prices = []

    for product_id in products:
        price_list = await db.execute(
            select(ProductPrice)
            .where(ProductPrice.product_id == product_id)
            .where(ProductPrice.currency == currency)
            .order_by(ProductPrice.price)
        )
        prices = price_list.scalars().all()
        all_prices.extend(prices)

    # Build comparison data
    comparison = {}
    for product_id in comparison:
        comparison[product_id] = {
            "product": product,
        }

    # Find best price for each product
    for product_id in comparison:
        best_price = None

        comparison[product_id]["best_price"] = {
            "price": best_price,

        } if best_price is not None else None

    return {
        "products": list(products.values()),
        "comparison": comparison
    }

async def get_product_by_category(db: AsyncSession, category_id: int) -> Dict[str, Any]:
    """
    Get all products in a category and its subcategories

    If the category has a parent, also include products from the parent category

    Args:
        db: Database session
        category_id: ID of the category to get products for

    Returns:
        Dictionary with products and category information
    """
    # First, get the category to check if it has a parent
    category_result = await db.execute(select(Category).where(Category.id == category_id))
    category = category_result.scalars().first()

    if not category:
        return {
            "products": [],
            "category": None,
            "total": 0
        }

    # Initialize list of category IDs to include in the query
    category_ids = [category_id]

    # Check if category has a parent
    parent_category = None
    if category.parent_id:
        parent_result = await db.execute(select(Category).where(Category.parent_id == category.parent_id))
        parent_category = parent_result.scalars().first()
        if parent_category:
            category_ids.append(parent_category.id)

    # Get all child categories
    child_result = await db.execute(select(Category).where(Category.parent_id == category_id))
    child_categories = child_result.scalars().all()

    # Add child category IDs to the list
    for child in child_categories:
        category_ids.append(child.id)

    # Query products from all relevant categories
    query = select(Product).where(Product.category_id.in_(category_ids))
    result = await db.execute(query)
    products = result.scalars().all()

    # Create a list of products with complete information
    product_list = []
    for product in products:
        # Get variants and images
        product_variants = await get_product_variants(db, product.id)
        product_images = await get_product_image(db, product.id)

        # Create a dictionary from product
        product_dict = {
            "id": product.id,
            "barcode": product.barcode,
            "product_name": product.product_name,
            "description": product.description,
            "price": product.price,
            "category_id": product.category_id,
            "brand_id": product.brand_id,
            "created_at": product.created_at,
            "updated_at": product.updated_at,
            "quantity": product.quantity,
            "variants": product_variants,
            "images": product_images
        }
        product_list.append(product_dict)

    # Format category information
    category_info = {
        "id": category.id,
        "name": category.category_name,
        "description": category.description,
        "image_url": category.image_url,
        "parent_id": category.parent_id
    }


    # Return formatted response
    return {
        "products": product_list,
        "category": category_info,
        "total": len(product_list)
    }

async def get_parent_categories(db: AsyncSession) -> List[Category]:
    """
    Get all parent categories
    """
    result = await db.execute(select(Category).where(Category.parent_id == None))
    return result.scalars().all()