-- Mock data for 100 products across different categories and brands

-- ELECTRONICS PRODUCTS (30 products)

-- Smartphones & Tablets (Category ID: 5, Parent: 1 - Đồ điện tử)
INSERT INTO products (barcode, brand_id, product_name, description, price, category_id, created_at, updated_at, quantity)
VALUES
('8801643598532', 2, 'Samsung Galaxy S23 Ultra', 'Flagship smartphone with 200MP camera and S Pen', 25990000, 5, NOW(), NOW(), 50),
('1902532185302', 1, 'iPhone 15 Pro Max', 'Apple''s premium smartphone with A17 Pro chip', 34990000, 5, NOW(), NOW(), 35),
('6934177768232', 3, 'Xiaomi 14 Pro', 'Flagship smartphone with Snapdragon 8 Gen 3', 19990000, 5, NOW(), NOW(), 45),
('6971408152226', 5, 'Xiaomi Redmi Note 13 Pro', 'Mid-range smartphone with 108MP camera', 7990000, 5, NOW(), NOW(), 60),
('8806094653953', 4, 'LG Velvet', 'Stylish smartphone with triple camera setup', 9990000, 5, NOW(), NOW(), 25),
('1902532185401', 1, 'iPad Pro 12.9 (2023)', 'Powerful tablet with M2 chip and Liquid Retina XDR display', 28990000, 5, NOW(), NOW(), 30),
('8806092991828', 2, 'Samsung Galaxy Tab S9 Ultra', 'Premium Android tablet with 14.6" AMOLED display', 24990000, 5, NOW(), NOW(), 20),
('6934177770303', 5, 'Xiaomi Pad 6', 'High-performance tablet with 11" 2.8K display', 8990000, 5, NOW(), NOW(), 40);

-- Laptops & Computers (Category ID: 6, Parent: 1 - Đồ điện tử)
INSERT INTO products (barcode, brand_id, product_name, description, price, category_id, created_at, updated_at, quantity)
VALUES
('1902532186012', 1, 'MacBook Pro 16" M3 Max', 'Professional laptop with powerful M3 Max chip', 79990000, 6, NOW(), NOW(), 15),
('1902532186029', 1, 'MacBook Air 13" M3', 'Thin and light laptop with M3 chip', 29990000, 6, NOW(), NOW(), 25),
('195553539838', 4, 'LG Gram 17', 'Ultra-lightweight 17" laptop with long battery life', 32990000, 6, NOW(), NOW(), 20),
('195553539845', 4, 'LG UltraGear Gaming Laptop', 'High-performance gaming laptop with RTX 4070', 39990000, 6, NOW(), NOW(), 15),
('195697627941', 2, 'Samsung Galaxy Book4 Pro', 'Premium 2-in-1 laptop with AMOLED display', 34990000, 6, NOW(), NOW(), 18),
('195697627958', 2, 'Samsung Galaxy Book4 Ultra', 'High-end laptop with Intel Core Ultra processor', 49990000, 6, NOW(), NOW(), 12);

-- Audio Devices (Category ID: 7, Parent: 1 - Đồ điện tử)
INSERT INTO products (barcode, brand_id, product_name, description, price, category_id, created_at, updated_at, quantity)
VALUES
('1902532187016', 1, 'AirPods Pro 2', 'Wireless earbuds with active noise cancellation', 5990000, 7, NOW(), NOW(), 50),
('1902532187023', 1, 'AirPods Max', 'Over-ear headphones with spatial audio', 12990000, 7, NOW(), NOW(), 20),
('4905524963052', 3, 'Sony WH-1000XM5', 'Premium noise-cancelling headphones', 8990000, 7, NOW(), NOW(), 30),
('4905524963069', 3, 'Sony WF-1000XM5', 'Wireless earbuds with industry-leading noise cancellation', 6490000, 7, NOW(), NOW(), 35),
('6925281967047', 9, 'JBL Quantum 910', 'Wireless gaming headset with head-tracking', 5490000, 7, NOW(), NOW(), 25),
('6925281967054', 9, 'JBL Flip 6', 'Portable waterproof Bluetooth speaker', 2490000, 7, NOW(), NOW(), 40);

