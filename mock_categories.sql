-- Mock data for categories about electronics, household items, and clothing

-- Main Categories
INSERT INTO categories (category_name, description, parent_id, image_url, created_at, updated_at)
VALUES 
-- Main categories
('Đồ điện tử', 'Các sản phẩm điện tử, công nghệ', NULL, 'https://example.com/images/categories/electronics.jpg', NOW(), NOW()),
('Đồ gia dụng', 'Các thiết bị và vật dụng trong gia đình', NULL, 'https://example.com/images/categories/household.jpg', NOW(), NOW()),
('Thời trang', 'Quần áo, giày dép và phụ kiện thời trang', NULL, 'https://example.com/images/categories/fashion.jpg', NOW(), NOW()),
('Sức khỏe & Làm đẹp', 'Sản phẩm chăm sóc sức khỏe và làm đẹp', NULL, 'https://example.com/images/categories/health_beauty.jpg', NOW(), NOW());

-- Electronics subcategories (parent_id = 1)
INSERT INTO categories (category_name, description, parent_id, image_url, created_at, updated_at)
VALUES 
('Điện thoại & Máy tính bảng', 'Điện thoại di động, máy tính bảng và phụ kiện', 1, 'https://example.com/images/categories/phones_tablets.jpg', NOW(), NOW()),
('Laptop & Máy tính', 'Máy tính xách tay, máy tính để bàn và linh kiện', 1, 'https://example.com/images/categories/computers.jpg', NOW(), NOW()),
('Thiết bị âm thanh', 'Loa, tai nghe và thiết bị âm thanh', 1, 'https://example.com/images/categories/audio.jpg', NOW(), NOW()),
('Tivi & Thiết bị giải trí', 'Tivi, đầu phát và thiết bị giải trí gia đình', 1, 'https://example.com/images/categories/tv_entertainment.jpg', NOW(), NOW()),
('Máy ảnh & Máy quay', 'Máy ảnh, máy quay phim và phụ kiện', 1, 'https://example.com/images/categories/cameras.jpg', NOW(), NOW()),
('Thiết bị thông minh', 'Thiết bị nhà thông minh và wearables', 1, 'https://example.com/images/categories/smart_devices.jpg', NOW(), NOW());

-- Household items subcategories (parent_id = 2)
INSERT INTO categories (category_name, description, parent_id, image_url, created_at, updated_at)
VALUES 
('Đồ dùng nhà bếp', 'Thiết bị và dụng cụ nhà bếp', 2, 'https://example.com/images/categories/kitchen.jpg', NOW(), NOW()),
('Thiết bị điện gia dụng', 'Máy giặt, tủ lạnh, máy hút bụi và các thiết bị điện khác', 2, 'https://example.com/images/categories/appliances.jpg', NOW(), NOW()),
('Đồ nội thất', 'Bàn ghế, giường, tủ và các đồ nội thất khác', 2, 'https://example.com/images/categories/furniture.jpg', NOW(), NOW()),
('Dụng cụ & Thiết bị sửa chữa', 'Dụng cụ sửa chữa và cải tạo nhà cửa', 2, 'https://example.com/images/categories/tools.jpg', NOW(), NOW()),
('Đồ dùng phòng tắm', 'Thiết bị và vật dụng phòng tắm', 2, 'https://example.com/images/categories/bathroom.jpg', NOW(), NOW()),
('Đồ trang trí nội thất', 'Đèn, tranh ảnh và các vật dụng trang trí', 2, 'https://example.com/images/categories/decor.jpg', NOW(), NOW());

-- Fashion subcategories (parent_id = 3)
INSERT INTO categories (category_name, description, parent_id, image_url, created_at, updated_at)
VALUES 
('Thời trang nam', 'Quần áo, giày dép và phụ kiện cho nam', 3, 'https://example.com/images/categories/men_fashion.jpg', NOW(), NOW()),
('Thời trang nữ', 'Quần áo, giày dép và phụ kiện cho nữ', 3, 'https://example.com/images/categories/women_fashion.jpg', NOW(), NOW()),
('Thời trang trẻ em', 'Quần áo và giày dép cho trẻ em', 3, 'https://example.com/images/categories/kids_fashion.jpg', NOW(), NOW()),
('Đồng hồ', 'Đồng hồ đeo tay các loại', 3, 'https://example.com/images/categories/watches.jpg', NOW(), NOW()),
('Trang sức', 'Nhẫn, dây chuyền, vòng tay và các loại trang sức', 3, 'https://example.com/images/categories/jewelry.jpg', NOW(), NOW()),
('Túi xách & Balo', 'Túi xách, balo, ví và vali', 3, 'https://example.com/images/categories/bags.jpg', NOW(), NOW());

-- Health & Beauty subcategories (parent_id = 4)
INSERT INTO categories (category_name, description, parent_id, image_url, created_at, updated_at)
VALUES 
('Mỹ phẩm', 'Sản phẩm trang điểm và làm đẹp', 4, 'https://example.com/images/categories/cosmetics.jpg', NOW(), NOW()),
('Chăm sóc da', 'Sản phẩm chăm sóc da mặt và cơ thể', 4, 'https://example.com/images/categories/skincare.jpg', NOW(), NOW()),
('Chăm sóc tóc', 'Sản phẩm chăm sóc và tạo kiểu tóc', 4, 'https://example.com/images/categories/haircare.jpg', NOW(), NOW()),
('Nước hoa', 'Nước hoa cho nam và nữ', 4, 'https://example.com/images/categories/perfume.jpg', NOW(), NOW()),
('Thiết bị làm đẹp', 'Máy sấy tóc, máy cạo râu và các thiết bị làm đẹp', 4, 'https://example.com/images/categories/beauty_devices.jpg', NOW(), NOW()),
('Thực phẩm chức năng', 'Vitamin, thực phẩm bổ sung và sản phẩm chăm sóc sức khỏe', 4, 'https://example.com/images/categories/supplements.jpg', NOW(), NOW());
