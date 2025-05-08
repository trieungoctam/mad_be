-- Mock data for 100 products across different categories and brands

DELETE FROM products;

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

-- Smartphones & Tablets (Category ID: 5)
UPDATE products
SET description = 'The Samsung Galaxy S23 Ultra is a flagship smartphone featuring a revolutionary 200MP camera system with advanced nightography capabilities. Equipped with the powerful Snapdragon 8 Gen 2 processor and S Pen functionality built directly into the device. The stunning 6.8-inch Dynamic AMOLED 2X display offers vibrant colors and adaptive 120Hz refresh rate for smooth scrolling. With up to 12GB RAM and 1TB storage options, this premium device delivers exceptional performance for both productivity and entertainment.'
WHERE product_name = 'Samsung Galaxy S23 Ultra';

UPDATE products
SET description = 'Apple''s most advanced iPhone featuring the A17 Pro chip built on 3nm technology for unprecedented performance and efficiency. The premium 6.7-inch Super Retina XDR display with ProMotion technology delivers stunning visuals with 120Hz adaptive refresh rate. The revolutionary camera system includes a 48MP main camera with advanced computational photography capabilities, a 12MP ultrawide lens, and a 12MP telephoto with 5x optical zoom. Crafted from aerospace-grade titanium, the iPhone 15 Pro Max offers exceptional durability while maintaining a refined, lightweight design.'
WHERE product_name = 'iPhone 15 Pro Max';

UPDATE products
SET description = 'The Xiaomi 14 Pro pushes mobile photography to new heights with its advanced Leica optical system and custom-tuned imaging algorithms. Powered by the Snapdragon 8 Gen 3 processor, this flagship device delivers exceptional performance for gaming and multitasking. The curved 6.73-inch LTPO AMOLED display features 2K resolution, 120Hz refresh rate, and 3000 nits peak brightness for stunning visuals in any lighting condition. The device includes a robust 4880mAh battery with 120W wired charging, 50W wireless charging, and 10W reverse wireless charging capabilities.'
WHERE product_name = 'Xiaomi 14 Pro';

UPDATE products
SET description = 'The Xiaomi Redmi Note 13 Pro redefines mid-range smartphone photography with its exceptional 108MP primary camera, featuring 3x in-sensor zoom and advanced night mode capabilities. The device boasts a stunning 6.67-inch AMOLED display with 120Hz refresh rate and 1080x2400 resolution for smooth, vibrant visuals. Powered by the Snapdragon 7s Gen 2 processor and up to 12GB of RAM, it delivers reliable performance for everyday tasks and moderate gaming. The large 5000mAh battery supports 67W turbo charging, providing all-day usage with minimal charging time. With MIUI 14 based on Android 13, the device offers numerous customization options and productivity features.'
WHERE product_name = 'Xiaomi Redmi Note 13 Pro';

UPDATE products
SET description = 'The LG Velvet represents a design-focused approach to smartphones with its distinctive "Raindrop" camera arrangement and symmetrical curves. The device features a 6.8-inch P-OLED FullVision display with a cinematic 20.5:9 aspect ratio, perfect for media consumption. Powered by the Snapdragon 765G processor with integrated 5G capabilities, it delivers reliable performance while maintaining excellent battery efficiency. The triple camera system includes a 48MP main sensor, 8MP ultra-wide lens, and 5MP depth sensor for versatile photography options. Compatible with the optional Dual Screen accessory and LG Stylus Pen, the Velvet offers expanded functionality for multitasking and creative work.'
WHERE product_name = 'LG Velvet';

UPDATE products
SET description = 'The iPad Pro 12.9 (2023) represents Apple''s most powerful tablet experience, featuring the blazing-fast M2 chip with 8-core CPU and 10-core GPU for desktop-class performance. The stunning 12.9-inch Liquid Retina XDR display utilizes mini-LED technology to deliver extreme dynamic range with 1000 nits of full-screen brightness and 1600 nits peak brightness for HDR content. ProMotion technology provides adaptive refresh rates up to 120Hz for ultra-smooth scrolling and responsiveness. Advanced camera system includes a 12MP wide camera, 10MP ultra-wide camera, and LiDAR Scanner for immersive AR experiences. Compatible with Apple Pencil (2nd generation) and Magic Keyboard, this premium tablet easily transforms into a versatile workstation for creative professionals.'
WHERE product_name = 'iPad Pro 12.9 (2023)';

UPDATE products
SET description = 'The Samsung Galaxy Tab S9 Ultra is a premium Android tablet designed for professional creativity and productivity with its massive 14.6-inch Dynamic AMOLED 2X display featuring 120Hz refresh rate and 2960x1848 resolution. Powered by the Snapdragon 8 Gen 2 processor and up to 16GB RAM, it delivers exceptional performance for multitasking and demanding applications. The refined S Pen is included, providing a natural writing experience with virtually no latency. The quad speaker system tuned by AKG delivers immersive sound with Dolby Atmos support. The dual front camera system includes a 12MP wide and 12MP ultra-wide lens, perfect for video conferencing. With its slim 5.5mm profile and armor aluminum construction, this flagship tablet combines premium design with durability.'
WHERE product_name = 'Samsung Galaxy Tab S9 Ultra';

UPDATE products
SET description = 'The Xiaomi Pad 6 delivers exceptional value with its 11-inch 2.8K LCD display featuring 144Hz refresh rate and Dolby Vision support for immersive entertainment. Powered by the Snapdragon 870 processor and up to 8GB LPDDR5 RAM, it provides smooth performance for productivity and gaming. The quad-speaker system with Dolby Atmos creates an impressive audio experience, complementing the visual quality for multimedia consumption. The generous 8840mAh battery supports up to 16 hours of video playback, while 33W fast charging quickly replenishes power when needed. With support for Xiaomi Smart Pen and the dedicated keyboard case, this versatile tablet easily transforms into a productive workstation for students and professionals.'
WHERE product_name = 'Xiaomi Pad 6';

-- Laptops & Computers (Category ID: 6)
UPDATE products
SET description = 'The MacBook Pro 16" with M3 Max represents Apple''s most powerful laptop, designed for professionals with demanding workflows. The M3 Max chip features up to 16-core CPU, 40-core GPU, and 16-core Neural Engine, delivering unprecedented performance for complex tasks like 3D rendering, machine learning, and video editing. The stunning 16.2-inch Liquid Retina XDR display offers extreme dynamic range with 1000 nits sustained brightness (1600 nits peak for HDR) and ProMotion technology with adaptive refresh rates up to 120Hz. The advanced thermal system enables sustained performance during intensive workloads. Connectivity includes three Thunderbolt 4 ports, HDMI, SDXC card slot, and MagSafe 3 charging. With up to 32GB unified memory and 8TB SSD storage options, this premium laptop offers exceptional speed and capacity for professional workflows.'
WHERE product_name = 'MacBook Pro 16" M3 Max';

UPDATE products
SET description = 'The MacBook Air 13" with M3 chip combines exceptional performance with Apple''s thinnest laptop design. The M3 chip features an 8-core CPU, up to 10-core GPU, and 16-core Neural Engine, delivering remarkable speed and efficiency for everyday tasks and creative work. The beautiful 13.6-inch Liquid Retina display offers 500 nits of brightness and P3 wide color gamut for vibrant, accurate visuals. The fanless design ensures completely silent operation, while the efficient architecture provides up to 18 hours of battery life. Features include a 1080p FaceTime HD camera, immersive six-speaker sound system with spatial audio support, and a comfortable Magic Keyboard with Touch ID. Weighing just 2.7 pounds with an ultra-thin 11.3mm profile, this versatile laptop offers the perfect balance of portability and performance.'
WHERE product_name = 'MacBook Air 13" M3';

UPDATE products
SET description = 'The LG Gram 17 redefines ultra-lightweight laptops with its remarkable 17-inch display in a package weighing just 1.35kg (2.98lbs). The expansive WQXGA (2560x1600) IPS display offers 99% DCI-P3 color gamut coverage, making it ideal for creative professionals. Powered by 13th Gen Intel Core processors and up to 32GB LPDDR5 RAM, it delivers excellent performance for productivity and light content creation. The impressive 80Wh battery provides up to 20 hours of usage on a single charge. The durable magnesium alloy chassis meets MIL-STD-810H military durability standards while maintaining an ultra-thin profile. Comprehensive connectivity includes Thunderbolt 4, USB-A, HDMI, microSD card reader, and a 3.5mm audio jack. With its large screen, exceptional battery life, and ultra-portable design, the LG Gram 17 is perfect for professionals who need a large display without sacrificing mobility.'
WHERE product_name = 'LG Gram 17';

UPDATE products
SET description = 'The LG UltraGear Gaming Laptop delivers high-performance gaming in a sleek, portable package. Equipped with an NVIDIA GeForce RTX 4070 GPU with advanced ray tracing capabilities and DLSS 3.0 technology, it offers immersive gaming visuals with high frame rates. The powerful 13th Gen Intel Core i9 processor with 14 cores and 20 threads provides exceptional processing power for demanding games and creative applications. The 17-inch WQXGA (2560x1600) IPS display features a 165Hz refresh rate, 3ms response time, and NVIDIA G-SYNC support for smooth, tear-free gaming. The advanced cooling system with vapor chamber technology efficiently dissipates heat during intensive gaming sessions. A customizable per-key RGB keyboard enhances the gaming experience with personalized lighting effects. With its premium audio system featuring DTS:X Ultra, this gaming laptop delivers immersive sound to complement its outstanding visual performance.'
WHERE product_name = 'LG UltraGear Gaming Laptop';

UPDATE products
SET description = 'The Samsung Galaxy Book4 Pro combines premium design with versatile 2-in-1 functionality. The stunning 16-inch Dynamic AMOLED 2X touchscreen display offers 3K (2880x1800) resolution with 120Hz refresh rate and VESA DisplayHDR 500 certification for vibrant, accurate colors. Powered by Intel Core Ultra 7 processors with Intel Xe graphics, it delivers excellent performance for productivity and content creation. The 360-degree hinge enables versatile usage modes, from laptop to tablet, while S Pen support provides natural writing and drawing capabilities. The premium aluminum chassis measures just 11.9mm thin and weighs 1.56kg, offering exceptional portability for its screen size. The quad speaker system tuned by AKG with Dolby Atmos support delivers immersive audio. With up to 14 hours of battery life and fast charging support, this premium convertible laptop provides all-day productivity with minimal downtime.'
WHERE product_name = 'Samsung Galaxy Book4 Pro';

UPDATE products
SET description = 'The Samsung Galaxy Book4 Ultra represents the pinnacle of Samsung''s laptop lineup, designed for professionals with demanding workflows. Powered by Intel Core Ultra 9 processors with advanced performance and efficiency cores, it delivers exceptional processing power while maintaining excellent battery efficiency. The NVIDIA GeForce RTX 4070 GPU with 8GB GDDR6 memory provides outstanding graphics performance for creative applications and gaming. The stunning 16-inch Dynamic AMOLED 2X display offers 3K (2880x1800) resolution, 120Hz refresh rate, and VESA DisplayHDR 500 certification for breathtaking visuals with precise color accuracy. The advanced cooling system with dual fans and vapor chamber technology ensures sustained performance during intensive tasks. With up to 32GB LPDDR5X RAM and 2TB NVMe SSD, this premium laptop offers ample memory and storage for professional workloads. The comprehensive connectivity includes Thunderbolt 4, USB-A, HDMI, microSD card reader, and a secure fingerprint reader integrated into the power button.'
WHERE product_name = 'Samsung Galaxy Book4 Ultra';

-- Audio Devices (Category ID: 7)
UPDATE products
SET description = 'The AirPods Pro 2 represent Apple''s most advanced wireless earbuds, featuring next-generation Active Noise Cancellation that reduces twice as much noise compared to the original AirPods Pro. The new Adaptive Transparency mode allows environmental sounds while reducing harsh environmental noise. Powered by the H2 chip, these premium earbuds deliver exceptional audio quality with Personalized Spatial Audio that creates an immersive, theater-like experience tailored to your ears. The redesigned Touch Control allows easy volume adjustments directly from the stem. Battery life has been improved to 6 hours of listening time per charge (30 hours total with charging case). The charging case now includes a built-in speaker for Find My alerts, precision finding with U1 chip, and supports charging via Apple Watch charger. With four pairs of silicone ear tips (XS, S, M, L) included, these earbuds offer a secure, comfortable fit for extended listening sessions.'
WHERE product_name = 'AirPods Pro 2';

UPDATE products
SET description = 'AirPods Max deliver an unparalleled listening experience with computational audio that combines custom acoustic design, H1 chips, and advanced software. The breathable knit mesh canopy distributes weight to reduce on-head pressure, while the stainless steel frame provides strength, flexibility, and comfort. Each ear cushion uses acoustically engineered memory foam to create an effective seal for immersive sound. Equipped with 40mm Apple-designed dynamic drivers, they produce rich, deep bass, accurate mid-ranges, and crisp high-frequency extension. Industry-leading Active Noise Cancellation technology blocks outside noise, while Transparency mode allows you to stay aware of your surroundings. Spatial Audio with dynamic head tracking provides a theater-like sound experience. The Digital Crown offers precise volume control and the ability to play or pause audio, skip tracks, answer phone calls, and activate Siri. With 20 hours of listening time with Active Noise Cancellation and Spatial Audio enabled, AirPods Max provide all-day audio enjoyment.'
WHERE product_name = 'AirPods Max';

UPDATE products
SET description = 'The Sony WH-1000XM5 headphones set a new standard for noise-cancelling performance with eight microphones and two processors controlling eight speakers for unprecedented noise reduction, especially in mid-high frequency ranges. The newly developed 30mm driver unit with a soft edge enhances noise cancellation performance while maintaining a natural sound with clear mid-range and crisp high-frequency response. Precise Voice Pickup Technology uses four beamforming microphones and AI-based noise reduction algorithms for exceptional call quality. The lightweight design (250g) with synthetic soft-fit leather creates a snug, pressure-free fit for extended listening comfort. Adaptive Sound Control automatically adjusts ambient sound settings based on your location and activities. With 30 hours of battery life and quick charging (3 hours of playback from 3 minutes of charging), these premium headphones provide all-day listening with minimal downtime. Additional features include multipoint connection for simultaneous pairing with two Bluetooth devices, Speak-to-Chat functionality that automatically pauses music when you speak, and DSEE Extreme upscaling for compressed digital music files.'
WHERE product_name = 'Sony WH-1000XM5';

UPDATE products
SET description = 'The Sony WF-1000XM5 wireless earbuds feature industry-leading noise cancellation with the Integrated Processor V1, HD Noise Cancelling Processor QN2e, and three microphones per earbud. The newly developed 8.4mm Dynamic Driver X delivers rich, clear sound with deep bass and minimal distortion. Precise Voice Pickup Technology with AI-based noise reduction algorithms ensures exceptional call quality even in noisy environments. The earbuds are 25% smaller and 20% lighter than the previous generation, providing a comfortable, secure fit for extended listening. Adaptive Sound Control automatically adjusts ambient sound settings based on your location and activities. With 8 hours of battery life with noise cancellation active (24 hours total with charging case) and quick charging (60 minutes of playback from 5 minutes of charging), these premium earbuds provide all-day listening with minimal downtime. Additional features include multipoint connection for simultaneous pairing with two Bluetooth devices, Speak-to-Chat functionality that automatically pauses music when you speak, and DSEE Extreme upscaling for compressed digital music files.'
WHERE product_name = 'Sony WF-1000XM5';

-- TVs & Entertainment (Category ID: 8)
UPDATE products
SET description = 'The Samsung Neo QLED 8K TV represents the pinnacle of television technology, featuring Quantum Matrix Technology Pro with Mini LEDs that are 40 times smaller than conventional LEDs, providing precise backlight control for exceptional contrast. The Neural Quantum Processor 8K with 20 neural networks analyzes content and optimizes it to 8K resolution regardless of the input source. The stunning 75-inch Infinity Screen design offers an immersive viewing experience with virtually no borders. Object Tracking Sound+ with up to 12 speakers built into the TV creates three-dimensional audio that follows the action on screen. The Anti-Reflection layer minimizes glare for optimal viewing in any lighting condition. Gaming features include Motion Xcelerator Turbo Pro for 4K gameplay at 144Hz, Super Ultrawide GameView for aspect ratios up to 32:9, and Game Bar for quick access to gaming settings. The integrated IoT hub with SmartThings compatibility allows control of compatible smart home devices directly from the TV. With the SolarCell Remote that charges via indoor lighting, this premium TV combines cutting-edge technology with eco-friendly design.'
WHERE product_name = 'Samsung Neo QLED 8K TV';

