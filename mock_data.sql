-- Mock data for categories and brands

-- Categories
INSERT INTO categories (category_name, description, parent_id, image_url, created_at, updated_at)
VALUES 
('Điện thoại', 'Các loại điện thoại di động', NULL, 'https://example.com/images/categories/phones.jpg', NOW(), NOW()),
('Laptop', 'Máy tính xách tay các loại', NULL, 'https://example.com/images/categories/laptops.jpg', NOW(), NOW()),
('Phụ kiện', 'Phụ kiện điện tử các loại', NULL, 'https://example.com/images/categories/accessories.jpg', NOW(), NOW()),
('Tai nghe', 'Các loại tai nghe', 3, 'https://example.com/images/categories/headphones.jpg', NOW(), NOW());

-- Brands
INSERT INTO brands (brand_name, description, logo_url, website, created_at, updated_at)
VALUES 
('Apple', 'Công ty công nghệ đa quốc gia của Mỹ', 'https://example.com/images/brands/apple.png', 'https://www.apple.com', NOW(), NOW()),
('Samsung', 'Tập đoàn đa quốc gia của Hàn Quốc', 'https://example.com/images/brands/samsung.png', 'https://www.samsung.com', NOW(), NOW()),
('Xiaomi', 'Công ty công nghệ Trung Quốc', 'https://example.com/images/brands/xiaomi.png', 'https://www.mi.com', NOW(), NOW()),
('Dell', 'Công ty máy tính đa quốc gia của Mỹ', 'https://example.com/images/brands/dell.png', 'https://www.dell.com', NOW(), NOW()),
('HP', 'Hewlett-Packard, công ty công nghệ thông tin Mỹ', 'https://example.com/images/brands/hp.png', 'https://www.hp.com', NOW(), NOW()),
('Asus', 'Công ty máy tính Đài Loan', 'https://example.com/images/brands/asus.png', 'https://www.asus.com', NOW(), NOW()),
('Lenovo', 'Công ty máy tính đa quốc gia Trung Quốc', 'https://example.com/images/brands/lenovo.png', 'https://www.lenovo.com', NOW(), NOW()),
('Sony', 'Tập đoàn đa quốc gia của Nhật Bản', 'https://example.com/images/brands/sony.png', 'https://www.sony.com', NOW(), NOW()),
('JBL', 'Công ty âm thanh Mỹ', 'https://example.com/images/brands/jbl.png', 'https://www.jbl.com', NOW(), NOW()),
('Anker', 'Công ty phụ kiện điện tử Trung Quốc', 'https://example.com/images/brands/anker.png', 'https://www.anker.com', NOW(), NOW());
