-- Migration to remove shopping list functionality

-- First remove foreign key constraints
ALTER TABLE IF EXISTS barcode_scan_history
    DROP CONSTRAINT IF EXISTS barcode_scan_history_shopping_list_id_fkey;

-- Drop shared_lists table
DROP TABLE IF EXISTS shared_lists;

-- Drop list_items table
DROP TABLE IF EXISTS list_items;

-- Drop shopping_lists table
DROP TABLE IF EXISTS shopping_lists;

-- Add migration record
INSERT INTO migration_history (migration_name, status)
VALUES ('remove_shopping_list', 'completed');