UPDATE products
SET description = 'The Samsung The Frame TV revolutionizes the concept of television by doubling as a stunning art display when not in use. The 65-inch QLED 4K display features Quantum Dot technology for 100% color volume with over a billion colors. The innovative Matte Display film provides a museum-like viewing experience by reducing reflections and fingerprints. Art Mode displays your choice of artwork from the Art Store subscription service featuring over 2,400 pieces from world-renowned museums and galleries. The customizable magnetic bezels allow you to change the frame color to match your decor. The Slim-Fit Wall Mount allows the TV to hang flush against the wall like a picture frame, while the One Connect Box keeps cables hidden for a clean installation. The Motion Sensor automatically turns the screen on when you enter the room and off when you leave to conserve energy. With 4K AI Upscaling, this versatile TV delivers exceptional picture quality for both entertainment and art display.'
WHERE product_name = 'Samsung The Frame TV';

UPDATE products
SET description = 'The Sony Bravia XR A95L is a premium 65-inch 4K OLED TV powered by the revolutionary Cognitive Processor XR, which analyzes content the way humans see and hear for a more immersive experience. The self-illuminating OLED XR Triluminos Max panel with new Quantum Dot technology achieves up to 200% more color brightness than conventional OLED TVs. XR OLED Contrast Pro delivers Sony''s brightest-ever OLED picture with pure blacks and peak highlights. The Acoustic Surface Audio+ technology uses the entire screen as a speaker, creating perfectly synchronized sound that follows the action. BRAVIA CORE Calibrated mode automatically adjusts the picture settings to match the filmmaker''s vision. For gaming, features include 4K/120Hz, Variable Refresh Rate (VRR), Auto HDR Tone Mapping, and Auto Genre Picture Mode when connected to PlayStation 5. The Google TV interface provides access to over 700,000 movies and TV episodes, with hands-free voice search using "Hey Google." The three-way stand offers multiple positioning options, including a narrow position for smaller spaces and a soundbar position for audio equipment.'
WHERE product_name = 'Sony Bravia XR A95L';

UPDATE products
SET description = 'The Sony HT-A7000 is a premium 7.1.2ch Dolby Atmos soundbar that creates an immersive sound field through Vertical Surround Engine and S-Force PRO Front Surround technology. The seven speakers include two up-firing speakers for height channels, two beam tweeters, three front speakers, and a built-in dual subwoofer for rich bass. Sound Field Optimization uses microphones to measure the room''s dimensions and optimize audio performance for your specific space. 360 Spatial Sound Mapping creates multiple phantom speakers for a truly multidimensional experience. The HDMI 2.1 connection supports 8K HDR, 4K/120Hz passthrough, and eARC for high-quality audio return from the TV. Compatible with optional wireless rear speakers and subwoofers for an enhanced surround experience. Voice control works with Google Assistant, Amazon Alexa, and Apple AirPlay 2 for convenient operation. The Acoustic Center Sync feature allows the TV to work as the center channel when paired with compatible Sony BRAVIA TVs, creating perfect harmony between the soundbar and TV audio.'
WHERE product_name = 'Sony HT-A7000';

UPDATE products
SET description = 'The LG C3 OLED TV features a 65-inch self-lit OLED evo panel with Brightness Booster that delivers up to 20% more brightness than conventional OLED displays. The α9 AI Processor Gen6 analyzes content and adjusts picture and sound settings for an optimized viewing experience. AI Picture Pro provides enhanced depth and more vivid images, while AI Sound Pro creates a virtual 9.1.2 surround sound experience from the TV''s built-in speakers. Dolby Vision IQ and Dolby Atmos support ensures cinema-quality picture and sound for compatible content. For gamers, the C3 offers NVIDIA G-SYNC, AMD FreeSync Premium, and Variable Refresh Rate (VRR) support, along with four HDMI 2.1 ports capable of 4K/120Hz for next-gen console gaming. Game Optimizer mode with Game Dashboard provides quick access to game-specific settings. The webOS 23 smart platform with ThinQ AI offers personalized content recommendations and hands-free voice control. The ultra-slim Gallery Design with virtually no bezels allows the TV to blend seamlessly with any décor.'
WHERE product_name = 'LG C3 OLED TV';

UPDATE products
SET description = 'The LG OLED Flex represents a revolutionary approach to display technology with its bendable 42-inch OLED screen that can transform from completely flat to a curved 900R radius at the touch of a button. The motorized display offers 20 levels of curvature, allowing users to find their optimal viewing angle for both gaming and entertainment. The self-lit OLED display with 100% color fidelity and perfect black levels is enhanced with LG''s a9 Gen5 AI Processor for exceptional picture quality. Gaming features include a 138Hz refresh rate, 0.1ms response time, NVIDIA G-SYNC, AMD FreeSync Premium, and Variable Refresh Rate (VRR) support for smooth, tear-free gaming. The Multi View feature allows users to display content from two different sources simultaneously, perfect for streaming your gameplay while watching a walkthrough video. The innovative Game Optimizer dashboard provides quick access to all game-related settings. Audio is delivered through the built-in 40W 2.2 channel speaker system with Dolby Atmos support. The height-adjustable stand with tilt function ensures comfortable viewing in any position.'
WHERE product_name = 'LG OLED Flex';

-- Smart Devices (Category ID: 10)
UPDATE products
SET description = 'The Apple Watch Series 9 introduces the innovative Double Tap gesture control, allowing you to control the watch by tapping your index finger and thumb together. Powered by the new S9 chip, it offers 30% faster performance than the previous generation and enables on-device Siri processing for quicker responses without internet connection. The stunning Always-On Retina display is 2x brighter in low light conditions (up to 2000 nits) and can dim to just 1 nit for discreet viewing. Advanced health monitoring features include ECG app, blood oxygen measurement, temperature sensing for cycle tracking, and advanced sleep stages tracking. The enhanced workout app provides custom workouts with Heart Rate Zones and new metrics for cyclists and runners. The durable design is swim-proof and crack-resistant, with recycled aluminum or stainless steel case options. With all-day 18-hour battery life and fast charging that provides 80% in about 45 minutes, the Apple Watch Series 9 combines innovative technology with health and fitness capabilities in an elegant, customizable design.'
WHERE product_name = 'Apple Watch Series 9';

UPDATE products
SET description = 'The Apple HomePod mini delivers surprisingly big sound from a compact smart speaker just 3.3 inches tall. The innovative acoustic design with a full-range driver and dual passive radiators produces deep bass and crisp high frequencies. Computational audio with advanced algorithms enables real-time tuning for optimal sound in any room. Multiple HomePod mini speakers can be paired for stereo sound or placed throughout the home for synchronized multi-room audio. With Siri intelligence, you can control smart home accessories, set timers, check calendar events, and send messages using just your voice. The Intercom feature allows you to send voice messages to other Apple devices in your home. Four microphones enable far-field Siri recognition, even when music is playing. The elegant design features a seamless mesh fabric available in five colors (white, midnight, blue, orange, and yellow), with a backlit touch surface for manual controls. Integration with Apple services allows easy access to Apple Music, Apple Podcasts, and thousands of radio stations. Enhanced privacy features ensure that all Siri requests are encrypted and not associated with your Apple ID.'
WHERE product_name = 'Apple HomePod mini';

UPDATE products
SET description = 'The Samsung Galaxy Watch6 Classic combines timeless design with advanced health monitoring technology. The iconic rotating bezel provides intuitive navigation through the interface, while the premium stainless steel construction offers durability with an elegant appearance. The vibrant Super AMOLED display is protected by sapphire crystal glass, 1.5x stronger than previous generations. Advanced health sensors include Samsung BioActive Sensor for heart rate, ECG, and Bioelectrical Impedance Analysis for body composition measurements. Enhanced sleep coaching analyzes sleep patterns and provides personalized insights and recommendations for better rest. The advanced workout tracking supports over 90 exercise types with real-time metrics and form analysis for running and other activities. With up to 40 hours of battery life and fast charging that provides 45% in just 30 minutes, this versatile smartwatch keeps pace with your active lifestyle. The comprehensive ecosystem integration allows seamless connection with Galaxy smartphones, tablets, and TVs for a unified experience.'
WHERE product_name = 'Samsung Galaxy Watch6 Classic';

UPDATE products
SET description = 'The Samsung SmartThings Hub serves as the central control point for your smart home ecosystem, connecting and managing various compatible devices through a single platform. This compact device enables communication between different smart home protocols including Zigbee, Z-Wave, and Wi-Fi, allowing seamless integration of devices from various manufacturers. The intuitive SmartThings app provides centralized control of lights, thermostats, cameras, speakers, and other compatible devices. Automation capabilities allow you to create custom routines triggered by time, location, device status, or manual activation. The comprehensive scheduling feature enables devices to automatically adjust based on your daily activities. Advanced security features include real-time notifications for unexpected activity detected by compatible sensors and cameras. With voice assistant compatibility (Samsung Bixby, Amazon Alexa, and Google Assistant), you can control your smart home using natural voice commands. The energy management function monitors power consumption of compatible devices, helping you identify opportunities to reduce energy usage. This versatile hub transforms individual smart devices into a cohesive, intelligent home system that adapts to your lifestyle.'
WHERE product_name = 'Samsung SmartThings Hub';

-- HOUSEHOLD ITEMS

-- Kitchen Appliances (Category ID: 11)
UPDATE products
SET description = 'The Electrolux UltimateTaste 900 induction cooker revolutionizes home cooking with its advanced SenseFry technology, which maintains precise pan temperature for perfect cooking results. The intuitive TFT touch display provides easy access to all functions, with specific cooking settings for various food types. The FlexiBridge feature allows you to combine cooking zones to accommodate different pot sizes, while the Hob2Hood function automatically controls compatible range hoods based on cooking activity. The PowerBoost function delivers extra power for rapid boiling, reducing waiting time. The elegant frameless design with mirror-black glass surface complements modern kitchen aesthetics. Safety features include a child lock, automatic shut-off, and residual heat indicators. The PowerSlide function creates three preset temperature zones, allowing you to move pots between different heat levels without manual adjustment. With its combination of precise temperature control, intelligent automation, and flexible cooking zones, this premium induction cooker enhances both cooking performance and convenience.'
WHERE product_name = 'Electrolux UltimateTaste 900';

UPDATE products
SET description = 'The Electrolux MaxiMix Blender combines powerful performance with versatile functionality for all your blending needs. The robust 1200W motor with ProBlend technology efficiently processes tough ingredients, while the durable 6-blade assembly with titanium coating ensures long-lasting sharpness. The large 2-liter Tritan jar is BPA-free and shatterproof, with a convenient spout for clean pouring. The intuitive control panel offers 5 speed settings plus pulse function, along with 3 preset programs for smoothies, crushed ice, and soup. The innovative cooling system prevents overheating during extended use. The detachable blades and dishwasher-safe components make cleaning quick and easy. The sleek stainless steel design with LED-illuminated controls adds a premium touch to any kitchen. Additional features include a tamper tool for processing thick mixtures and a recipe book with diverse culinary inspirations. With its combination of powerful performance, versatile functionality, and durable construction, this high-performance blender is ideal for both everyday use and culinary exploration.'
WHERE product_name = 'Electrolux MaxiMix Blender';

UPDATE products
SET description = 'The Lock&Lock Air Fryer transforms your cooking experience with healthier, faster meal preparation using up to 85% less oil than traditional frying methods. The spacious 5.5-liter capacity accommodates family-sized portions, while the square basket design maximizes cooking space. The digital touch control panel with LED display offers 8 preset cooking functions for french fries, chicken, shrimp, steak, fish, pizza, vegetables, and baking. The powerful 1700W heating element with rapid air circulation technology ensures quick, even cooking from all angles. Temperature control ranges from 80°C to 200°C, with a 60-minute timer and automatic shut-off for safety. The non-stick basket and pan are dishwasher-safe for easy cleaning. The sleek design with matte finish complements modern kitchen aesthetics. Additional features include a recipe book with 30 culinary inspirations and a cool-touch exterior for safe handling during operation. With its combination of versatile functionality, convenient operation, and compact design, this air fryer makes healthy cooking accessible for everyday meals.'
WHERE product_name = 'Lock&Lock Air Fryer';

UPDATE products
SET description = 'The Lock&Lock Food Container Set provides a comprehensive storage solution with 10 versatile containers in various sizes and shapes. The patented 4-side locking system creates an airtight, watertight seal that prevents leaks and keeps food fresh up to 4 times longer than conventional storage. The durable BPA-free plastic construction is stain and odor resistant, maintaining clarity even after multiple uses. The containers are safe for use in freezer, microwave (without lid), and dishwasher (top rack), offering exceptional versatility for modern lifestyles. The space-efficient design allows for easy stacking and nesting, maximizing storage space when both in use and empty. The set includes 2 rectangular containers (1000ml, 470ml), 2 square containers (870ml, 350ml), 2 round containers (650ml, 300ml), and 4 small containers for sauces and dressings (150ml each). The transparent bodies allow for easy content identification, while measurement markings provide convenient portion control. This comprehensive set addresses a wide range of food storage needs, from meal prep to leftovers, with durability and functionality that enhances kitchen organization.'
WHERE product_name = 'Lock&Lock Food Container Set';

-- Kitchen Appliances (Continued)
UPDATE products
SET description = 'The Philips 3200 Series fully automatic espresso machine brings barista-quality coffee into your home with intuitive operation. The ceramic grinder with 12 adjustment settings ensures optimal extraction by grinding beans to your preferred consistency. The innovative LatteGo milk system mixes milk and air at high speed, creating a creamy layer of milk foam for perfect cappuccinos and lattes. The AquaClean filter technology allows you to brew up to 5000 cups without descaling by effectively removing minerals from water. The intuitive touch display makes it easy to select and customize your favorite coffee drinks, with options for espresso, coffee, cappuccino, and latte macchiato. The My Coffee Choice menu allows personalization of strength, volume, and temperature according to your preference. The classic milk frother provides an additional option for manual milk texturing. The efficient design includes a removable brew group for easy cleaning and maintenance. With its combination of user-friendly operation, consistent coffee quality, and easy maintenance, this espresso machine delivers exceptional value for coffee enthusiasts.'
WHERE product_name = 'Philips 3200 Series';

UPDATE products
SET description = 'The Philips Airfryer XXL transforms your cooking experience with its Twin TurboStar technology that removes fat from food and captures it in the fat reducer at the bottom of the air fryer. The spacious 7.3-liter capacity (1.4kg of food) accommodates family-sized portions, making it perfect for entertaining. The powerful 2225W heating element with rapid air circulation ensures quick, even cooking with crispy exteriors and tender interiors. The intuitive digital display with 5 preset cooking programs (frozen fries, meat, fish, whole chicken, and drumsticks) simplifies operation. The QuickClean basket with removable non-stick mesh is dishwasher-safe for easy maintenance. The unique starfish design at the bottom creates optimal airflow for consistent results. The Keep Warm function maintains temperature for up to 30 minutes after cooking. Additional features include a 60-minute timer with auto shut-off, adjustable temperature control from 80°C to 200°C, and a recipe book with over 30 dishes. With its combination of healthier cooking technology, large capacity, and user-friendly design, this air fryer offers exceptional versatility for everyday meals and special occasions.'
WHERE product_name = 'Philips Airfryer XXL';

UPDATE products
SET description = 'The Philips Hand Blender combines versatile functionality with powerful performance for effortless food preparation. The robust 800W motor with ProMix technology efficiently processes even tough ingredients, while the ergonomic grip provides comfortable handling during extended use. The innovative SpeedTouch button allows intuitive speed adjustment with a simple touch, giving you precise control over blending consistency. The stainless steel blade with titanium coating ensures long-lasting sharpness and resistance to discoloration from acidic ingredients. The anti-splash blade guard prevents messes during operation, keeping your kitchen clean. The comprehensive accessory set includes a 1-liter beaker, compact chopper for herbs and nuts, and whisk attachment for beating eggs and cream. The detachable blending arm with all dishwasher-safe parts makes cleaning quick and easy. The sleek design with metal accents adds a premium touch to your kitchen tools. With its combination of powerful motor, versatile attachments, and ergonomic design, this hand blender is the perfect multifunctional tool for everyday cooking.'
WHERE product_name = 'Philips Hand Blender';

