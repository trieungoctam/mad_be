from typing import List, Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import or_, and_, func, desc, update, delete

from app.models.product import Product, Category, Brand
from app.models.user import SearchHistory
from app.schemas.search import SearchHistoryCreate


async def search_products(
    db: AsyncSession,
    query: str,
    user_id: Optional[int] = None,
    category_id: Optional[int] = None,
    brand_id: Optional[int] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    sort_by: str = "relevance",  # relevance, price_asc, price_desc, name_asc
    limit: int = 20,
    offset: int = 0
) -> Dict[str, Any]:
    """
    Search for products with various filtering and sorting options
    """
    # Format the search term for LIKE queries
    search_term = f"%{query}%"

    # Build the base search condition
    search_condition = or_(
        Product.product_name.ilike(search_term),
        Product.description.ilike(search_term),
        Product.barcode == query  # Exact match for barcode
    )

    # Add additional filters
    filters = [search_condition]

    if category_id:
        filters.append(Product.category_id == category_id)

    if brand_id:
        filters.append(Product.brand_id == brand_id)

    if min_price is not None:
        filters.append(Product.default_price >= min_price)

    if max_price is not None:
        filters.append(Product.default_price <= max_price)

    # Count total results
    count_result = await db.execute(
        select(func.count()).select_from(
            select(Product).where(and_(*filters)).subquery()
        )
    )
    total_count = count_result.scalar_one()

    # Determine sorting
    if sort_by == "price_asc":
        order_clause = Product.default_price.asc()
    elif sort_by == "price_desc":
        order_clause = Product.default_price.desc()
    elif sort_by == "name_asc":
        order_clause = Product.product_name.asc()
    else:  # Default to relevance
        # For relevance, we could use a more sophisticated ranking algorithm
        # Here we'll just use the name match as primary factor
        order_clause = Product.product_name.ilike(f"{query}%").desc()

    # Execute the query with sorting
    result = await db.execute(
        select(Product)
        .where(and_(*filters))
        .order_by(order_clause)
        .limit(limit)
        .offset(offset)
    )

    products = result.scalars().all()

    # If user is authenticated, log the search
    if user_id:
        # Only log searches that returned results or had a meaningful query
        if len(query.strip()) > 2 and (total_count > 0 or len(products) > 0):
            selected_product_id = products[0].id if products else None
            await log_search_history(
                db=db,
                user_id=user_id,
                search_query=query,
                result_count=total_count,
                selected_product_id=selected_product_id
            )

    return {
        "items": products,
        "total": total_count,
        "limit": limit,
        "offset": offset,
        "query": query,
        "filters": {
            "category_id": category_id,
            "brand_id": brand_id,
            "price_range": [min_price, max_price]
        }
    }


async def log_search_history(
    db: AsyncSession,
    user_id: int,
    search_query: str,
    result_count: int,
    selected_product_id: Optional[int] = None
) -> SearchHistory:
    """
    Log a search query to user's search history
    """
    db_search_history = SearchHistory(
        user_id=user_id,
        search_query=search_query,
        result_count=result_count,
        selected_product_id=selected_product_id
    )
    db.add(db_search_history)
    await db.commit()
    await db.refresh(db_search_history)

    return db_search_history


async def get_user_search_history(
    db: AsyncSession,
    user_id: int,
    limit: int = 10,
    offset: int = 0
) -> List[SearchHistory]:
    """
    Get a user's search history
    """
    result = await db.execute(
        select(SearchHistory)
        .where(SearchHistory.user_id == user_id)
        .order_by(desc(SearchHistory.search_date))
        .limit(limit)
        .offset(offset)
    )

    return result.scalars().all()


async def clear_search_history(db: AsyncSession, user_id: int) -> int:
    """
    Clear a user's search history
    Returns the number of items deleted
    """
    result = await db.execute(
        select(SearchHistory)
        .where(SearchHistory.user_id == user_id)
    )

    search_history = result.scalars().all()
    count = len(search_history)

    for item in search_history:
        await db.delete(item)

    await db.commit()

    return count


async def get_trending_searches(db: AsyncSession, limit: int = 10) -> List[Dict[str, Any]]:
    """
    Get trending searches based on frequency and recency
    """
    # This is a simplified implementation. In a real app, we would use a more sophisticated
    # algorithm that considers both frequency and recency.

    from datetime import datetime, timedelta

    # Get searches from the last 7 days
    cutoff_date = datetime.utcnow() - timedelta(days=7)

    result = await db.execute(
        select(
            SearchHistory.search_query,
            func.count(SearchHistory.id).label("count")
        )
        .where(SearchHistory.search_date >= cutoff_date)
        .group_by(SearchHistory.search_query)
        .order_by(desc("count"))
        .limit(limit)
    )

    trending = []
    for row in result:
        trending.append({
            "query": row.search_query,
            "count": row.count
        })

    return trending