-- TVs & Entertainment (Category ID: 8, Parent: 1 - Đồ điện tử)
INSERT INTO products (barcode, brand_id, product_name, description, price, category_id, created_at, updated_at, quantity)
VALUES
('8806092992016', 2, 'Samsung Neo QLED 8K TV', '75" premium 8K smart TV with Mini LED technology', 89990000, 8, NOW(), NOW(), 10),
('8806092992023', 2, 'Samsung The Frame TV', '65" 4K QLED TV that doubles as an art display', 32990000, 8, NOW(), NOW(), 15),
('4905524964011', 3, 'Sony Bravia XR A95L', '65" 4K OLED TV with cognitive processor XR', 79990000, 8, NOW(), NOW(), 12),
('4905524964028', 3, 'Sony HT-A7000', '7.1.2ch Dolby Atmos soundbar', 24990000, 8, NOW(), NOW(), 18),
('8806091992033', 4, 'LG C3 OLED TV', '65" 4K OLED evo TV with AI processor', 45990000, 8, NOW(), NOW(), 14),
('8806091992040', 4, 'LG OLED Flex', '42" bendable OLED display for gaming and entertainment', 39990000, 8, NOW(), NOW(), 8);

-- Smart Devices (Category ID: 10, Parent: 1 - Đồ điện tử)
INSERT INTO products (barcode, brand_id, product_name, description, price, category_id, created_at, updated_at, quantity)
VALUES
('1902532189014', 1, 'Apple Watch Series 9', 'Smartwatch with health monitoring features', 10990000, 10, NOW(), NOW(), 30),
('1902532189021', 1, 'Apple HomePod mini', 'Compact smart speaker with Siri', 2490000, 10, NOW(), NOW(), 25),
('8806092994010', 2, 'Samsung Galaxy Watch6 Classic', 'Premium smartwatch with rotating bezel', 8990000, 10, NOW(), NOW(), 22),
('8806092994027', 2, 'Samsung SmartThings Hub', 'Central control for smart home devices', 1990000, 10, NOW(), NOW(), 15);

-- HOUSEHOLD ITEMS (30 products)

-- Kitchen Appliances (Category ID: 11, Parent: 2 - Đồ gia dụng)
INSERT INTO products (barcode, brand_id, product_name, description, price, category_id, created_at, updated_at, quantity)
VALUES
('7332543731763', 6, 'Electrolux UltimateTaste 900', 'Induction cooker with SenseFry technology', 15990000, 11, NOW(), NOW(), 20),
('7332543731770', 6, 'Electrolux MaxiMix Blender', 'High-performance blender with multiple settings', 2990000, 11, NOW(), NOW(), 30),
('8851965230019', 10, 'Lock&Lock Air Fryer', 'Digital air fryer with 8 preset cooking functions', 2490000, 11, NOW(), NOW(), 35),
('8851965230026', 10, 'Lock&Lock Food Container Set', '10-piece airtight food storage container set', 590000, 11, NOW(), NOW(), 50),
('5025232956012', 8, 'Philips 3200 Series', 'Fully automatic espresso machine', 12990000, 11, NOW(), NOW(), 15),
('5025232956029', 8, 'Philips Airfryer XXL', 'Large capacity air fryer with fat removal technology', 4990000, 11, NOW(), NOW(), 25),
('5025232956036', 8, 'Philips Hand Blender', '800W hand blender with multiple attachments', 1490000, 11, NOW(), NOW(), 30);

-- Home Appliances (Category ID: 12, Parent: 2 - Đồ gia dụng)
INSERT INTO products (barcode, brand_id, product_name, description, price, category_id, created_at, updated_at, quantity)
VALUES
('7332543732012', 6, 'Electrolux UltimateCare 900', 'Front load washing machine with SteamCare', 18990000, 12, NOW(), NOW(), 15),
('7332543732029', 6, 'Electrolux PerfectCare 800', 'Heat pump dryer with GentleCare system', 22990000, 12, NOW(), NOW(), 12),
('8806091993016', 4, 'LG InstaView Door-in-Door', 'Smart refrigerator with knock-twice to see inside', 32990000, 12, NOW(), NOW(), 10),
('8806091993023', 4, 'LG DUAL Inverter AC', 'Energy-efficient air conditioner with air purification', 12990000, 12, NOW(), NOW(), 18),
('8806091993030', 4, 'LG CordZero A9', 'Cordless stick vacuum with dual power pack', 14990000, 12, NOW(), NOW(), 20),
('5025232957019', 8, 'Philips Air Purifier 3000i', 'Smart air purifier with HEPA filter', 8990000, 12, NOW(), NOW(), 22),
('5025232957026', 8, 'Philips Steam Iron', 'Azur steam iron with SteamGlide soleplate', 1990000, 12, NOW(), NOW(), 35);