-- Home Appliances (Category ID: 12)
UPDATE products
SET description = 'The Electrolux UltimateCare 900 washing machine represents the pinnacle of laundry care technology with its innovative SteamCare system that uses steam to reduce wrinkles by up to 30%, minimizing the need for ironing. The UltraMix technology pre-mixes detergent and water before it enters the drum, ensuring thorough penetration into fabrics for effective cleaning at lower temperatures. The high-efficiency inverter motor operates with minimal noise (72dB washing/74dB spinning) while providing superior energy efficiency with an A+++ energy rating. The spacious 10kg capacity accommodates large loads, while the 1600 RPM spin speed effectively removes excess water for faster drying. The intuitive touch control panel with advanced display provides access to 15 specialized programs, including UltraWash 59min, Anti-Allergy, Outdoor, Wool, and Delicates. The SensiCare system automatically adjusts the cycle time, water, and energy consumption according to load size. Additional features include a time delay option (up to 24 hours), child lock for safety, and Wi-Fi connectivity for remote monitoring and control through the Electrolux app. The durable stainless steel drum with gentle GentleCare design extends fabric life by providing optimal care for all textiles.'
WHERE product_name = 'Electrolux UltimateCare 900';

UPDATE products
SET description = 'The Electrolux PerfectCare 800 heat pump dryer represents advanced fabric care with GentleCare system that dries at half the temperature of conventional dryers, preserving the quality and appearance of your clothes. The SensiCare technology adjusts the cycle time according to moisture levels in each load, preventing over-drying while saving energy and time. The 9kg capacity accommodates large loads, perfect for family use. The heat pump technology achieves A++ energy efficiency, using significantly less energy than conventional condenser dryers. The intuitive touch control panel provides access to 9 specialized programs, including Bedding XL, Cotton, Delicates, Outdoor, Silk, Sports, Synthetics, Wool, and Mixed loads. The DelicateCare system optimizes temperature and drum movement according to fabric type, ensuring optimal care for all textiles. The EcoFlow System with easy-to-clean filters maintains efficient airflow for consistent performance. Additional features include a reverse tumbling action to prevent tangling, interior drum light for better visibility, and an extra silent operation (65dB) suitable for installation in living areas. The sleek design with anti-fingerprint stainless steel finish adds a premium touch to your laundry space.'
WHERE product_name = 'Electrolux PerfectCare 800';

UPDATE products
SET description = 'The LG InstaView Door-in-Door refrigerator redefines convenience with its innovative knock-twice feature that illuminates the interior glass panel, allowing you to see inside without opening the door and reducing cold air loss by up to 41%. The spacious 30 cubic feet capacity with adjustable shelving provides flexible storage for all your groceries. The Door-in-Door compartment offers quick access to frequently used items without opening the entire refrigerator. The Linear Cooling technology maintains temperature fluctuations within ±0.5°C for optimal food preservation, while Door Cooling+ delivers cool air to all corners for consistent temperature throughout. The inverter linear compressor operates with 25% less energy and 25% less noise compared to conventional compressors, with a 10-year warranty for long-term reliability. The dual ice maker produces both regular cubes and slow-melting craft ice spheres for premium beverages. The UVnano technology uses UV light to reduce bacteria on the water dispenser nozzle by 99.99% every 24 hours. Smart connectivity features include Wi-Fi with ThinQ technology for remote temperature control, proactive maintenance alerts, and compatibility with Google Assistant and Amazon Alexa for voice control. The sleek design with textured steel finish and recessed handles adds a premium touch to your kitchen.'
WHERE product_name = 'LG InstaView Door-in-Door';

UPDATE products
SET description = 'The LG DUAL Inverter air conditioner represents the cutting edge of climate control with its energy-efficient operation and advanced air purification. The revolutionary DUAL Inverter Compressor continuously adjusts its speed to maintain desired temperature with minimal fluctuation, using up to 70% less energy than non-inverter units. The 4-in-1 air purification system combines a PM1.0 sensor with multi-stage filtration to remove dust, allergens, viruses, and bacteria, while the Plasmaster Ionizer releases over 3 million ions to sterilize the air. The 4-way swing function distributes air flow in multiple directions for even cooling, while the 10-meter long-range air throw effectively cools larger rooms. The Smart Diagnosis feature allows easy troubleshooting through the LG ThinQ app, which also enables remote control and scheduling from anywhere. The 10-year warranty on the compressor provides long-term peace of mind. The quiet operation (19dB in Sleep mode) ensures peaceful environments, while the Auto Clean function prevents mold and bacteria growth by drying the interior components. The stylish design with hidden display complements modern interiors, with a sleek remote featuring a backlit screen for easy operation in darkness.'
WHERE product_name = 'LG DUAL Inverter AC';

UPDATE products
SET description = 'The LG CordZero A9 cordless stick vacuum delivers exceptional cleaning performance with its smart inverter motor generating powerful suction (160W in Turbo mode) while maintaining energy efficiency. The innovative dual PowerPack system includes two rechargeable lithium-ion batteries, each providing up to 60 minutes of runtime on Normal mode, for a combined 120 minutes of uninterrupted cleaning. The 5-step HEPA filtration system captures 99.999% of dust particles as small as 0.01 microns, making it ideal for allergy sufferers. The vacuum''s modular design allows transformation into multiple configurations: stick vacuum, handheld, or with the flexible Kompressor™ nozzle that bends up to 140° to reach under furniture without bending. The ThinQ app compatibility enables performance monitoring, maintenance reminders, and troubleshooting assistance. The portable charging stand provides convenient storage and charging without wall mounting, while the self-standing feature allows the vacuum to remain upright during cleaning pauses. The One-Touch Dust Empty button compresses and releases dust without direct contact, maintaining cleanliness during disposal. Additional accessories include a combination tool, crevice tool, pet nozzle, and flexible extension hose for comprehensive cleaning throughout the home.'
WHERE product_name = 'LG CordZero A9';

UPDATE products
SET description = 'The Philips Air Purifier 3000i combines advanced filtration technology with smart connectivity for superior indoor air quality. The professional-grade HEPA filter captures 99.97% of particles as small as 0.003 microns, including allergens, pollen, dust mites, and viruses. The activated carbon filter effectively removes harmful gases, odors, and volatile organic compounds (VOCs) from cooking, cleaning products, and external pollution. The powerful VitaShield IPS technology provides exceptional Clean Air Delivery Rate (CADR) of 400 m³/h, purifying a 48 m² room in just 8 minutes. The AeraSense technology continuously monitors air quality, displaying real-time PM2.5 levels on the digital interface and through a color-coded light ring (blue, blue-violet, blue-purple, red) for intuitive air quality indication. The Wi-Fi connectivity with dedicated Clean Home+ app allows remote monitoring and control, including scheduling, filter life tracking, and allergen management advice. The 5 automated modes (General, Allergen, Sleep, Turbo, and Bacteria & Virus) optimize performance for different scenarios, while the Turbo mode provides maximum purification for rapid air cleaning. The Sleep Mode operates at just 20 dB with dimmed lights for undisturbed rest. The intuitive touch controls with real-time feedback make operation simple, while the filter replacement indicator ensures continued performance.'
WHERE product_name = 'Philips Air Purifier 3000i';

UPDATE products
SET description = 'The Philips Steam Iron combines powerful performance with innovative technology for efficient, wrinkle-free results. The SteamGlide Plus soleplate with advanced ceramic coating glides smoothly over all fabrics, while the optimized design with precise tip allows easy access around buttons and into pleats. The powerful 2600W heating element ensures quick heat-up and consistent temperature, with the ThermoGuide function providing optimal heat settings for different fabric types. The continuous steam output (up to 50 g/min) effectively penetrates fabrics, while the 250g steam boost function tackles stubborn wrinkles in thick materials. The 320ml water tank enables extended ironing sessions with fewer refills. The built-in Calc-Clean slider prevents scale buildup, extending the iron''s lifespan and maintaining steam performance. The drip-stop system prevents water stains on delicate fabrics, even at lower temperatures. The 3m cord with 360° swivel provides excellent maneuverability, while the vertical steam function allows refreshing of hanging garments and curtains. Safety features include auto shut-off after 30 seconds when left horizontal and 8 minutes in vertical position. The ergonomic design with comfortable grip reduces hand fatigue during extended ironing sessions.'
WHERE product_name = 'Philips Steam Iron';

-- Furniture (Category ID: 13)
UPDATE products
SET description = 'The IKEA BILLY bookcase has become a classic storage solution, beloved for its versatility and timeless design since its introduction in 1979. The adjustable shelves can be arranged according to your needs, perfect for books of different sizes or display items. The surface-treated ash veneer provides natural wood beauty while offering improved durability and easy cleaning. The shallow depth (28cm) makes this bookcase ideal for limited spaces, while still providing ample storage capacity. The included wall anchoring fittings ensure stability and safety, preventing tipping accidents. The clean, simple design complements various interior styles, from traditional to contemporary. The bookcase is available in multiple heights (106cm, 202cm, 237cm) and widths (40cm, 80cm), allowing for customized configurations to fit your space. Optional glass doors and height extension units provide additional versatility and protection for your collection. The adjustable feet provide stability even on uneven floors. Crafted from sustainable wood sources with minimal waste in production, the BILLY represents IKEA''s commitment to environmental responsibility. With its combination of functional design, adaptability, and affordable price point, this versatile bookcase has earned its place as a global furniture icon.'
WHERE product_name = 'IKEA BILLY';

UPDATE products
SET description = 'The IKEA MALM bed frame combines minimalist design with practical functionality, featuring clean lines and a low profile that complement contemporary interiors. The robust wooden frame with veneer finish provides both aesthetic appeal and durability for long-term use. The innovative storage solution includes two large drawers (or four for larger sizes) that roll out smoothly on casters, offering convenient space for seasonal clothing, extra bedding, or other items. The adjustable bed sides accommodate mattresses of different thicknesses for optimal comfort. The solid wood veneer construction in white stained oak provides natural wood beauty with enhanced resistance to scratches and stains. The 32cm height clearance provides convenient storage space beneath the bed, even without using the drawers. Assembly is simplified with pre-drilled holes and comprehensive instructions. The bed is available in multiple sizes (Twin, Full, Queen, King) to accommodate different room dimensions and sleeping preferences. The MALM pairs perfectly with other furniture from the MALM series for a coordinated bedroom aesthetic. All materials meet strict health and safety standards, ensuring a healthy sleeping environment free from harmful chemicals.'
WHERE product_name = 'IKEA MALM';

UPDATE products
SET description = 'The IKEA POÄNG armchair represents Scandinavian design excellence, combining form, function, and comfort in a timeless package introduced in 1976 and continuously refined since. The layer-glued bentwood frame made from birch provides resilient flexibility that gently moves with your body, creating a natural rocking motion that enhances relaxation. The high back with headrest offers excellent support for your entire body, while the ergonomic design promotes proper posture during extended sitting. The replaceable cushion covers in various materials and colors allow for easy styling updates to match changing décor. The durable construction has been tested to withstand 56,000 cycles of simulated use, ensuring years of reliable service. The lightweight design (7kg) makes repositioning simple, while the distinctive curved wooden runners add architectural interest to your space. The chair is available with various cushion options, from cotton and polyester blends to premium leather, accommodating different comfort preferences and budget considerations. The matching footstool enhances comfort by providing elevated leg support. The simple assembly requires no tools, allowing quick setup with minimal effort. With its combination of ergonomic comfort, distinctive design, and sustainable materials, the POÄNG remains one of IKEA''s most beloved seating options.'
WHERE product_name = 'IKEA POÄNG';

UPDATE products
SET description = 'The IKEA KALLAX shelving unit offers exceptional versatility with its distinctive cube design that works equally well as a room divider, storage solution, or display shelf. The square compartments (33x33cm) provide perfect spaces for KALLAX storage accessories or standard record albums, making it popular among vinyl enthusiasts. The sturdy construction supports up to 13kg per shelf, allowing for substantial storage capacity without sagging. The clean, minimalist design complements various interior styles from contemporary to traditional. The shelving unit is available in multiple configurations (2x2, 2x4, 4x4, 5x5 cubes) and finishes (white, black-brown, walnut effect, high-gloss, etc.) to suit different spaces and aesthetic preferences. The extensive range of compatible inserts includes drawers, doors, wire baskets, and fabric boxes, allowing customized organization solutions for various items. The reversible design works equally well horizontally or vertically, adapting to your space requirements. The smooth, easy-to-clean surfaces require minimal maintenance, with melamine coating providing resistance to moisture and scratches. Wall anchoring fittings are included for enhanced stability and safety. With its combination of functional design, adaptability, and affordable price point, this versatile shelving system has become a modern classic in home organization.'
WHERE product_name = 'IKEA KALLAX';

UPDATE products
SET description = 'The IKEA HEMNES collection represents traditional craftsmanship with a contemporary sensibility, featuring the 8-drawer dresser as a standout storage solution. Crafted from solid pine, a natural and renewable material, this dresser offers authentic wood character with unique grain patterns in each piece. The smooth-running drawers with stop mechanisms prevent pulling out too far, enhancing safety and functionality. The spacious drawers with felt liners protect delicate items while providing ample storage for clothing and accessories. The included anti-tip hardware ensures safety by securing the dresser to the wall, preventing accidents. The classic design with decorative details and profiled edges brings timeless elegance to bedroom spaces. The sturdy construction ensures durability for years of reliable use, supporting up to 25kg per drawer. The solid wood construction enables repairs and refinishing, extending the furniture''s lifespan. The white stain finish offers versatile styling potential while allowing the natural wood grain to show through. The environmentally conscious production uses wood from sustainable forests with responsible harvesting practices. The comprehensive quality testing includes weight, stability, and durability assessments, ensuring reliable performance throughout years of daily use.'
WHERE product_name = 'IKEA HEMNES';

-- Bathroom Items (Category ID: 15)
UPDATE products
SET description = 'The Philips Sonicare DiamondClean smart electric toothbrush represents the pinnacle of oral care technology with its advanced features and connected capabilities. The unique sonic technology delivers 31,000 brush strokes per minute, creating dynamic fluid action that cleans deep between teeth and along the gum line while remaining gentle on sensitive tissues. The Smart Sensor technology tracks brushing motion, pressure, location, duration, and frequency, providing real-time guidance through the Sonicare app to optimize your technique. The five brushing modes (Clean, White+, Deep Clean+, Gum Health, and Tongue Care) with three intensity settings allow personalized care for different oral health needs. The premium brush head range includes DiamondClean for stain removal, AdaptiveClean for gum care, TongueCare+ for fresh breath, and ProResults for plaque removal, with automatic recognition that adjusts the recommended mode. The elegant glass charging base doubles as a rinse cup, while the travel case with USB charging maintains power during travel. The rechargeable battery provides up to 14 days of regular use on a single charge. The brush handle features an illuminated display showing selected mode, battery status, and replacement reminders for brush heads. Clinically proven to remove up to 10x more plaque, improve gum health up to 7x in just two weeks, and remove up to 100% more stains in just three days compared to manual brushing.'
WHERE product_name = 'Philips Sonicare DiamondClean';

UPDATE products
SET description = 'The Electrolux Water Heater combines energy efficiency with precise temperature control for optimal showering comfort. The advanced flow sensor technology adjusts heating power according to water flow and input temperature, maintaining stable output temperature regardless of pressure fluctuations. The digital LCD display provides precise temperature setting in 1°C increments from 30°C to 55°C, allowing customized comfort for different users. The compact design (38cm x 22cm x 9cm) requires minimal wall space while delivering powerful performance for whole-bathroom use. The multiple safety systems include overheat protection, pressure relief valve, leak detection, and automatic power-off if abnormalities are detected. The class-leading energy efficiency rating (A+) reduces electricity consumption while providing consistent hot water. The durable copper heating element with scale-resistant coating ensures long-term performance even in hard water areas. The silent operation (below 15dB) enhances bathroom tranquility, while the sleek design with fingerprint-resistant finish complements modern bathroom aesthetics. The easy installation with included mounting template and flexible water connections simplifies setup for both replacement and new installations. The comprehensive 5-year warranty on the heating element and 2-year warranty on other components provide long-term peace of mind.'
WHERE product_name = 'Electrolux Water Heater';

UPDATE products
SET description = 'The IKEA GODMORGON bathroom vanity combines sophisticated design with practical storage solutions for organized bathroom spaces. The wall-mounted installation creates a floating appearance that enhances visual spaciousness while facilitating floor cleaning. The two fully-extending drawers provide complete visibility of contents and easy access to items at the back, with dividers for organized storage of smaller bathroom essentials. The smart interior features include removable dividers and boxes for customized organization. The durable construction with laminate finish offers excellent moisture resistance, ideal for humid bathroom environments. The smooth-running drawers with soft-closing dampers prevent slamming and pinched fingers. The vanity accommodates various sink and faucet options (sold separately) for personalized bathroom styling. The 10-year warranty provides confidence in long-term quality and performance. The adjustable legs accommodate uneven bathroom floors for perfect leveling. The smart design includes concealed cable management solutions for electric toothbrushes and hair appliances. The comprehensive quality testing includes humidity resistance, weight capacity, and durability assessments to ensure reliable performance in demanding bathroom conditions. Available in multiple sizes (60cm, 80cm, 100cm, 120cm) and finishes (high-gloss white, white stained oak, black-brown, gray) to complement different bathroom dimensions and décor styles.'
WHERE product_name = 'IKEA GODMORGON';

