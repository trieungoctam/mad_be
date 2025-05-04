# Cấu trúc Cơ sở dữ liệu

## Bảng `users`
- `id`: UUID (primary key)
- `email`: VARCHAR(255) (unique)
- `hashed_password`: VARCHAR(255)
- `full_name`: VARCHAR(255)
- `phone_number`: VARCHAR(20)
- `is_active`: BOOLEAN
- `is_superuser`: BOOLEAN
- `created_at`: TIMESTAMP
- `updated_at`: TIMESTAMP

## Bảng `addresses`
- `id`: UUID (primary key)
- `user_id`: UUID (foreign key -> users.id)
- `address_line1`: VARCHAR(255)
- `address_line2`: VARCHAR(255) (nullable)
- `city`: VARCHAR(100)
- `district`: VARCHAR(100)
- `ward`: VARCHAR(100)
- `postal_code`: VARCHAR(20)
- `is_default`: BOOLEAN
- `created_at`: TIMESTAMP
- `updated_at`: TIMESTAMP

## Bảng `shopping_lists`
- `id`: UUID (primary key)
- `user_id`: UUID (foreign key -> users.id)
- `name`: VARCHAR(255)
- `description`: TEXT (nullable)
- `is_public`: BOOLEAN
- `created_at`: TIMESTAMP
- `updated_at`: TIMESTAMP

## Bảng `shopping_list_items`
- `id`: UUID (primary key)
- `shopping_list_id`: UUID (foreign key -> shopping_lists.id)
- `product_id`: UUID (foreign key -> products.id) (nullable)
- `name`: VARCHAR(255)
- `quantity`: INTEGER
- `unit`: VARCHAR(50) (nullable)
- `note`: TEXT (nullable)
- `is_completed`: BOOLEAN
- `created_at`: TIMESTAMP
- `updated_at`: TIMESTAMP

## Bảng `shopping_list_shares`
- `id`: UUID (primary key)
- `shopping_list_id`: UUID (foreign key -> shopping_lists.id)
- `user_id`: UUID (foreign key -> users.id)
- `can_edit`: BOOLEAN
- `created_at`: TIMESTAMP
- `updated_at`: TIMESTAMP

## Bảng `barcode_scans`
- `id`: UUID (primary key)
- `user_id`: UUID (foreign key -> users.id)
- `barcode`: VARCHAR(100)
- `product_id`: UUID (foreign key -> products.id) (nullable)
- `scanned_at`: TIMESTAMP
- `source`: VARCHAR(50) (e.g., 'scan', 'manual')

## Bảng `products`
- `id`: UUID (primary key)
- `name`: VARCHAR(255)
- `description`: TEXT (nullable)
- `barcode`: VARCHAR(100) (nullable, indexed)
- `image_url`: VARCHAR(255) (nullable)
- `category`: VARCHAR(100) (nullable)
- `brand`: VARCHAR(100) (nullable)
- `unit`: VARCHAR(50) (nullable)
- `price`: DECIMAL(10, 2) (nullable)
- `currency`: VARCHAR(3) (default 'VND')
- `in_stock`: BOOLEAN
- `created_at`: TIMESTAMP
- `updated_at`: TIMESTAMP

## Bảng `product_stores`
- `id`: UUID (primary key)
- `product_id`: UUID (foreign key -> products.id)
- `store_name`: VARCHAR(255)
- `price`: DECIMAL(10, 2)
- `currency`: VARCHAR(3) (default 'VND')
- `url`: VARCHAR(255) (nullable)
- `last_updated`: TIMESTAMP

## Bảng `favorite_products`
- `id`: UUID (primary key)
- `user_id`: UUID (foreign key -> users.id)
- `product_id`: UUID (foreign key -> products.id)
- `created_at`: TIMESTAMP

## Bảng `carts`
- `id`: UUID (primary key)
- `user_id`: UUID (foreign key -> users.id)
- `created_at`: TIMESTAMP
- `updated_at`: TIMESTAMP