-- Furniture (Category ID: 13, Parent: 2 - Đồ gia dụng)
INSERT INTO products (barcode, brand_id, product_name, description, price, category_id, created_at, updated_at, quantity)
VALUES
('70234198', 9, 'IKEA BILLY', 'Versatile bookcase with adjustable shelves', 1990000, 13, NOW(), NOW(), 30),
('70234204', 9, 'IKEA MALM', 'Bed frame with storage boxes', 5990000, 13, NOW(), NOW(), 15),
('70234211', 9, 'IKEA POÄNG', 'Armchair with bentwood frame', 2490000, 13, NOW(), NOW(), 25),
('70234228', 9, 'IKEA KALLAX', 'Shelving unit with versatile storage options', 2990000, 13, NOW(), NOW(), 20),
('70234235', 9, 'IKEA HEMNES', 'Dresser with 8 drawers', 6990000, 13, NOW(), NOW(), 12);

-- Bathroom Items (Category ID: 15, Parent: 2 - Đồ gia dụng)
INSERT INTO products (barcode, brand_id, product_name, description, price, category_id, created_at, updated_at, quantity)
VALUES
('5025232958016', 8, 'Philips Sonicare DiamondClean', 'Smart electric toothbrush with app connectivity', 3990000, 15, NOW(), NOW(), 25),
('7332543733019', 6, 'Electrolux Water Heater', 'Instant water heater with temperature control', 2490000, 15, NOW(), NOW(), 20),
('70234242', 9, 'IKEA GODMORGON', 'Bathroom vanity with drawers', 4990000, 15, NOW(), NOW(), 15),
('70234259', 9, 'IKEA BROGRUND', 'Bathroom accessories set', 790000, 15, NOW(), NOW(), 30);

-- Home Decor (Category ID: 16, Parent: 2 - Đồ gia dụng)
INSERT INTO products (barcode, brand_id, product_name, description, price, category_id, created_at, updated_at, quantity)
VALUES
('70234266', 9, 'IKEA STOCKHOLM', 'Handwoven rug with wool blend', 3990000, 16, NOW(), NOW(), 18),
('70234273', 9, 'IKEA RIBBA', 'Picture frame set in various sizes', 590000, 16, NOW(), NOW(), 40),
('70234280', 9, 'IKEA FEJKA', 'Artificial potted plant', 290000, 16, NOW(), NOW(), 50),
('70234297', 9, 'IKEA SYMFONISK', 'Table lamp with WiFi speaker', 2990000, 16, NOW(), NOW(), 22);

-- FASHION (30 products)

-- Men's Fashion (Category ID: 17, Parent: 3 - Thời trang)
INSERT INTO products (barcode, brand_id, product_name, description, price, category_id, created_at, updated_at, quantity)
VALUES
('4060509674016', 14, 'Adidas Ultraboost 23', 'Men''s premium running shoes', 4990000, 17, NOW(), NOW(), 30),
('4060509674023', 14, 'Adidas Tiro Track Jacket', 'Men''s athletic jacket with zip pockets', 1490000, 17, NOW(), NOW(), 35),
('194493246018', 15, 'Nike Air Force 1', 'Men''s classic sneakers', 2790000, 17, NOW(), NOW(), 40),
('194493246025', 15, 'Nike Dri-FIT T-Shirt', 'Men''s moisture-wicking training shirt', 790000, 17, NOW(), NOW(), 50),
('8718108562019', 11, 'Zara Slim Fit Blazer', 'Men''s tailored blazer', 2290000, 17, NOW(), NOW(), 25),
('8718108562026', 11, 'Zara Chino Trousers', 'Men''s casual pants', 1190000, 17, NOW(), NOW(), 30),
('8718108562033', 11, 'Zara Oxford Shirt', 'Men''s button-up cotton shirt', 890000, 17, NOW(), NOW(), 35);