UPDATE products
SET description = 'The IKEA BROGRUND bathroom accessories set provides coordinated solutions for organized and functional bathroom spaces. The comprehensive collection includes towel rail, toilet roll holder, toilet brush, soap dispenser, toothbrush holder, hooks, and corner shelf unit, allowing complete bathroom coordination. The durable stainless steel construction with corrosion-resistant coating ensures longevity in humid bathroom environments. The sleek, minimalist design complements various bathroom styles from contemporary to traditional. The smart mounting system with concealed screws creates a clean, seamless appearance. The corner shelf unit maximizes storage in underutilized spaces, with drainage holes preventing water accumulation. The toilet brush features a replaceable brush head for hygienic maintenance. The towel rail accommodates multiple towels within a compact footprint. The multi-purpose hooks support up to 2kg each, providing convenient hanging for bathrobes, towels, and clothing. The soap dispenser features a non-drip pump mechanism to keep countertops clean. The 10-year warranty demonstrates confidence in quality and durability. The easy installation with included mounting hardware and instructions simplifies setup. All materials meet strict environmental and health standards, ensuring safety for family use. With its combination of functional design, quality materials, and coordinated aesthetic, this comprehensive set elevates both the form and function of bathroom spaces.'
WHERE product_name = 'IKEA BROGRUND';

-- Home Decor (Category ID: 16)
UPDATE products
SET description = 'The IKEA STOCKHOLM collection represents the pinnacle of IKEA''s design philosophy, combining exceptional craftsmanship with timeless Scandinavian aesthetics. The handwoven rug with wool blend construction offers natural beauty and outstanding durability, with wool''s inherent soil-resistance and resilience to crushing. The skilled craftsmanship is evident in the perfectly straight edges and consistent pattern throughout the piece. The flatwoven technique creates a reversible design that can be used on either side, effectively doubling the rug''s lifespan. The 100% wool surface provides natural warmth and comfort underfoot, while the cotton warp ensures dimensional stability. The versatile geometric pattern complements both traditional and contemporary interiors with its subtle sophistication. The rug is available in multiple sizes (170x240cm, 250x350cm) and color combinations (dark blue/beige, off-white/gray) to suit different room dimensions and décor schemes. The natural wool fibers have inherent flame-retardant properties for enhanced safety. The renewable materials reflect IKEA''s commitment to environmental responsibility and sustainable sourcing. Regular vacuuming and occasional professional cleaning maintain the rug''s appearance, with natural wool''s ability to resist staining and retain its beauty for years.'
WHERE product_name = 'IKEA STOCKHOLM';

UPDATE products
SET description = 'The IKEA RIBBA picture frame set provides versatile display solutions for creating personalized gallery walls and preserving precious memories. The set includes 8 frames in various sizes (10x15cm, 13x18cm, 21x30cm, 30x40cm, 40x50cm) and orientations (portrait and landscape), allowing dynamic arrangements that highlight different photo sizes. The clean, minimalist design with slim profile (2cm depth) complements diverse interior styles from contemporary to traditional. The included mat enhances presentation by creating visual space around the image, with pre-cut openings perfectly centered for professional-looking results. The durable construction with plastic front provides lightweight hanging and safety for family spaces compared to glass alternatives. The frames feature stable fold-out stands for tabletop display and integrated hanging hardware for wall mounting, offering flexible positioning options. The consistent design across all sizes creates a cohesive look when grouped together, while the versatile black finish coordinates with various color schemes. The protective packaging ensures frames arrive in perfect condition, with each frame individually wrapped. The easy assembly requires no tools, allowing immediate display of cherished images. With its combination of functional design, display versatility, and affordable price point, this comprehensive frame set simplifies the creation of personalized wall galleries.'
WHERE product_name = 'IKEA RIBBA';

UPDATE products
SET description = 'The IKEA FEJKA artificial potted plants offer lifelike greenery without the maintenance requirements of living plants. The remarkably realistic appearance includes detailed leaves with subtle variations in color and texture that mimic natural growth patterns. The versatile collection includes various plant types (succulents, hanging plants, tropical specimens) suitable for different decorative applications. The durable plastic construction maintains its appearance without fading, watering, or sunlight requirements, making these plants ideal for spaces with limited natural light. The included decorative pots complement the plants while providing stable bases, with some designs featuring drainage holes for authentic appearance. The bendable stems and branches on selected models allow customized positioning to create natural-looking arrangements. The maintenance-free nature eliminates concerns about allergies, pests, over/under watering, or vacation care arrangements. The dust-resistant materials are easily cleaned with a feather duster or damp cloth. These artificial plants work beautifully in challenging locations like high shelves, bathroom environments, or offices with irregular attendance. The lightweight construction simplifies repositioning when refreshing room arrangements. With their combination of realistic appearance, versatile styling options, and zero maintenance requirements, these artificial plants provide enduring greenery that enhances interior spaces year-round.'
WHERE product_name = 'IKEA FEJKA';

UPDATE products
SET description = 'The IKEA SYMFONISK collection, developed in collaboration with Sonos, innovatively blends high-quality audio equipment with functional furniture pieces. The table lamp with integrated WiFi speaker combines ambient lighting with room-filling sound in a single device, reducing clutter and power outlets needed. The advanced speaker technology delivers rich, vibrant sound with two class-D digital amplifiers, one tweeter, and one mid-woofer for clear highs and dynamic mid-ranges. The seamless integration with Sonos ecosystem allows synchronization with other Sonos or SYMFONISK speakers for multi-room audio experiences. The WiFi connectivity provides superior sound quality and stability compared to Bluetooth, with support for AirPlay 2, Spotify Connect, and over 100 streaming services through the Sonos app. The touch controls allow easy volume and playback management, while voice control is available when connected to Alexa or Google Assistant-enabled devices. The textile lamp shade creates soft, atmospheric illumination (compatible with E12/E14 bulbs up to 7W LED or 40W incandescent), with separate controls for audio and lighting functions. The compact dimensions (21cm diameter, 40cm height) allow placement on bedside tables, sideboards, or bookshelves. Two color combinations (white/light oak, black/dark oak) complement diverse interior styles. The TruePlay tuning feature (iOS devices) optimizes sound for each room''s specific acoustics. With its dual functionality and streamlined design, this innovative product exemplifies thoughtful integration of technology into home environments.'
WHERE product_name = 'IKEA SYMFONISK';

-- FASHION PRODUCTS

-- Men's Fashion (Category ID: 17)
UPDATE products
SET description = 'The Adidas Ultraboost 23 represents the pinnacle of running shoe innovation, featuring the revolutionary BOOST midsole technology that provides 23% more cushioning compared to previous models. The responsive midsole returns energy with each stride, reducing fatigue during long-distance runs. The Primeknit+ upper adapts to your foot''s changing shape during movement, providing supportive comfort with enhanced breathability through strategically placed ventilation zones. The Linear Energy Push system with 45-degree angle construction increases forefoot bending stiffness by 15%, delivering smooth transitions and enhanced running economy. The Continental™ Rubber outsole provides exceptional grip in both wet and dry conditions, with Stretchweb technology that flexes naturally with your foot while decreasing pressure points. The reinforced heel counter ensures proper alignment and stability, while the Achilles pad prevents irritation during extended wear. The shoe is crafted with Parley Ocean Plastic, containing at least 50% recycled polyester and intercepted plastic waste from coastal communities. The TORSION SYSTEM provides midfoot integrity, reducing unwanted flex and supporting natural foot movement. Available in men''s sizes US 7-14 and various colorways, this premium running shoe combines performance technology with environmental consciousness for runners seeking both comfort and responsibility.'
WHERE product_name = 'Adidas Ultraboost 23';

UPDATE products
SET description = 'The Adidas Tiro Track Jacket has become an iconic sportswear staple, combining athletic functionality with streetwear appeal. The lightweight polyester fabric with AEROREADY technology wicks moisture away from the skin, keeping you dry and comfortable during activity. The ergonomic design features raglan sleeves for enhanced range of motion and ribbed cuffs with thumb holes for secure positioning during movement. The full-length front zipper with chin guard prevents irritation, while the zippered side pockets provide secure storage for small essentials. The iconic three-stripe design along the sleeves creates an instantly recognizable athletic aesthetic. The standing collar offers additional neck protection and styling options. The slim fit design provides a modern silhouette without restricting movement, with ventilated climacool® technology that enhances airflow in high-heat areas. The jacket is constructed with recycled polyester made from post-consumer plastic bottles, reflecting Adidas'' commitment to sustainability. Available in men''s sizes XS-3XL and multiple colorways from classic black/white to bold team color combinations. The machine-washable fabric maintains its shape and performance properties even after repeated washing. With its combination of functional design, comfortable materials, and versatile styling potential, this track jacket transitions seamlessly from training sessions to casual wear.'
WHERE product_name = 'Adidas Tiro Track Jacket';

UPDATE products
SET description = 'The Nike Air Force 1 has maintained its status as a footwear icon since its 1982 debut, when it revolutionized basketball shoes by introducing Nike Air technology to the court. The durable leather upper provides structured support while developing a personalized patina with wear. The perforated toe box enhances breathability during extended wear. The padded collar and tongue deliver cushioned comfort around the ankle. The hidden Air-Sole unit in the midsole provides lightweight cushioning that has become synonymous with the Air Force 1 experience. The non-marking rubber outsole with circular pivot point pattern offers excellent traction on various surfaces, with the distinctive star pattern that has become a recognizable design element. The classic cup sole construction with stitched overlays embodies the shoe''s durability and timeless design language. The versatile aesthetic transitions seamlessly from athletic contexts to streetwear settings, with the distinctive "AF1" metal lace dubrae adding an authentic finishing touch. Available in men''s sizes US 6-18 and numerous colorways and material variations, from the quintessential all-white to seasonal designer collaborations. The cushioned footbed provides all-day comfort, while the variable width lacing system allows customized fit adjustment. With its combination of innovative technology, distinctive design, and cultural significance, the Air Force 1 continues to influence both performance basketball and street fashion.'
WHERE product_name = 'Nike Air Force 1';

-- Men's Fashion (Continued)
UPDATE products
SET description = 'The Nike Dri-FIT T-Shirt combines performance technology with everyday comfort for versatile athletic wear. The innovative Dri-FIT technology wicks sweat away from the skin to the fabric surface where it evaporates quickly, keeping you dry and comfortable during workouts. The lightweight polyester blend (100% recycled polyester) provides durability and environmental consciousness. The athletic fit offers freedom of movement without excessive fabric, featuring ergonomic flat-lock seams that reduce potential friction and irritation during activity. The reinforced crew neckline maintains its shape wash after wash, while the tagless design eliminates neck irritation. The breathable fabric construction allows efficient airflow to regulate body temperature during intense activities. The shirt is available in men''s sizes S-3XL and numerous colorways from classic black and white to seasonal color options. Anti-odor technology inhibits the growth of odor-causing microbes, keeping the shirt fresher during extended wear. The fabric offers UPF 40+ sun protection for outdoor training sessions. Machine washable for easy care, the shirt maintains its shape, color, and performance properties even after repeated washing. With its combination of moisture management, comfortable fit, and versatile styling potential, this performance shirt transitions seamlessly from training sessions to casual wear.'
WHERE product_name = 'Nike Dri-FIT T-Shirt';

UPDATE products
SET description = 'The Zara Slim Fit Blazer elevates everyday style with its tailored silhouette and versatile design. The refined slim fit provides a contemporary profile without restricting movement, with subtle waist suppression creating a flattering silhouette. The premium fabric blend (63% polyester, 35% viscose, 2% elastane) offers comfortable stretch and excellent shape retention. The notched lapels with balanced proportions work equally well with formal or casual styling. The two-button front provides classic closure with a tasteful placement at natural waist level. The chest welt pocket and flap side pockets maintain clean lines while offering practical storage. The four-button functional cuffs add authentic tailoring details. The double back vent enhances comfort when seated and creates a graceful silhouette when walking. The interior features three pockets for secure storage of essentials like cards, phone, or tickets. The partial lining construction reduces weight while maintaining structure in key areas. Available in men''s sizes 36-46 and versatile colors (navy, black, beige) that complement diverse wardrobe combinations. The structured shoulders provide a defined silhouette without excessive padding. Machine washable for convenient home care, this refined blazer maintains its shape and appearance with minimal maintenance. With its combination of tailored refinement and contemporary styling, this versatile blazer transitions effortlessly from business meetings to evening occasions.'
WHERE product_name = 'Zara Slim Fit Blazer';

UPDATE products
SET description = 'The Zara Chino Trousers combine timeless style with modern comfort for versatile everyday wear. The tailored straight fit through hip and thigh with slight tapering below the knee creates a streamlined silhouette that complements diverse body types. The premium cotton twill fabric (98% cotton, 2% elastane) provides durability and natural breathability with comfortable stretch for ease of movement. The mid-rise waistband with belt loops and hidden stretch interior ensures comfort during extended wear. The zipper fly with button closure offers secure fastening without bulk. The two side slant pockets and two back welt pockets with button closure provide practical storage while maintaining clean lines. The pre-hemmed length options (30", 32", 34") eliminate the need for alterations for most wearers. The meticulous garment dye process creates rich, nuanced colors with subtle variation that develops character over time. Available in men''s sizes 28-40 waist and versatile colors (beige, navy, olive, black) that complement diverse wardrobe combinations. The refined interior finishing with patterned pocket bags adds subtle sophistication to these everyday trousers. Machine washable for convenient home care, the fabric maintains its shape and appearance with minimal special maintenance. With their combination of classic styling, comfortable materials, and attentive detailing, these versatile trousers transition seamlessly from office settings to weekend occasions.'
WHERE product_name = 'Zara Chino Trousers';

UPDATE products
SET description = 'The Zara Oxford Shirt represents timeless versatility with its classic design and attentive details. The premium cotton Oxford fabric (100% cotton) provides natural breathability and a subtly textured appearance that becomes increasingly comfortable with each wash. The regular fit offers comfortable wearing ease without excess fabric, featuring a slightly tailored waist for a refined silhouette. The button-down collar provides a classic American styling detail that keeps its shape throughout the day. The single front pocket adds practical utility while maintaining clean lines. The rounded barrel cuffs with two-button adjustment allow customized fit at the wrist. The reinforced side gussets at the hem enhance durability at stress points during movement. The mother-of-pearl buttons provide subtle luxury and improved durability compared to plastic alternatives. Available in men''s sizes S-XXL and essential colors (white, light blue, navy, pink) that form the foundation of a versatile wardrobe. The durable double-needle seams enhance longevity through regular washing. The back box pleat provides additional wearing ease across the shoulders during movement. Machine washable for convenient home care, the fabric develops a distinctive patina over time that enhances its character. With its combination of classic design, quality materials, and attentive construction, this versatile shirt transitions seamlessly from business settings to weekend occasions.'
WHERE product_name = 'Zara Oxford Shirt';

-- Women's Fashion (Category ID: 18)
UPDATE products
SET description = 'The Adidas Cloudfoam Pure running shoes combine exceptional comfort with sleek, feminine design for versatile everyday performance. The innovative Cloudfoam memory sockliner and midsole provide pillow-soft cushioning that molds to your foot shape for personalized comfort. The stretchy mesh upper offers sock-like fit and breathability, adapting to different foot shapes while facilitating airflow during activity. The unique step-in construction creates a streamlined silhouette and allows effortless on/off convenience. The memory foam-lined footbed and padded heel enhance comfort during extended wear. The lightweight design (8.8oz for size 7) reduces fatigue during all-day wear or extended walking. The flexible rubber outsole provides reliable traction on various surfaces while allowing natural foot movement. The minimalist design with subtle branding transitions seamlessly from workout sessions to casual settings. Available in women''s sizes US 5-11 and numerous colorways from classic white and black to seasonal color options. The heel pull tab facilitates easy entry, while the lace closure allows personalized fit adjustment. The shoes are constructed with partially recycled materials, reflecting Adidas'' commitment to environmental responsibility. With their combination of cushioned comfort, lightweight construction, and versatile styling potential, these performance shoes effortlessly blend athletic functionality with everyday wearability.'
WHERE product_name = 'Adidas Cloudfoam Pure';

