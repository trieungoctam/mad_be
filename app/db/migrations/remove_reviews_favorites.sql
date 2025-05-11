-- Migration to remove favorites and product reviews

-- Drop favorites table
DROP TABLE IF EXISTS favorites;

-- Drop product_reviews table
DROP TABLE IF EXISTS product_reviews;

-- Add migration record (if migration_history table exists)
INSERT INTO migration_history (migration_name, status)
VALUES ('remove_reviews_favorites', 'completed');