-- Women's Fashion (Category ID: 18, Parent: 3 - Thời trang)
INSERT INTO products (barcode, brand_id, product_name, description, price, category_id, created_at, updated_at, quantity)
VALUES
('4060509675013', 14, 'Adidas Cloudfoam Pure', 'Women''s running shoes', 2490000, 18, NOW(), NOW(), 35),
('4060509675020', 14, 'Adidas Essentials Hoodie', 'Women''s cotton blend hoodie', 1290000, 18, NOW(), NOW(), 40),
('194493247015', 15, 'Nike Air Max 270', 'Women''s lifestyle shoes', 3790000, 18, NOW(), NOW(), 30),
('194493247022', 15, 'Nike Sportswear Leggings', 'Women''s high-waisted leggings', 1190000, 18, NOW(), NOW(), 45),
('8718108563016', 11, 'Zara Pleated Midi Skirt', 'Women''s elegant pleated skirt', 1490000, 18, NOW(), NOW(), 25),
('8718108563023', 11, 'Zara Oversized Blazer', 'Women''s stylish oversized blazer', 2490000, 18, NOW(), NOW(), 20),
('8718108563030', 11, 'Zara High Waist Jeans', 'Women''s skinny jeans', 1290000, 18, NOW(), NOW(), 30);

-- Kids' Fashion (Category ID: 19, Parent: 3 - Thời trang)
INSERT INTO products (barcode, brand_id, product_name, description, price, category_id, created_at, updated_at, quantity)
VALUES
('4060509676010', 14, 'Adidas Kids Superstar', 'Children''s classic sneakers', 1790000, 19, NOW(), NOW(), 25),
('4060509676027', 14, 'Adidas Kids Tracksuit', 'Children''s two-piece sports outfit', 1490000, 19, NOW(), NOW(), 20),
('194493248012', 15, 'Nike Kids Air Max', 'Children''s cushioned shoes', 1990000, 19, NOW(), NOW(), 22),
('194493248029', 15, 'Nike Kids Dri-FIT Set', 'Children''s sports t-shirt and shorts set', 990000, 19, NOW(), NOW(), 30);

-- Watches (Category ID: 20, Parent: 3 - Thời trang)
INSERT INTO products (barcode, brand_id, product_name, description, price, category_id, created_at, updated_at, quantity)
VALUES
('1902532190010', 1, 'Apple Watch Ultra 2', 'Rugged smartwatch for outdoor adventures', 19990000, 20, NOW(), NOW(), 15),
('8806092995017', 2, 'Samsung Galaxy Watch6', 'Advanced health monitoring smartwatch', 7990000, 20, NOW(), NOW(), 20),
('4905524965018', 3, 'Sony Wena 3', 'Hybrid smartwatch with traditional design', 6990000, 20, NOW(), NOW(), 12);

-- Bags & Backpacks (Category ID: 22, Parent: 3 - Thời trang)
INSERT INTO products (barcode, brand_id, product_name, description, price, category_id, created_at, updated_at, quantity)
VALUES
('4060509677017', 14, 'Adidas Linear Backpack', 'Spacious backpack for everyday use', 890000, 22, NOW(), NOW(), 35),
('4060509677024', 14, 'Adidas Duffel Bag', 'Sports bag with shoe compartment', 1290000, 22, NOW(), NOW(), 25),
('194493249019', 15, 'Nike Brasilia Backpack', 'Durable backpack with laptop sleeve', 990000, 22, NOW(), NOW(), 30),
('194493249026', 15, 'Nike Heritage Tote', 'Stylish tote bag for daily use', 790000, 22, NOW(), NOW(), 40),
('8718108564013', 11, 'Zara Leather Crossbody', 'Women''s small leather crossbody bag', 1490000, 22, NOW(), NOW(), 20);

-- HEALTH & BEAUTY (10 products)