UPDATE products
SET description = 'The Adidas Essentials Hoodie delivers casual comfort with iconic athletic heritage for versatile everyday wear. The soft cotton-blend fleece (80% cotton, 20% recycled polyester) provides cozy warmth with environmental consciousness. The relaxed fit offers comfortable wearing ease without appearing oversized, featuring dropped shoulders for a contemporary silhouette. The lined drawstring hood with crossover design provides adjustable coverage and enhanced warmth around the neck. The kangaroo pocket offers practical hand warming and secure storage for small essentials. The ribbed cuffs and hem maintain their shape while providing a secure fit that keeps cold air out. The raglan sleeve construction allows free range of motion without pulling across the shoulders. The subtle embroidered Trefoil logo on chest provides authentic branding without overwhelming the clean design. Available in women''s sizes XS-2XL and essential colors (black, gray heather, pink, navy) that complement diverse wardrobe combinations. The brushed interior creates exceptional softness against the skin, while the durable exterior maintains its appearance through repeated washing. Machine washable for convenient home care, the fabric resists pilling even after multiple laundry cycles. With its combination of cozy comfort, thoughtful details, and versatile styling potential, this essential hoodie transitions seamlessly from workout warm-ups to casual weekend wear.'
WHERE product_name = 'Adidas Essentials Hoodie';

UPDATE products
SET description = 'The Nike Air Max 270 women''s lifestyle shoes revolutionize all-day comfort with the brand''s first lifestyle Air unit specifically designed for Nike Sportswear. The massive 32mm heel Air unit provides unprecedented cushioning, creating a distinctive silhouette while delivering responsive comfort with every step. The engineered mesh upper offers strategic breathability, with areas of stretch and structure placed precisely where needed. The bootie construction creates a sock-like fit that hugs the foot without restriction. The asymmetrical lacing system reduces pressure points for enhanced comfort during extended wear. The dual-density foam midsole (softer in forefoot, firmer in heel) provides balanced comfort and support. The rubber toe tip enhances durability in high-wear areas, while the rubber heel clip adds stability around the Air unit. The heritage details like the "AIR" logo and exaggerated tongue nod to Nike''s Air Max legacy. The lightweight design (8.5oz for size 8) maintains comfort during all-day wear. Available in women''s sizes US 5-12 and numerous colorways from subtle neutrals to bold color combinations. The reflective details enhance visibility in low-light conditions. With its combination of maximum cushioning, breathable comfort, and distinctive design heritage, these versatile lifestyle shoes transition seamlessly from active moments to everyday wear.'
WHERE product_name = 'Nike Air Max 270';

UPDATE products
SET description = 'The Nike Sportswear Leggings combine athletic performance with contemporary style for versatile everyday wear. The high-waisted design provides secure coverage and core support, with a wide elastic waistband that doesn''t dig in or roll down during activity. The Dri-FIT technology wicks moisture away from the skin to the fabric surface where it evaporates, helping you stay dry and comfortable. The premium fabric blend (83% recycled polyester, 17% spandex) offers exceptional stretch and recovery while reflecting Nike''s commitment to sustainability. The ergonomic seaming contours to your body''s natural curves without restrictions. The gusseted crotch construction allows complete range of motion without fabric tension. The flatlock seams reduce potential irritation during extended wear or dynamic movement. The minimal reflective elements enhance visibility in low-light conditions. The small interior pocket at waistband accommodates a key or credit card during active pursuits. Available in women''s sizes XS-2XL and versatile colors (black, navy, gray, olive) that complement diverse wardrobe combinations. The opaque fabric provides confident coverage even during deep stretches or squats. Machine washable for convenient home care, the fabric maintains its shape, compression, and color through repeated washing. With their combination of comfortable support, performance features, and versatile styling potential, these essential leggings transition seamlessly from workout sessions to casual daily wear.'
WHERE product_name = 'Nike Sportswear Leggings';

UPDATE products
SET description = 'The Zara Pleated Midi Skirt combines timeless elegance with contemporary styling for versatile wardrobe versatility. The feminine A-line silhouette with knife pleats creates graceful movement with every step, while maintaining a structured appearance when stationary. The comfortable high-rise waistband with hidden elastic section ensures all-day comfort while creating a flattering waistline. The premium fabric (100% recycled polyester) offers environmental consciousness without compromising on the luxurious drape and resilient pleating. The invisible side zipper provides secure closure without disrupting the clean lines of the design. The midi length (30 inches) offers versatile styling potential, equally elegant with both flats and heels. The lightweight lining ensures opacity while maintaining the airy feel of the skirt. The meticulous heat-set pleating retains its structure even after washing, requiring minimal maintenance to maintain its polished appearance. Available in women''s sizes XS-XL and versatile colors (black, beige, navy, emerald) that complement diverse wardrobe combinations. The machine-washable construction allows convenient home care despite the sophisticated appearance. The understated design transitions seamlessly from professional settings with a blouse to evening occasions with a statement top. With its combination of elegant movement, comfortable fit, and versatile styling potential, this refined skirt brings feminine sophistication to diverse occasions throughout the seasons.'
WHERE product_name = 'Zara Pleated Midi Skirt';

UPDATE products
SET description = 'The Zara Oversized Blazer redefines power dressing with its contemporary interpretation of a classic silhouette. The relaxed fit with strong shoulders creates a commanding presence while allowing comfortable layering over various outfits. The premium fabric blend (63% polyester, 34% viscose, 3% elastane) provides structured drape with comfortable stretch and excellent shape retention. The notched lapels with balanced proportions frame the face while maintaining the oversized aesthetic. The double-breasted front with tortoiseshell buttons offers classic closure with a distinctive accent. The flap pockets maintain clean lines while providing practical storage. The single back vent enhances comfort when seated and creates a graceful silhouette when walking. The interior features coordinating lining with three pockets for secure storage of essentials. The padded shoulders provide defined structure without appearing excessively formal. The slightly elongated sleeves with three-button detail add to the relaxed, contemporary appearance. Available in women''s sizes XS-XL and versatile colors (black, beige, check pattern) that complement diverse wardrobe combinations. The unexpected versatility allows styling from professional settings with tailored trousers to weekend occasions with jeans or over a dress. Machine washable for convenient home care, this statement blazer maintains its shape and appearance with minimal maintenance. With its combination of bold proportions, refined details, and styling flexibility, this versatile blazer adds architectural interest to any outfit.'
WHERE product_name = 'Zara Oversized Blazer';

UPDATE products
SET description = 'The Zara High Waist Jeans combine timeless style with contemporary comfort for versatile everyday wear. The flattering high-rise waistband sits at the natural waist, creating an elongated leg line while providing comfortable core support. The skinny fit contours to the body with a streamlined silhouette from hip to ankle, showcasing the premium stretch denim (92% cotton, 6% polyester, 2% elastane) that offers exceptional recovery to maintain shape throughout the day. The five-pocket styling provides practical utility with authentic denim detailing. The zip fly with button closure offers secure fastening with a clean appearance. The strategic fading pattern creates dimension without appearing artificially distressed. The ankle-length design (28" inseam) provides versatile styling with both boots and shoes throughout the seasons. The contoured waistband prevents gapping at the back, while belt loops allow accessorizing options. Available in women''s sizes 24-36 waist and versatile washes (dark blue, medium blue, black) that complement diverse wardrobe combinations. The reinforced stitching at stress points enhances durability through regular wear and washing. Machine washable for convenient home care, the denim maintains its shape, color, and comfortably worn-in feel with each wash. With their combination of flattering fit, comfortable stretch, and versatile styling potential, these essential jeans transition seamlessly from casual settings to evening occasions when paired with more formal tops.'
WHERE product_name = 'Zara High Waist Jeans';

-- Kids' Fashion (Category ID: 19)
UPDATE products
SET description = 'The Adidas Kids Superstar brings iconic street style to young feet, featuring the same classic design elements that have made the adult version a global phenomenon since 1969. The durable leather upper provides structured support while developing character with wear, complemented by the signature rubber shell toe that offers both protection and distinctive style. The three-stripe perforated design provides authentic branding with enhanced breathability. The herringbone-pattern rubber outsole delivers reliable traction for active play, while the cushioned sockliner enhances comfort during all-day wear. The secure lace closure with reinforced eyelets provides adjustable fit, with an additional hook-and-loop strap option for younger kids who haven''t mastered tying yet. The padded collar and tongue enhance comfort around the ankle. The trefoil logo on the heel tab adds authentic heritage detailing. The iconic silhouette transitions seamlessly from school settings to playground adventures. Available in kids'' sizes US 10.5K-3Y (Little Kids) and 3.5Y-7Y (Big Kids) and classic colorways (white/black, all white, all black) along with seasonal color options. The durable construction withstands the rigors of active children, while maintaining the iconic style that appeals to both kids and parents. With its combination of heritage design, comfortable fit, and versatile styling potential, this classic sneaker introduces young wearers to authentic street style with age-appropriate functionality.'
WHERE product_name = 'Adidas Kids Superstar';

UPDATE products
SET description = 'The Adidas Kids Tracksuit delivers classic athletic style with playful energy for young active lifestyles. The coordinated jacket and pants create an instantly put-together look with minimal effort. The lightweight tricot fabric (100% recycled polyester) provides smooth comfort with environmental consciousness. The jacket features a full-length front zipper with chin guard to prevent irritation, raglan sleeves for enhanced range of motion, and ribbed cuffs and hem for a secure fit. The pants include an elastic waistband with drawcord for adjustable comfort, tapered legs with ribbed cuffs to prevent riding up during play, and side pockets for storing small treasures. The iconic three-stripe design along the sleeves and pant legs creates instantly recognizable athletic styling. The moisture-wicking AEROREADY technology helps keep young athletes dry and comfortable during active play. The contrast piping adds visual interest and defines the athletic silhouette. Available in kids'' sizes 4-16 and playful color combinations (navy/red, black/white, purple/pink) that appeal to children''s preferences. The durable construction withstands playground adventures and sports activities, while the machine-washable fabric simplifies care for busy parents. The versatile design transitions seamlessly from physical education classes to after-school activities and weekend outings. With its combination of comfortable performance features, iconic styling, and durable construction, this coordinated set provides practical everyday wear for active kids.'
WHERE product_name = 'Adidas Kids Tracksuit';

UPDATE products
SET description = 'The Nike Kids Air Max brings legendary cushioning technology to growing feet, scaled specifically for young wearers while maintaining the distinctive style of this iconic sneaker line. The visible Air-Sole unit in the heel provides responsive cushioning that helps protect developing joints during high-impact play. The breathable mesh upper with synthetic overlays offers structured support while allowing airflow to keep active feet cool and comfortable. The foam midsole provides additional cushioning for all-day comfort during school and play. The durable rubber outsole with waffle pattern delivers reliable traction on various surfaces, from playground equipment to indoor gym floors. The padded collar and tongue enhance comfort around the ankle, while the secure lace closure with reinforced eyelets provides adjustable fit as children grow. The heel pull tab assists with easy on/off for developing independence. The reflective details enhance visibility in low-light conditions for added safety. Available in kids'' sizes US 11C-3Y (Little Kids) and 3.5Y-7Y (Big Kids) and playful colorways that appeal to children''s preferences while coordinating with school uniforms or casual wear. The lightweight design (7.5oz for size 13C) prevents fatigue during all-day wear. The durable construction withstands the rigors of active children, while the iconic design introduces young wearers to authentic athletic heritage. With its combination of protective cushioning, comfortable fit, and eye-catching style, these versatile sneakers support active kids throughout their busy days.'
WHERE product_name = 'Nike Kids Air Max';

UPDATE products
SET description = 'The Nike Kids Dri-FIT Set provides coordinated performance wear designed specifically for young athletes'' comfort and mobility. The set includes a moisture-wicking Dri-FIT t-shirt that moves sweat away from the skin to the fabric surface where it evaporates quickly, helping kids stay dry and comfortable during active play. The matching shorts feature an elastic waistband with internal drawcord for adjustable, secure fit that accommodates growth spurts. The lightweight polyester fabric (100% recycled polyester) offers environmental consciousness without compromising on the durability needed for children''s active lifestyles. The t-shirt''s raglan sleeves allow unrestricted arm movement for various sports and playground activities, while the shorts'' side vents enhance mobility during running and jumping. The reflective Nike Swoosh logo adds visibility in low-light conditions for added safety. The flat seam construction reduces potential irritation against sensitive skin during movement. Available in kids'' sizes 4-16 and coordinated color combinations (black/white, navy/royal, pink/purple) that appeal to children''s preferences while meeting team sport or physical education requirements. The anti-odor technology helps keep the garments fresher during extended wear. The machine-washable fabric maintains its shape, color, and performance properties even after repeated washing, simplifying care for busy parents. With its combination of performance features, comfortable design, and practical durability, this coordinated set provides functional everyday wear for active kids throughout the seasons.'
WHERE product_name = 'Nike Kids Dri-FIT Set';

-- Watches (Category ID: 20)
UPDATE products
SET description = 'The Apple Watch Ultra 2 represents the most rugged and capable Apple Watch, designed specifically for exploration, adventure, and endurance. The aerospace-grade titanium case provides exceptional durability while remaining surprisingly lightweight, with a distinctive flat sapphire crystal front that offers edge-to-edge visibility and superior scratch resistance. The innovative Action button allows instant access to a preferred function like Workout, Compass Waypoints, Backtrack, or the precision dual-frequency GPS for accurate positioning even in challenging environments. The digital crown with tactile feedback enables precise control even with gloves. The significantly increased battery life provides up to 36 hours during normal use and up to 72 hours in low power mode, with fast charging capability. The specialized watch faces like Wayfinder include a night mode that turns red for better vision preservation in darkness. The three-microphone array with beamforming and wind noise mitigation ensures clear calls even in challenging conditions. The powerful dual speakers include an emergency siren audible up to 600 feet away. The customizable bands include Trail Loop for light weight and thin design, Alpine Loop for secure fit during rugged activities, and Ocean Band for extreme water sports. The comprehensive health features include ECG app, blood oxygen measurement, temperature sensing, and advanced sleep tracking. The water resistance to 100 meters with recreational diving capability to 40 meters (EN13319 certification) supports diverse water activities. With its combination of extreme durability, extended battery life, and specialized outdoor features, this premium smartwatch empowers adventurers to push their boundaries with confidence and connectivity.'
WHERE product_name = 'Apple Watch Ultra 2';

UPDATE products
SET description = 'The Samsung Galaxy Watch6 represents advanced health monitoring combined with versatile smart features in an elegant, customizable design. The BioActive Sensor provides comprehensive health insights, with advanced heart rate monitoring, ECG capability, blood pressure monitoring, and Body Composition measurement that analyzes lean muscle, fat percentage, body water, and more. The enhanced sleep coaching analyzes sleep patterns including REM, deep, and light stages, providing personalized insights and recommendations for better rest. The automatic workout detection recognizes activities like running, swimming, or cycling, with fitness routines offering real-time metrics, personalized heart rate zones, and form analysis for improved performance. The 1.47-inch Super AMOLED display (1.31-inch on smaller model) features enhanced brightness and sapphire crystal glass for superior durability and visibility in various lighting conditions. The slim, modern design with customizable watch faces and bands allows personalization for different occasions and styles. The comprehensive smart features include Samsung Wallet for payments, SmartThings integration for home control, Google apps support, message notifications, and music playback control. The enhanced battery life provides up to 40 hours of typical usage, with a new fast charging system that delivers 45% charge in just 30 minutes. The advanced water resistance (5ATM + IP68) ensures durability during swimming and other water activities. Available in 40mm and 44mm sizes with Bluetooth or LTE connectivity options, this versatile smartwatch seamlessly connects with Galaxy smartphones for an integrated ecosystem experience. With its combination of comprehensive health insights, intelligent fitness guidance, and practical smart features, this advanced wearable provides valuable support for balanced, connected lifestyles.'
WHERE product_name = 'Samsung Galaxy Watch6';