## Bảng `cart_items`
- `id`: UUID (primary key)
- `cart_id`: UUID (foreign key -> carts.id)
- `product_id`: UUID (foreign key -> products.id)
- `quantity`: INTEGER
- `price_at_addition`: DECIMAL(10, 2)
- `currency`: VARCHAR(3) (default 'VND')
- `added_at`: TIMESTAMP
- `updated_at`: TIMESTAMP

## Bảng `orders`
- `id`: UUID (primary key)
- `user_id`: UUID (foreign key -> users.id)
- `address_id`: UUID (foreign key -> addresses.id)
- `status`: VARCHAR(50) (e.g., 'pending', 'processing', 'shipped', 'delivered', 'cancelled')
- `total_amount`: DECIMAL(10, 2)
- `currency`: VARCHAR(3) (default 'VND')
- `payment_status`: VARCHAR(50) (e.g., 'pending', 'paid', 'failed')
- `shipping_fee`: DECIMAL(10, 2)
- `discount_amount`: DECIMAL(10, 2) (default 0)
- `notes`: TEXT (nullable)
- `tracking_number`: VARCHAR(100) (nullable)
- `created_at`: TIMESTAMP
- `updated_at`: TIMESTAMP

## Bảng `order_items`
- `id`: UUID (primary key)
- `order_id`: UUID (foreign key -> orders.id)
- `product_id`: UUID (foreign key -> products.id)
- `quantity`: INTEGER
- `unit_price`: DECIMAL(10, 2)
- `currency`: VARCHAR(3) (default 'VND')
- `total_price`: DECIMAL(10, 2)
- `created_at`: TIMESTAMP

## Bảng `payment_settings`
- `id`: UUID (primary key)
- `user_id`: UUID (foreign key -> users.id)
- `provider`: VARCHAR(100) (e.g., 'credit_card', 'paypal', 'momo')
- `account_number`: VARCHAR(255) (nullable)
- `is_default`: BOOLEAN
- `expires_at`: TIMESTAMP (nullable)
- `meta_data`: JSONB (nullable)
- `created_at`: TIMESTAMP
- `updated_at`: TIMESTAMP

## Bảng `payment_transactions`
- `id`: UUID (primary key)
- `order_id`: UUID (foreign key -> orders.id)
- `user_id`: UUID (foreign key -> users.id)
- `payment_setting_id`: UUID (foreign key -> payment_settings.id) (nullable)
- `amount`: DECIMAL(10, 2)
- `currency`: VARCHAR(3) (default 'VND')
- `status`: VARCHAR(50) (e.g., 'pending', 'completed', 'failed')
- `provider_transaction_id`: VARCHAR(255) (nullable)
- `provider`: VARCHAR(100)
- `meta_data`: JSONB (nullable)
- `created_at`: TIMESTAMP
- `updated_at`: TIMESTAMP

## Bảng `notifications`
- `id`: UUID (primary key)
- `user_id`: UUID (foreign key -> users.id)
- `type`: VARCHAR(100) (e.g., 'order_status', 'promotion', 'system')
- `title`: VARCHAR(255)
- `content`: TEXT
- `is_read`: BOOLEAN (default false)
- `reference_id`: UUID (nullable, e.g., order_id)
- `reference_type`: VARCHAR(100) (nullable, e.g., 'order', 'product')
- `created_at`: TIMESTAMP

## Bảng `notification_settings`
- `id`: UUID (primary key)
- `user_id`: UUID (foreign key -> users.id)
- `order_updates`: BOOLEAN (default true)
- `promotions`: BOOLEAN (default true)
- `product_discounts`: BOOLEAN (default true)
- `newsletter`: BOOLEAN (default true)
- `email_notifications`: BOOLEAN (default true)
- `push_notifications`: BOOLEAN (default true)
- `updated_at`: TIMESTAMP