-- Cosmetics (Category ID: 23, Parent: 4 - Sức khỏe & Làm đẹp)
INSERT INTO products (barcode, brand_id, product_name, description, price, category_id, created_at, updated_at, quantity)
VALUES
('3600522086840', 16, 'L''Oréal Paris True Match', 'Liquid foundation with hyaluronic acid', 290000, 23, NOW(), NOW(), 40),
('3600522086857', 16, 'L''Oréal Paris Voluminous Mascara', 'Volume-building mascara', 220000, 23, NOW(), NOW(), 45),
('3600531591816', 18, 'Maybelline Fit Me Matte', 'Poreless foundation for oily skin', 190000, 23, NOW(), NOW(), 50);

-- Skincare (Category ID: 24, Parent: 4 - Sức khỏe & Làm đẹp)
INSERT INTO products (barcode, brand_id, product_name, description, price, category_id, created_at, updated_at, quantity)
VALUES
('4005808178889', 17, 'Nivea Creme', 'All-purpose moisturizing cream', 120000, 24, NOW(), NOW(), 60),
('4005808178896', 17, 'Nivea Sun Protect & Moisture', 'Sunscreen lotion SPF 50+', 220000, 24, NOW(), NOW(), 40),
('8809516839841', 19, 'Innisfree Green Tea Seed Serum', 'Hydrating facial serum with green tea extract', 490000, 24, NOW(), NOW(), 35);

-- Beauty Devices (Category ID: 27, Parent: 4 - Sức khỏe & Làm đẹp)
INSERT INTO products (barcode, brand_id, product_name, description, price, category_id, created_at, updated_at, quantity)
VALUES
('5025232959013', 8, 'Philips Lumea IPL', 'Hair removal device with SenseIQ technology', 7990000, 27, NOW(), NOW(), 15),
('5025232959020', 8, 'Philips VisaPure', 'Facial cleansing brush with multiple settings', 2490000, 27, NOW(), NOW(), 20);

-- Supplements (Category ID: 28, Parent: 4 - Sức khỏe & Làm đẹp)
INSERT INTO products (barcode, brand_id, product_name, description, price, category_id, created_at, updated_at, quantity)
VALUES
('8809516839858', 19, 'Innisfree Vitamin C Powder', 'Pure vitamin C powder for skincare', 390000, 28, NOW(), NOW(), 30),
('8809516839865', 20, 'The Face Shop Collagen Supplement', '30-day collagen drink for skin elasticity', 790000, 28, NOW(), NOW(), 25);

-- Now add product images for some products
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES
-- Samsung Galaxy S23 Ultra images
(1, 'https://example.com/images/products/samsung_s23_ultra_1.jpg', TRUE, NOW()),
(1, 'https://example.com/images/products/samsung_s23_ultra_2.jpg', FALSE, NOW()),
(1, 'https://example.com/images/products/samsung_s23_ultra_3.jpg', FALSE, NOW()),

-- iPhone 15 Pro Max images
(2, 'https://example.com/images/products/iphone_15_pro_max_1.jpg', TRUE, NOW()),
(2, 'https://example.com/images/products/iphone_15_pro_max_2.jpg', FALSE, NOW()),
(2, 'https://example.com/images/products/iphone_15_pro_max_3.jpg', FALSE, NOW()),

-- MacBook Pro images
(9, 'https://example.com/images/products/macbook_pro_m3_max_1.jpg', TRUE, NOW()),
(9, 'https://example.com/images/products/macbook_pro_m3_max_2.jpg', FALSE, NOW()),

-- AirPods Pro 2 images
(17, 'https://example.com/images/products/airpods_pro_2_1.jpg', TRUE, NOW()),
(17, 'https://example.com/images/products/airpods_pro_2_2.jpg', FALSE, NOW()),

-- Samsung Neo QLED TV images
(23, 'https://example.com/images/products/samsung_neo_qled_1.jpg', TRUE, NOW()),
(23, 'https://example.com/images/products/samsung_neo_qled_2.jpg', FALSE, NOW()),

-- Electrolux washing machine images
(38, 'https://example.com/images/products/electrolux_washing_machine_1.jpg', TRUE, NOW()),
(38, 'https://example.com/images/products/electrolux_washing_machine_2.jpg', FALSE, NOW()),