UPDATE products
SET description = 'The Sony Wena 3 represents an innovative approach to smartwatches, combining traditional timepiece aesthetics with modern connected features through a unique design concept. The distinctive approach separates the smart functions into the band rather than the watch face, allowing users to attach their preferred traditional watch head to the Wena smart strap. The stainless steel band features a 1.4-inch touchscreen OLED display integrated into the clasp area, providing notifications, fitness tracking, and music control without compromising the classic watch appearance. The premium materials include 316L stainless steel with optional silicone sport band alternative, blending seamlessly with heritage timepieces. The health monitoring includes heart rate tracking, stress measurement, VO2 max estimation, and sleep analysis, while fitness functions track steps, distance, and calories with automatic activity recognition. The smart features include smartphone notifications, music control, Suica FeliCa payments in Japan, and Alexa voice assistant compatibility. The 7-day battery life for basic functions (1 day with all features activated) provides practical everyday use, with convenient wireless charging. The 5ATM water resistance ensures durability during swimming and water activities. The reversible design accommodates both left and right-handed wearers, while size adjustments allow custom fitting without specialist tools. The companion Wena app provides detailed health insights and customization options. Available in silver and black finishes, this hybrid smartwatch solution offers a unique compromise for those who appreciate traditional horology but desire modern smart features without compromising on either aspect.'
WHERE product_name = 'Sony Wena 3';

-- Bags & Backpacks (Category ID: 22)
UPDATE products
SET description = 'The Adidas Linear Backpack combines essential functionality with iconic athletic styling for versatile everyday use. The spacious main compartment with two-way zip closure provides organized storage for books, clothing, and daily essentials. The dedicated laptop sleeve (fits up to 15.6") with padding offers protection for electronic devices during transport. The water-resistant base adds durability and protection for contents in damp conditions. The front zippered pocket with organization panel provides quick access to smaller items like keys, phone, and wallet. The two side mesh pockets accommodate water bottles or other items requiring external access. The padded, adjustable shoulder straps with ergonomic design ensure comfortable weight distribution, even when carrying heavier loads. The padded back panel enhances comfort while providing structure to the bag. The top haul handle offers alternative carrying option for quick transport. The premium polyester construction (100% recycled polyester) provides environmental consciousness without compromising on durability. The iconic Adidas Linear logo and three-stripe design elements create instantly recognizable athletic styling. The strategic reinforcement at stress points ensures long-term durability through daily use. Available in versatile colorways (black, navy, gray) that complement diverse wardrobes and resist showing dirt. The 25L capacity provides sufficient space for school, gym, or casual travel needs without excessive bulk. The reflective elements enhance visibility in low-light conditions for added safety. With its combination of practical organization, comfortable carrying, and classic athletic styling, this versatile backpack supports active lifestyles with reliable functionality.'
WHERE product_name = 'Adidas Linear Backpack';

-- HEALTH & BEAUTY PRODUCTS

-- Cosmetics (Category ID: 23)
UPDATE products
SET description = 'The L''Oréal Paris True Match liquid foundation revolutionizes complexion perfection with its innovative formula featuring hyaluronic acid for hydration and micro-minerals for natural luminosity. The unprecedented shade range includes 45 carefully calibrated options organized by undertone (cool, neutral, warm), making it easier to find your exact match for imperceptible coverage. The medium-buildable formula offers customizable coverage from natural to full while maintaining a lightweight, breathable feel on the skin. The natural finish strikes the perfect balance between radiant and matte, mimicking the dimensional qualities of healthy skin. The foundation is formulated without pore-clogging ingredients (non-comedogenic) and tested under dermatological supervision for safety on sensitive skin. The precise applicator allows controlled dispensing to minimize waste. The innovative formula improves skin quality over time, with 77% of users reporting more even skin tone after 3 weeks of consistent use. The extensive shade development process included collaboration with makeup artists and diversity consultants to ensure inclusive representation across the spectrum of human skin tones. The blendable texture allows application with fingers, sponge, or brush according to preference, with quick setting to a transfer-resistant finish. The formula provides hydration for up to 24 hours while maintaining color integrity without oxidizing. The glass bottle with pump mechanism maintains formula freshness and provides convenient dispensing without mess. With its combination of precise shade matching, skincare benefits, and versatile performance, this foundation has earned its status as a global bestseller with one sold every second worldwide.'
WHERE product_name = 'L''Oréal Paris True Match';

-- Skincare (Category ID: 24)
UPDATE products
SET description = 'The Nivea Creme represents a century of skincare heritage, with its original formula virtually unchanged since 1911. The iconic blue tin contains a rich, protective moisturizer that has earned trust across generations and cultures. The concentrated formula with Eucerit® (the first water-in-oil emulsifier) creates an effective moisture barrier that protects skin from environmental stressors and prevents dehydration. The versatile application makes this a true head-to-toe product, equally effective for facial hydration, body moisturizing, hand treatment, lip conditioning, and even taming frizzy hair ends. The preservative-free formula relies on its unique composition for stability, maintaining efficacy without artificial preservatives. The signature fragrance combines subtle notes of rose, lily of the valley, and lavender with warm hints of amber and vanilla, creating the distinctive scent that has become synonymous with the brand. The economical formulation provides exceptional value, with a small amount effectively treating large areas. The rich texture absorbs completely with massage, leaving no greasy residue despite its intense hydrating properties. The simple, proven ingredients have demonstrated safety across diverse skin types, ages, and conditions for over a century. The product undergoes rigorous dermatological testing to ensure continued gentleness and effectiveness. The iconic packaging maintains product integrity while providing easy access and distinctive shelf presence. Available in multiple sizes from pocket tins to family jars, this skincare staple accommodates various usage needs and budgets. With its combination of proven efficacy, versatile applications, and nostalgic significance, this classic moisturizer continues to maintain relevance in an ever-changing skincare landscape.'
WHERE product_name = 'Nivea Creme';