-- IKEA BILLY bookcase images
(45, 'https://example.com/images/products/ikea_billy_1.jpg', TRUE, NOW()),
(45, 'https://example.com/images/products/ikea_billy_2.jpg', FALSE, NOW()),

-- Adidas Ultraboost images
(53, 'https://example.com/images/products/adidas_ultraboost_1.jpg', TRUE, NOW()),
(53, 'https://example.com/images/products/adidas_ultraboost_2.jpg', FALSE, NOW()),
(53, 'https://example.com/images/products/adidas_ultraboost_3.jpg', FALSE, NOW()),

-- Nike Air Force 1 images
(55, 'https://example.com/images/products/nike_air_force_1_1.jpg', TRUE, NOW()),
(55, 'https://example.com/images/products/nike_air_force_1_2.jpg', FALSE, NOW()),
(55, 'https://example.com/images/products/nike_air_force_1_3.jpg', FALSE, NOW()),

-- L'Oréal Paris True Match images
(83, 'https://example.com/images/products/loreal_true_match_1.jpg', TRUE, NOW()),
(83, 'https://example.com/images/products/loreal_true_match_2.jpg', FALSE, NOW());

-- Add product variants for clothing and shoes
INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES
-- Adidas Ultraboost 23 variants
(53, 'US 7', 5, NOW(), NOW()),
(53, 'US 8', 8, NOW(), NOW()),
(53, 'US 9', 10, NOW(), NOW()),
(53, 'US 10', 7, NOW(), NOW()),
(53, 'US 11', 5, NOW(), NOW()),

-- Nike Air Force 1 variants
(55, 'US 7', 6, NOW(), NOW()),
(55, 'US 8', 9, NOW(), NOW()),
(55, 'US 9', 12, NOW(), NOW()),
(55, 'US 10', 8, NOW(), NOW()),
(55, 'US 11', 5, NOW(), NOW()),

-- Adidas Tiro Track Jacket variants
(54, 'S', 7, NOW(), NOW()),
(54, 'M', 10, NOW(), NOW()),
(54, 'L', 12, NOW(), NOW()),
(54, 'XL', 6, NOW(), NOW()),

-- Nike Dri-FIT T-Shirt variants
(56, 'S', 10, NOW(), NOW()),
(56, 'M', 15, NOW(), NOW()),
(56, 'L', 15, NOW(), NOW()),
(56, 'XL', 10, NOW(), NOW()),

-- Zara Slim Fit Blazer variants
(57, '48', 5, NOW(), NOW()),
(57, '50', 7, NOW(), NOW()),
(57, '52', 8, NOW(), NOW()),
(57, '54', 5, NOW(), NOW()),

-- Zara Chino Trousers variants
(58, '30', 6, NOW(), NOW()),
(58, '32', 8, NOW(), NOW()),
(58, '34', 10, NOW(), NOW()),
(58, '36', 6, NOW(), NOW()),

-- Adidas Cloudfoam Pure variants
(60, 'US 5', 7, NOW(), NOW()),
(60, 'US 6', 9, NOW(), NOW()),
(60, 'US 7', 10, NOW(), NOW()),
(60, 'US 8', 9, NOW(), NOW()),

-- Nike Air Max 270 variants
(62, 'US 5', 6, NOW(), NOW()),
(62, 'US 6', 8, NOW(), NOW()),
(62, 'US 7', 10, NOW(), NOW()),
(62, 'US 8', 6, NOW(), NOW()),

-- Zara Pleated Midi Skirt variants
(64, 'XS', 5, NOW(), NOW()),
(64, 'S', 7, NOW(), NOW()),
(64, 'M', 8, NOW(), NOW()),
(64, 'L', 5, NOW(), NOW()),

-- Adidas Kids Superstar variants
(67, 'US 1', 5, NOW(), NOW()),
(67, 'US 2', 6, NOW(), NOW()),
(67, 'US 3', 7, NOW(), NOW()),
(67, 'US 4', 5, NOW(), NOW()),
(67, 'US 5', 2, NOW(), NOW());