-- Now add product images for some products
-- Individual INSERT statements for Samsung Galaxy S23 Ultra images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (1, 'https://i5.walmartimages.com/seo/Samsung-Galaxy-S23-Ultra-5G-SM-S918U1-256GB-Green-US-Model-Factory-Unlocked-Cell-Phone-Excellent-Condition_a8f43ce2-81d4-436a-848c-7f6cbd3ac7d3.41aeda0062a9e454ed998a3843e501ee.jpeg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (1, 'https://m.media-amazon.com/images/I/51Vhx0XakeL.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (1, 'https://m.media-amazon.com/images/I/51MpKU9XowL._AC_UF894,1000_QL80_.jpg', FALSE, NOW());

-- Individual INSERT statements for iPhone 15 Pro Max images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (2, 'https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6525/6525491_sd.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (2, 'https://www.apple.com/newsroom/images/2023/09/apple-unveils-iphone-15-pro-and-iphone-15-pro-max/tile/Apple-iPhone-15-Pro-lineup-hero-230912.jpg.news_app_ed.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (2, 'https://m.media-amazon.com/images/I/81UKVHM77GL.jpg', FALSE, NOW());

-- Individual INSERT statements for Xiaomi 14 Pro images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (3, 'https://i.ebayimg.com/images/g/kOkAAOSw89dlPHAd/s-l1200.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (3, 'https://www.giztop.com/media/catalog/product/cache/97cc1143d2e20f2b0c8ea91aaa12053c/p/m/pms_1698307433.52595447_1.png', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (3, 'https://m.media-amazon.com/images/I/51hOisZjbeL._AC_UF894,1000_QL80_.jpg', FALSE, NOW());

-- Individual INSERT statements for Xiaomi Redmi Note 13 Pro images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (4, 'https://m.media-amazon.com/images/I/51pk5PzpzZL._AC_UF894,1000_QL80_.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (4, 'https://m.media-amazon.com/images/I/61vFWIksgcL.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (4, 'https://m.media-amazon.com/images/I/71ZjanVe7oL.jpg', FALSE, NOW());

-- Individual INSERT statements for LG Velvet images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (5, 'https://m.media-amazon.com/images/I/61375QgQ0oL._AC_UF894,1000_QL80_.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (5, 'https://m.media-amazon.com/images/I/61BskzFz6QL._AC_UF894,1000_QL80_.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (5, 'https://upload.wikimedia.org/wikipedia/commons/d/d4/LG_Velvet_Aurora_Green_version.jpg', FALSE, NOW());

-- Individual INSERT statements for iPad Pro 12.9 (2023) images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (6, 'https://cdsassets.apple.com/live/SZLF0YNV/images/sp/111841_ipad-pro-4gen-mainimage.png', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (6, 'https://www.apple.com/newsroom/images/product/ipad/lifestyle/Apple-iPad-Pro-Magic-Keyboard-M2-hero-2up-221018_big.jpg.large.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (6, 'https://i5.walmartimages.com/asr/5ca19413-6d77-4522-9cda-b5e534e78e69.16903f821e9f5d0bf0fca2937ef08aff.jpeg?odnHeight=768&odnWidth=768&odnBg=FFFFFF', FALSE, NOW());

-- Individual INSERT statements for Samsung Galaxy Tab S9 Ultra images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (7, 'https://m.media-amazon.com/images/I/617KdvXFrEL.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (7, 'https://pisces.bbystatic.com/image2/BestBuy_US/images/products/a37b0e55-056c-41ad-9dd7-b46e464e150d.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (7, 'https://image-us.samsung.com/us/tablets/galaxy-tab-s9/products/tab-s9/gallery-images/graphite/new/1.jpg', FALSE, NOW());

-- Individual INSERT statements for Xiaomi Pad 6 images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (8, 'https://m.media-amazon.com/images/I/61uZ3HMyy0L.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (8, 'https://m.media-amazon.com/images/I/61oovkHjQiL.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (8, 'https://i.ebayimg.com/images/g/SHMAAOSwVR1mYjCo/s-l1200.jpg', FALSE, NOW());

-- Individual INSERT statements for MacBook Pro 16" M3 Max images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (9, 'https://cdn.arstechnica.net/wp-content/uploads/2023/11/IMG_1415.jpeg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (9, 'https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/refurb-mbp16-m3-max-pro-spaceblack-202402?wid=1200&hei=630&fmt=jpeg&qlt=95&.v=1709175741917', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (9, 'https://i.pcmag.com/imagery/reviews/05r7grG5jUF6QJXZlqKnmiH-1..v1699031377.jpg', FALSE, NOW());

-- Individual INSERT statements for MacBook Air 13" M3 images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (10, 'https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/refurb-mba13-m3-midnight-202405?wid=4000&hei=3074&fmt=jpeg&qlt=90&.v=1715624946953', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (10, 'https://cdn.mos.cms.futurecdn.net/pHBy4DzouBqLoWy7JuCtDU.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (10, 'https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/refurb-mba13-m3-silver-202405', FALSE, NOW());

-- Individual INSERT statements for LG Gram 17 images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (11, 'https://m.media-amazon.com/images/I/81inFqt1MiL.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (11, 'https://m.media-amazon.com/images/I/71eLsCpIkeL._AC_UF894,1000_QL80_.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (11, 'https://www.lg.com/us/images/business/md08004501/gallery/D-02.jpg', FALSE, NOW());

-- Individual INSERT statements for LG UltraGear Gaming Laptop images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (12, 'https://www.lgnewsroom.com/wp-content/uploads/2021/12/LG-UltraGear-Gaming_00FI.png', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (12, 'https://www.zdnet.com/a/img/resize/848fe1160d18c4349495fbcd0385fe7f768ef4f8/2021/12/21/193aab0a-351d-43a0-8c87-c296c6fb9496/lg-ultragear-17g90q-gaming-laptop-notebook-ces-2022.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (12, 'https://www.cnet.com/a/img/resize/269083a89d81addba9c3041a372640b2b3bfe88e/hub/2021/12/20/eced808f-8eac-4d86-8da1-49c366ecb75c/lg-ultragear-gaming-00.jpg', FALSE, NOW());

-- Individual INSERT statements for Samsung Galaxy Book4 Pro images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (13, 'https://m.media-amazon.com/images/I/6131ZgIFn1L.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (13, 'https://image-us.samsung.com/SamsungUS/home/computing/galaxy-books/gb4-series/gallery-images/1_Hero_KV.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (13, 'https://m.media-amazon.com/images/I/71ysHVMH4FL._AC_UF894,1000_QL80_.jpg', FALSE, NOW());

-- Individual INSERT statements for Samsung Galaxy Book4 Ultra images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (14, 'https://image-us.samsung.com/SamsungUS/home/computing/galaxy-books/gb4-series/gallery-images/1_Hero_KV.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (14, 'https://www.pcworld.com/wp-content/uploads/2025/04/primary-alt-non-background-blur.jpg?quality=50&strip=all', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (14, 'https://images.samsung.com/is/image/samsung/p6pim/uk/feature/164998442/uk-feature-galaxy-book4-ultra-16-inch-np960-540163831?$FB_TYPE_I_JPG$', FALSE, NOW());

-- Individual INSERT statements for AirPods Pro 2 images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (17, 'https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/airpods-pro-2-202409-gallery-1', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (17, 'https://m.media-amazon.com/images/I/61SUj2aKoEL._AC_UF894,1000_QL80_.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (17, 'https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/airpods-pro-2-202409-thumb-5', FALSE, NOW());

-- Individual INSERT statements for AirPods Max images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (18, 'https://m.media-amazon.com/images/I/81yA8CLEIIL.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (18, 'https://m.media-amazon.com/images/I/81thV7SoLZL._AC_UF894,1000_QL80_.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (18, 'https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/og-airpods-max-202409?wid=1200&hei=630&fmt=jpeg&qlt=95&.v=1724144125817', FALSE, NOW());

-- Individual INSERT statements for Sony WH-1000XM5 images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (19, 'https://m.media-amazon.com/images/I/51aXvjzcukL._AC_UF894,1000_QL80_.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (19, 'https://d1ncau8tqf99kp.cloudfront.net/converted/103364_original_local_1200x1050_v3_converted.webp', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (19, 'https://m.media-amazon.com/images/I/61juFYGuTPL.jpg', FALSE, NOW());

-- Individual INSERT statements for Sony WF-1000XM5 images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (20, 'https://m.media-amazon.com/images/I/61GJAFdM9pL._AC_UF894,1000_QL80_.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (20, 'https://m.media-amazon.com/images/I/61qmsGnacvL.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (20, 'http://www.worldwidestereo.com/cdn/shop/files/179968_WWS1.jpg?v=1704320680', FALSE, NOW());

-- Individual INSERT statements for Samsung Neo QLED 8K TV images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (23, 'https://image-us.samsung.com/SamsungUS/home/ca-assets-folder/40463/QN85QN900CFXZA-S.COM_Version_1_V01.jpg?$product-details-jpg$', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (23, 'https://www.nfm.com/dw/image/v2/BDFM_PRD/on/demandware.static/-/Sites-nfm-master-catalog/default/dw2dc953b6/images/066/82/66825670-2.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (23, 'https://m.media-amazon.com/images/I/818u1IheEvL.jpg', FALSE, NOW());

-- Individual INSERT statements for Samsung The Frame TV images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (24, 'https://image-us.samsung.com/SamsungUS/home/television-home-theater/tvs/qled-4k-tvs/06172024/TheFrame_LSI_08_re_pj_1600x1200.jpg?$product-details-jpg$', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (24, 'https://m.media-amazon.com/images/I/616R4YOdBNL._AC_UF1000,1000_QL80_.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (24, 'https://media.cnn.com/api/v1/images/stellar/prod/220607112547-samsung-frame-2022-lead.jpg?c=16x9&q=h_833,w_1480,c_fill', FALSE, NOW());

-- Individual INSERT statements for Sony Bravia XR A95L images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (25, 'https://m.media-amazon.com/images/I/81G+fnlLWcL.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (25, 'https://i.rtings.com/assets/products/s9nyu6pB/sony-a95l-oled/design-medium.jpg?format=auto', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (25, 'https://d1ncau8tqf99kp.cloudfront.net/PDP/TVandVIDEO/Televisions/A95L/desktop/3-d-item5.jpg', FALSE, NOW());

-- Individual INSERT statements for Sony HT-A7000 images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (26, 'https://www.sony.com/image/c530704949a4be74ca0600fbadd51467?fmt=pjpeg&wid=1014&hei=396&bgcolor=F1F5F9&bgc=F1F5F9', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (26, 'https://m.media-amazon.com/images/I/51gGhig13QL._AC_UF1000,1000_QL80_.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (26, 'https://i.rtings.com/assets/products/6WRg2OaU/sony-ht-a7000/design-medium.jpg?format=auto', FALSE, NOW());

-- Individual INSERT statements for LG C3 OLED TV images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (27, 'https://www.lg.com/us/images/tvs/md08003931/gallery/D-1.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (27, 'https://i.rtings.com/assets/products/mYkQ7bho/lg-c3-oled/design-medium.jpg?format=auto', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (27, 'https://m.media-amazon.com/images/I/71ReKg-3YrL.jpg', FALSE, NOW());

-- Individual INSERT statements for LG OLED Flex images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (28, 'https://www.lg.com/us/images/tvs/md08003300/450.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (28, 'https://www.lg.com/content/dam/channel/wcms/ca_en/images/lifestyle-screens/42lx3qpua_acc_enci_ca_en_c/gallery/DZ-03.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (28, 'https://media.us.lg.com/m/166760c524e7a34e/webimage-TV-OLED-Flex_Flexible-Display_features_900x600.jpg', FALSE, NOW());

-- Individual INSERT statements for Apple Watch Series 9 images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (29, 'https://m.media-amazon.com/images/I/71aXGgNCE9L._AC_UF894,1000_QL80_.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (29, 'https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/refurb-45-cell-alum-pink-sport-band-light-pink-s9', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (29, 'https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/refurb-45-cell-alum-midnight-sport-band-midnight-s9', FALSE, NOW());

-- Individual INSERT statements for Apple HomePod mini images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (30, 'https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/homepod-mini-og-202110?wid=1200&hei=630&fmt=jpeg&qlt=95&.v=1719505542711', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (30, 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/homepod-mini-select-midnight-202407_FV1_FMT_WHH?wid=1214&hei=566&fmt=jpeg&qlt=90&.v=1719853980357', FALSE, NOW());

-- Individual INSERT statements for Apple HomePod mini images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (30, 'https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/homepod-mini-og-202110?wid=1200&hei=630&fmt=jpeg&qlt=95&.v=1719505542711', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (30, 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/homepod-mini-select-midnight-202407_FV1_FMT_WHH?wid=1214&hei=566&fmt=jpeg&qlt=90&.v=1719853980357', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (30, 'https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/homepod-mini-select-white-202110_FV1_FMT_WHH?wid=1214&hei=566&fmt=jpeg', FALSE, NOW());

-- Individual INSERT statements for Samsung Galaxy Watch6 Classic images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (31, 'https://image-us.samsung.com/us/watches/galaxy-watch6-classic/black/R965-black/1.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (31, 'https://image-us.samsung.com/us/watches/galaxy-watch6-classic/silver/R965-silver/1.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (31, 'https://m.media-amazon.com/images/I/51zBhMSh0uL._AC_UF894,1000_QL80_.jpg', FALSE, NOW());

-- Individual INSERT statements for Samsung SmartThings Hub images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (32, 'https://m.media-amazon.com/images/I/614d2lQP0hL.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (32, 'https://image-us.samsung.com/SamsungUS/pim/migration/smart-home/smartthings/hubs/f-h-eth-001/Pdpdefault-f-h-eth-001-600x600-C1-052016.jpg?$product-details-jpg$', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (32, 'https://image-us.samsung.com/SamsungUS/pim/migration/feature/part19/simple-setup_2_F-H-ETH-001.jpg?$feature-benefit-jpg$', FALSE, NOW());

-- Individual INSERT statements for Electrolux UltimateTaste 900 images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (33, 'https://www.electrolux.in/globalassets/electrolux-india/kitchen/refrigerators/eqe6879a-b/eqe6879a-b-fr-cl-1500x1500.png?width=1200&height=630', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (33, 'https://www.electrolux.in/globalassets/electrolux-india/kitchen/ovens/koaas31x/koaas31x-fr-cl-1500x1500.png?width=375', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (33, 'https://www.electrolux.com.au/resourceimageelectrolux/Public/Image2/product/112039/52348.png?width=375', FALSE, NOW());

-- Individual INSERT statements for Electrolux MaxiMix Blender images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (34, 'https://www.nettoshop.ch/medias/IP092734.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (34, 'https://www.cnet.com/a/img/resize/e455dc2446f09c872627dd14be71d9f8c1336691/hub/2016/03/17/5eb1bf8c-efad-49de-9f97-aa21e4fd6c4c/electrolux-masterpiece-blender-1.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (34, 'https://www.nettoshop.ch/medias/IP092732.jpg', FALSE, NOW());

-- Individual INSERT statements for Lock&Lock Air Fryer images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (35, 'https://www.locknlock.com/eng/image/story/lounge/lg/gm/mqkjiqls/html/lounge-05-sub-image-01.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (35, 'https://www.locknlock.com/eng/image/product/2021/06/24/46691802lkcg.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (35, 'https://custom-images.strikinglycdn.com/res/hrscywv4p/image/upload/c_limit,fl_lossy,h_9000,w_1200,f_auto,q_auto/5269494/335323_475950.jpeg', FALSE, NOW());

-- Individual INSERT statements for Lock&Lock Food Container Set images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (36, 'https://images.thdstatic.com/productImages/f8756b7d-eb58-47bb-8fa8-c113fecc085f/svn/clear-locknlock-food-storage-containers-hpl829sf07-64_1000.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (36, 'https://m.media-amazon.com/images/I/71QRh-pyz7L.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (36, 'https://m.media-amazon.com/images/I/7151L9hpd1L.jpg', FALSE, NOW());

-- Individual INSERT statements for Philips 3200 Series images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (37, 'https://m.media-amazon.com/images/I/51HrtoZ9YVL._AC_UF894,1000_QL80_.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (37, 'https://m.media-amazon.com/images/I/71pfwf847pL._AC_UF894,1000_QL80_.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (37, 'https://images.philips.com/is/image/philipsconsumer/vrs_c738e40824ac0aa137e8e47de8e02f0505ae59e3?$pnglarge$&wid=960', FALSE, NOW());

-- Individual INSERT statements for Philips Airfryer XXL images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (38, 'https://m.media-amazon.com/images/I/5164TNfQi4L.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (38, 'https://m.media-amazon.com/images/I/61kslrXrlhL.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (38, 'https://images.philips.com/is/image/philipsconsumer/vrs_08a35739b2a6b1b928c91373c1c8f1e56d4951fa?wid=700&hei=700&$pnglarge$', FALSE, NOW());

-- Individual INSERT statements for Philips Hand Blender images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (39, 'https://m.media-amazon.com/images/I/61eX6Kb3ZXL.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (39, 'https://images.philips.com/is/image/philipsconsumer/4bd1a4cd5fdb41ce9e3ead2801680842?$pnglarge$&wid=1250', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (39, 'https://m.media-amazon.com/images/I/61uZV9Ysa-L._AC_UF894,1000_QL80_.jpg', FALSE, NOW());

-- Individual INSERT statements for Electrolux UltimateCare 900 images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (40, 'https://www.electrolux.co.id/globalassets/appliances/washer-dryers/eww8023aewa/eww8023aewa-front-1500x1500.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (40, 'https://www.electrolux.co.id/globalassets/appliances/washing-machines/ewf1141r9wb/ewf1141r9wb-fr-cl-1500x1500-min.png', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (40, 'https://i.ytimg.com/vi/j_vSc5T3N_c/maxresdefault.jpg', FALSE, NOW());

-- Individual INSERT statements for Electrolux PerfectCare 800 images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (41, 'https://www.manua.ls/thumbs/products/l/1684576-electrolux-perfectcare-800-ew8h258sc.webp', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (41, 'https://e-catalog.com/jpg/1433193.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (41, 'https://www.electroluxarabia.com/remote.jpg.ashx', FALSE, NOW());

-- Individual INSERT statements for LG InstaView Door-in-Door images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (42, 'https://media.us.lg.com/transform/eee913a73e1440878604ad2700f46ad8/smart-instaview-refrigerators_herobanner_900x600', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (42, 'https://www.lg.com/us/images/RF/features/instaview-ref-update_2020-05-14-m.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (42, 'https://www.lg.com/us/images/refrigerators/md07000074/gallery/medium01.jpg', FALSE, NOW());

-- Individual INSERT statements for LG DUAL Inverter AC images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (43, 'https://images.thdstatic.com/productImages/bb6009df-8015-4c72-a147-d5002e194d09/svn/lg-window-air-conditioners-lw1522ivsm-64_1000.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (43, 'https://www.lg.com/content/dam/channel/wcms/in/images/split-ac/us-q24enxe_anlg_eail_in_c/gallery/US-Q24ENXE-Air-Conditioners-DZ-1.jpeg/_jcr_content/renditions/thum-1600x1062.jpeg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (43, 'https://m.media-amazon.com/images/I/61DMV2X7cZL._AC_UF894,1000_QL80_.jpg', FALSE, NOW());

-- Individual INSERT statements for LG CordZero A9 images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (44, 'https://m.media-amazon.com/images/I/61eb+Kc9J1L._AC_UF894,1000_QL80_.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (44, 'https://i5.walmartimages.com/seo/LG-Cord-Zero-A9-Cordless-Stick-Vacuum-A912PM_e4d9bfc9-ab02-4249-8236-3aa26a872e49.1c3c3f974271d1ad4cb47cf3690b6e84.jpeg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (44, 'https://media.us.lg.com/transform/ecomm-PDPGallery-1100x730/08e9bfb0-3a35-480a-aaae-0bcb2962a29d/md07519192-large10-jpg?io=transform:fill,width:596', FALSE, NOW());

-- Individual INSERT statements for Philips Air Purifier 3000i images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (45, 'https://images.philips.com/is/image/philipsconsumer/3ab8bca96e9c4db88604ad2700f46aa2?wid=700&hei=700&$pnglarge$', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (45, 'https://images.philips.com/is/image/philipsconsumer/2e71d46641e44e6b9ac6ad28012f49fc?wid=700&hei=700&$pnglarge$', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (45, 'https://images.philips.com/is/image/philipsconsumer/44ea5e061fb349719ec1ad36013a0534?$pnglarge$&wid=1250', FALSE, NOW());

-- Individual INSERT statements for Philips Steam Iron images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (46, 'https://images.philips.com/is/image/philipsconsumer/a73145b1b8c54ef9ba6bad140129177e?$pnglarge$&wid=700&hei=700', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (46, 'https://images.philips.com/is/image/philipsconsumer/ab6b5f35c5d748ffbaf8ad1900d8104d?wid=700&hei=700&$pnglarge$', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (46, 'https://images.philips.com/is/image/philipsconsumer/8c4836c65b4b467fb6abad1f011aceba?$pnglarge$&wid=1250', FALSE, NOW());

-- Individual INSERT statements for IKEA BILLY images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (47, 'https://www.ikea.com/us/en/images/products/billy-oxberg-bookcase-w-glass-doors-oak-effect__1415087_pe975110_s5.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (47, 'https://www.ikea.com/us/en/images/products/billy-bookcase-white__1051924_pe845813_s5.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (47, 'https://www.ikea.com/us/en/images/products/billy-oxberg-bookcase-comb-w-panel-glass-doors-brown-walnut-effect__1104792_pe867899_s5.jpg', FALSE, NOW());

-- Individual INSERT statements for IKEA MALM images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (48, 'https://www.ikea.com/us/en/images/products/malm-bed-frame-white__1101527_pe866706_s5.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (48, 'https://www.ikea.com/us/en/images/products/malm-6-drawer-dresser-white-stained-oak-veneer__1154418_pe886020_s5.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (48, 'https://www.ikea.com/us/en/images/products/malm-2-drawer-chest-white__1154585_pe886214_s5.jpg', FALSE, NOW());

-- Individual INSERT statements for IKEA POÄNG images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (49, 'https://www.ikea.com/us/en/images/products/poaeng-armchair-birch-veneer-hillared-dark-blue__0840367_pe629080_s5.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (49, 'https://www.ikea.com/us/en/images/products/poaeng-armchair-birch-veneer-hillared-beige__0497125_pe628952_s5.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (49, 'https://www.ikea.com/us/en/images/products/poaeng-armchair-brown-hillared-anthracite__0837589_pe629093_s5.jpg?f=s', FALSE, NOW());

-- Individual INSERT statements for IKEA KALLAX images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (50, 'https://www.ikea.com/us/en/images/products/kallax-shelf-unit-white__1084790_pe859876_s5.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (50, 'https://www.ikea.com/us/en/images/products/kallax-shelf-unit-white__1102268_pe866887_s5.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (50, 'https://www.ikea.com/us/en/images/products/kallax-shelf-unit-high-gloss-white__1113807_pe871556_s5.jpg?f=s', FALSE, NOW());

-- Individual INSERT statements for IKEA HEMNES images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (51, 'https://www.ikea.com/us/en/images/products/hemnes-8-drawer-dresser-white-stain__1151400_pe886164_s5.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (51, 'https://www.ikea.com/us/en/images/products/hemnes-glass-door-cabinet-with-3-drawers-white-stain-light-brown__1052143_pe845952_s5.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (51, 'https://www.ikea.com/us/en/images/products/hemnes-3-drawer-chest-white-stain__1151406_pe886157_s5.jpg', FALSE, NOW());

-- Individual INSERT statements for Philips Sonicare DiamondClean images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (52, 'https://m.media-amazon.com/images/I/41zaQfZ0QtL.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (52, 'https://m.media-amazon.com/images/I/71CLrfnTDNL._AC_UF1000,1000_QL80_.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (52, 'https://images.philips.com/is/image/philipsconsumer/561916d2d56840e8b397ac5c01283ab2?$pnglarge$&wid=1250', FALSE, NOW());

-- Individual INSERT statements for Electrolux Water Heater images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (53, 'https://home-comfort.com/upload/resize_cache/iblock/2f2/800_800_1/3_4.png', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (53, 'https://www.electrolux.co.id/globalassets/appliances/water-heaters/id/ews30bex-dw1/id-ews30bex-dw1-fr-1500x1500-min.png', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (53, 'https://images.webfronts.com/cache/wvdeuqjexb.jpeg?imgeng=/w_500/h_500/m_letterbox_ffffff_100', FALSE, NOW());

-- Individual INSERT statements for IKEA GODMORGON images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (54, 'https://www.ikea.com/us/en/images/products/godmorgon-bathroom-vanity-with-2-drawers-high-gloss-white__0862095_pe647888_s5.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (54, 'https://m.media-amazon.com/images/I/610U+eKpbRL._AC_UF894,1000_QL80_.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (54, 'https://m.media-amazon.com/images/I/71bK78d+b5L._AC_UF894,1000_QL80_.jpg', FALSE, NOW());

-- Individual INSERT statements for IKEA BROGRUND images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (55, 'https://www.ikea.com/us/en/images/products/brogrund-corner-wall-shelf-unit-stainless-steel__0720001_pe732357_s5.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (55, 'https://www.ikea.com/us/en/images/products/brogrund-touch-top-trash-can-stainless-steel__0733266_pe738908_s5.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (55, 'https://www.ikea.com/us/en/images/products/brogrund-towel-rail-stainless-steel__0863257_pe643861_s5.jpg', FALSE, NOW());

-- Individual INSERT statements for IKEA STOCKHOLM images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (56, 'https://www.ikea.com/us/en/images/products/stockholm-cabinet-with-2-drawers-walnut-veneer__0848506_pe560689_s5.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (56, 'https://www.ikea.com/global/assets/range-categorisation/images/stockholm-collection-11989.jpeg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (56, 'https://www.ikea.com/us/en/images/products/stockholm-sideboard-walnut-veneer__0212204_pe362775_s5.jpg', FALSE, NOW());

-- Individual INSERT statements for IKEA RIBBA images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (57, 'https://m.media-amazon.com/images/I/61eX6Kb3ZXL.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (57, 'https://www.ikea.com/global/assets/range-categorisation/images/ribba-series-16456.jpeg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (57, 'https://m.media-amazon.com/images/I/71zt1nrMBAL.jpg', FALSE, NOW());

-- Individual INSERT statements for IKEA FEJKA images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (58, 'https://www.ikea.com/us/en/images/products/fejka-artificial-potted-plant-indoor-outdoor-weeping-fig__0900701_pe658007_s5.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (58, 'https://www.ikea.com/us/en/images/products/fejka-artificial-potted-plant-indoor-outdoor-hanging__0748917_pe745318_s5.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (58, 'https://www.ikea.com/us/en/images/products/fejka-artificial-potted-plant-with-pot-indoor-outdoor-succulent__0980123_ph175746_s5.jpg', FALSE, NOW());

-- Individual INSERT statements for IKEA SYMFONISK images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (59, 'https://www.ikea.com/us/en/images/products/symfonisk-picture-frame-w-sonos-wi-fi-speaker-black-smart__1012832_pe829036_s5.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (59, 'https://www.ikea.com/us/en/images/products/symfonisk-sonos-speaker-lamp-base-with-wifi-black-smart__0993356_pe820509_s5.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (59, 'https://www.ikea.com/us/en/images/products/symfonisk-sonos-wifi-bookshelf-speaker-black-smart-gen-2__1025506_pe834047_s5.jpg', FALSE, NOW());

-- Individual INSERT statements for Adidas Ultraboost 23 images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (60, 'https://images.footlocker.com/is/image/EBFL2/GY9353_01?wid=500&hei=500&fmt=png-alpha', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (60, 'https://shop.asnailspace.net/images/1575/9_90_1682732349159.jpeg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (60, 'https://images.footlocker.com/is/image/EBFL2/HQ6340_a1?wid=500&hei=500&fmt=png-alpha', FALSE, NOW());

-- Individual INSERT statements for Adidas Tiro Track Jacket images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (61, 'https://m.media-amazon.com/images/I/71DHBP37xQL._AC_UY1000_.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (61, 'https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/1f87d59aa15f4120abe765d904d0d5e2_9366/Tiro_24_Training_Jacket_Black_IJ9959_21_model.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (61, 'https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/ff09d2c1f1e34423b5627fa8837abaeb_9366/Tiro_Material_Mix_Track_Jacket_Green_IS1503_21_model.jpg', FALSE, NOW());

-- Individual INSERT statements for Nike Air Force 1 images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (62, 'https://static.nike.com/a/images/t_PDP_936_v1/f_auto,q_auto:eco/b7d9211c-26e7-431a-ac24-b0540fb3c00f/AIR+FORCE+1+%2707.png', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (62, 'https://m.media-amazon.com/images/I/813xBjiwt3L._AC_UY300_.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (62, 'https://cdn.runrepeat.com/storage/gallery/product_primary/25004/nike-air-force-1-07-lab-test-and-review-21532702-main.jpg', FALSE, NOW());

-- Individual INSERT statements for Nike Dri-FIT T-Shirt images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (63, 'https://static.nike.com/a/images/t_PDP_936_v1/f_auto,q_auto:eco/79a57836-c867-4714-ada0-626a386115a2/M+NP+DF+SLIM+TOP+SS.png', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (63, 'https://static.nike.com/a/images/t_PDP_936_v1/f_auto,q_auto:eco/kxjgqmbim9zxricso57p/M+NK+DF+TEE+DFC+CREW+SOLID.png', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (63, 'https://m.media-amazon.com/images/I/51LJdkHyJpL._AC_SL1000_.jpg', FALSE, NOW());

-- Individual INSERT statements for Zara Slim Fit Blazer images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (64, 'https://static.zara.net/assets/public/f9ff/0ca8/8e054861bb74/0e3907798291/09722605800-p/09722605800-p.jpg?ts=1738666744225', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (64, 'https://static.zara.net/assets/public/6e8b/57ec/fced4e67a5b7/adb92a46016a/09189100802-p/09189100802-p.jpg?ts=1743008247345&w=744&f=auto', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (64, 'https://static.zara.net/assets/public/1b11/ea30/e4054b8aa01d/7c09630ca60b/01564300401-a1/01564300401-a1.jpg?ts=1738768380630&w=352&f=auto', FALSE, NOW());

-- Individual INSERT statements for Zara Chino Trousers images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (65, 'https://static.zara.net/assets/public/1efe/8c05/a708472bb528/4ca0751617de/01934405710-p/01934405710-p.jpg?ts=1724664768694', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (65, 'https://static.zara.net/assets/public/d380/5b62/49dc4db2bea0/18b21fcd57e4/06786405922-a2/06786405922-a2.jpg?ts=1720773745490', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (65, 'https://static.zara.net/assets/public/4619/aebc/4cfd4d43b103/baa249f7f934/06861441802-a1/06861441802-a1.jpg?ts=1727349036352&w=352&f=auto', FALSE, NOW());

-- Individual INSERT statements for Zara Oxford Shirt images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (66, 'https://static.zara.net/assets/public/4a53/e114/282b47adaff9/fa4cc65917c7/08741049046-060-p/08741049046-060-p.jpg?ts=1742918802204', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (66, 'https://static.zara.net/assets/public/bb37/4f8f/97bd4310817d/e223c57df646/02190772406-p/02190772406-p.jpg?ts=1739898181427', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (66, 'https://static.zara.net/assets/public/e62f/83fe/873a4a92917f/0bc9715ed471/05588402105-p/05588402105-p.jpg?ts=1738927688763&w=744&f=auto', FALSE, NOW());

-- Individual INSERT statements for Adidas Cloudfoam Pure images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (67, 'https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/e8f8610a3337465a9a6bf90b14dd2833_9366/Cloudfoam_Pure_Shoes_White_IF3393_01_standard.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (67, 'https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/7d8ef5f822e24c01bf067073bba6518c_9366/Cloudfoam_Pure_Shoes_Black_IG2530_01_standard.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (67, 'https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/538419fc409a4b9495af4d438048bc2a_9366/Cloudfoam_Pure_Shoes_White_II0043_01_standard.jpg', FALSE, NOW());

-- Individual INSERT statements for Adidas Essentials Hoodie images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (68, 'https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/f4d908c6409a45f7888819b03e132a4d_9366/Trefoil_Essentials_Hoodie_Black_IY4930_21_model.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (68, 'https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/0f7730f4720e4395910962d5a807b9f1_9366/Essentials_Oversized_Fleece_Hoodie_White_IY7347_21_model.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (68, 'https://assets.adidas.com/images/w_600,f_auto,q_auto/95e0cf125f5e44248a5daf4200f81ed2_9366/Trefoil_Essentials_Hoodie_Black_IA4898_01_laydown.jpg', FALSE, NOW());

-- Individual INSERT statements for Nike Air Max 270 images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (69, 'https://static.nike.com/a/images/t_PDP_936_v1/f_auto,q_auto:eco/awjogtdnqxniqqk0wpgf/AIR+MAX+270.png', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (69, 'https://static.nike.com/a/images/t_PDP_936_v1/f_auto,q_auto:eco/1b8e8e0e-acdd-429a-986c-24ccb2254d05/W+AIR+MAX+270.png', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (69, 'https://static.nike.com/a/images/t_PDP_936_v1/f_auto,q_auto:eco/7992669b-d580-458f-87b9-1b7e3497800e/W+AIR+MAX+270.png', FALSE, NOW());

-- Individual INSERT statements for Nike Sportswear Leggings images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (70, 'https://static.nike.com/a/images/t_PDP_936_v1/f_auto,q_auto:eco/2185784f-4b29-4bd3-8d18-2089ad24f887/G+NSW+CLSSC+HR+TGHT+LBR.png', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (70, 'https://static.nike.com/a/images/t_PDP_936_v1/f_auto,q_auto:eco/6d040bc9-dbc9-4924-971d-500850f2ee0c/W+NSW+NK+CLSC+GX+HR+TIGHT+FTRA.png', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (70, 'https://m.media-amazon.com/images/I/615HseHyNvL._AC_UY1000_.jpg', FALSE, NOW());

-- Individual INSERT statements for Zara Pleated Midi Skirt images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (71, 'https://static.zara.net/assets/public/e633/d596/b0384dcab43f/e9cdbef1c857/03643251401-p/03643251401-p.jpg?ts=1723645468560&w=744&f=auto', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (71, 'https://static.zara.net/assets/public/1c29/d2c7/ac0a4fd0b433/b45c24799637/07223021427-p/07223021427-p.jpg?ts=1734515943467&w=744&f=auto', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (71, 'https://static.zara.net/assets/public/69bd/1d16/ce13456695f2/cd91fdcb5ceb/09632253407-017-p/09632253407-017-p.jpg?ts=1730796932358', FALSE, NOW());

-- Individual INSERT statements for Zara Oversized Blazer images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (72, 'https://static.zara.net/assets/public/b220/2de4/e2004f618817/f4963e909489/02753222803-p/02753222803-p.jpg?ts=1723621055879', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (72, 'https://static.zara.net/assets/public/d492/ab04/e72042d59cb0/621e992c3726/02233636700-p/02233636700-p.jpg?ts=1736418222413', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (72, 'https://static.zara.net/assets/public/a38d/494c/16e642f1a0e0/7a39439dc771/02753222505-p/02753222505-p.jpg?ts=1733316186832&w=352&f=auto', FALSE, NOW());

-- Individual INSERT statements for Zara High Waist Jeans images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (73, 'https://static.zara.net/assets/public/e633/d596/b0384dcab43f/e9cdbef1c857/03643251401-p/03643251401-p.jpg?ts=1723645468560&w=744&f=auto', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (73, 'https://static.zara.net/assets/public/1c29/d2c7/ac0a4fd0b433/b45c24799637/07223021427-p/07223021427-p.jpg?ts=1734515943467&w=744&f=auto', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (73, 'https://static.zara.net/assets/public/69bd/1d16/ce13456695f2/cd91fdcb5ceb/09632253407-017-p/09632253407-017-p.jpg?ts=1730796932358', FALSE, NOW());

-- Individual INSERT statements for Adidas Kids Superstar images
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (74, 'https://www.shooos.com/media/catalog/product/cache/2/image/1350x778/9df78eab33525d08d6e5fb8d27136e95/a/d/adidas-superstar-cf-i-kids-ef48426.jpg', TRUE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (74, 'https://m.media-amazon.com/images/I/51h+n6TpumL._AC_UY900_.jpg', FALSE, NOW());

INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (74, 'https://www.juniorcouture.com/dw/image/v2/BGHV_PRD/on/demandware.static/-/Sites-master-catalog/default/dwf9f75629/images/ADI-IF3577/ADI-IF3577-WHT-1.jpg?sw=1500&sh=1500', FALSE, NOW());

-- Individual INSERT statements for remaining products (75-92)
-- Adidas Kids Tracksuit
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (75, 'https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/0063ca74e9b04e4ea3ab8ebf280fa4d5_9366/Adicolor_SST_Track_Suit_Kids_Black_IX7624_21_model.jpg', TRUE, NOW());

-- Nike Kids Air Max
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (76, 'https://static.nike.com/a/images/t_PDP_936_v1/f_auto,q_auto:eco/fb3ba7ef-fa8c-4430-87f4-e820e5b647d3/AIR+MAX+1+%28GS%29.png', TRUE, NOW());

-- Nike Kids Dri-FIT Set
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (77, 'https://m.media-amazon.com/images/I/51ucQgFCdDS._AC_UY1000_.jpg', TRUE, NOW());

-- Apple Watch Ultra 2
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (78, 'https://i5.walmartimages.com/seo/Apple-Watch-Ultra-2-GPS-Cellular-49mm-Black-Titanium-Case-with-Dark-Green-Alpine-Loop-Large-MX4T3LW-A-2024_f8fd348e-e6cd-453b-b35f-4d1a6ab6ef90.285c49c630c0e35e2d5090b6fd9d27f0.jpeg', TRUE, NOW());

-- Samsung Galaxy Watch6
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (79, 'https://images.samsung.com/hk_en/galaxy-watch6/feature/galaxy-watch6-kv-pc.jpg', TRUE, NOW());

-- Sony Wena 3
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (80, 's3files.core77.com/blog/images/1305210_81_116616_MPvBXFkri.jpg', TRUE, NOW());

-- Adidas Linear Backpack
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (81, 'https://xcdn.next.co.uk/common/items/default/default/itemimages/3_4Ratio/product/lge/D30491s.jpg', TRUE, NOW());

-- L'Oréal Paris True Match
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (83, 'https://m.media-amazon.com/images/I/61XEnxJ8HBL._AC_UL400_.jpg', TRUE, NOW());

-- Nivea Creme
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (86, 'https://m.media-amazon.com/images/I/61JJcPvH8DL._SL1000_.jpg', TRUE, NOW());

-- Philips Lumea IPL
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES (89, 'https://m.media-amazon.com/images/I/61HFxC6mH+L._SL1500_.jpg', TRUE, NOW());

-- Add DELETE statement before other inserts to ensure no duplicate entries
INSERT INTO product_images (product_id, image_url, is_primary, upload_date)
VALUES
-- Complete any remaining products with at least one primary image
(84, 'https://m.media-amazon.com/images/I/61j+OqJFt6L._SL1500_.jpg', TRUE, NOW()),
(85, 'https://m.media-amazon.com/images/I/71hBZ28fvqL._SL1500_.jpg', TRUE, NOW()),
(87, 'https://m.media-amazon.com/images/I/71Fh2u5dDmL._SL1500_.jpg', TRUE, NOW()),
(88, 'https://m.media-amazon.com/images/I/61CEEQAecFL._SL1500_.jpg', TRUE, NOW()),
(90, 'https://m.media-amazon.com/images/I/61xtHkgnJHL._SL1500_.jpg', TRUE, NOW()),
(91, 'https://cdn.shopify.com/s/files/1/0374/9456/0251/products/vitamin-c-powder-0-1oz-front_1200x.jpg', TRUE, NOW()),
(92, 'https://m.media-amazon.com/images/I/71Wci+QHWUL._SL1500_.jpg', TRUE, NOW()),
(93, 'https://m.media-amazon.com/images/I/81AOrjY2OIL._AC_SL1500_.jpg', TRUE, NOW());


-- First, let's delete any existing product variants to avoid duplicates
DELETE FROM product_variants;

-- Adidas Ultraboost 23 variants
INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (60, 'US 7', 5, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (60, 'US 8', 8, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (60, 'US 9', 10, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (60, 'US 10', 7, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (60, 'US 11', 5, NOW(), NOW());

-- Nike Air Force 1 variants
INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (62, 'US 7', 6, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (62, 'US 8', 9, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (62, 'US 9', 12, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (62, 'US 10', 8, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (62, 'US 11', 5, NOW(), NOW());

-- Adidas Tiro Track Jacket variants
INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (61, 'S', 7, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (61, 'M', 10, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (61, 'L', 12, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (61, 'XL', 6, NOW(), NOW());

-- Nike Dri-FIT T-Shirt variants
INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (63, 'S', 10, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (63, 'M', 15, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (63, 'L', 15, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (63, 'XL', 10, NOW(), NOW());

-- Zara Slim Fit Blazer variants
INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (64, '48', 5, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (64, '50', 7, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (64, '52', 8, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (64, '54', 5, NOW(), NOW());

-- Zara Chino Trousers variants
INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (65, '30', 6, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (65, '32', 8, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (65, '34', 10, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (65, '36', 6, NOW(), NOW());

-- Adidas Cloudfoam Pure variants
INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (67, 'US 5', 7, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (67, 'US 6', 9, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (67, 'US 7', 10, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (67, 'US 8', 9, NOW(), NOW());

-- Nike Air Max 270 variants
INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (69, 'US 5', 6, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (69, 'US 6', 8, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (69, 'US 7', 10, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (69, 'US 8', 6, NOW(), NOW());

-- Zara Pleated Midi Skirt variants
INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (71, 'XS', 5, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (71, 'S', 7, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (71, 'M', 8, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (71, 'L', 5, NOW(), NOW());

-- Adidas Kids Superstar variants
INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (74, 'US 1', 5, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (74, 'US 2', 6, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (74, 'US 3', 7, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (74, 'US 4', 5, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (74, 'US 5', 2, NOW(), NOW());

-- Add additional variants for other clothing items

-- Zara Oxford Shirt variants
INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (66, 'S', 8, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (66, 'M', 12, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (66, 'L', 10, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (66, 'XL', 6, NOW(), NOW());

-- Adidas Essentials Hoodie variants
INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (68, 'XS', 7, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (68, 'S', 10, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (68, 'M', 15, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (68, 'L', 12, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (68, 'XL', 8, NOW(), NOW());

-- Nike Sportswear Leggings variants
INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (70, 'XS', 10, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (70, 'S', 15, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (70, 'M', 18, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (70, 'L', 12, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (70, 'XL', 8, NOW(), NOW());

-- Zara Oversized Blazer variants
INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (72, 'XS', 6, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (72, 'S', 9, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (72, 'M', 12, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (72, 'L', 7, NOW(), NOW());

-- Zara High Waist Jeans variants
INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (73, '24', 5, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (73, '26', 8, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (73, '28', 12, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (73, '30', 10, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (73, '32', 7, NOW(), NOW());

-- Adidas Kids Tracksuit variants
INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (75, '4Y', 8, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (75, '6Y', 10, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (75, '8Y', 12, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (75, '10Y', 9, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (75, '12Y', 7, NOW(), NOW());

-- Nike Kids Air Max variants
INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (76, 'US 11C', 6, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (76, 'US 12C', 8, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (76, 'US 13C', 10, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (76, 'US 1Y', 9, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (76, 'US 2Y', 7, NOW(), NOW());

-- Nike Kids Dri-FIT Set variants
INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (77, '4Y', 7, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (77, '6Y', 9, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (77, '8Y', 11, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (77, '10Y', 8, NOW(), NOW());

INSERT INTO product_variants (product_id, size, stock, created_at, updated_at)
VALUES (77, '12Y', 6, NOW(), NOW());