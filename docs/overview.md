Tài liệu API Backend Ecommerce
1. Tổng quan kiến trúc
Mô hình kiến trúc
Backend API được xây dựng theo kiến trúc nhiều lớp:
Apply to auth.py
API Endpoints (routers): Xử lý request HTTP, validate input và trả về response
Services: Chứa logic nghiệp vụ
Models: Định nghĩa cấu trúc dữ liệu và tương tác với database
Schemas: Đảm bảo validation và serialization dữ liệu
Công nghệ sử dụng
FastAPI: Framework web API hiệu năng cao
SQLAlchemy: ORM cho PostgreSQL
Pydantic: Validation và serialization
JWT: Xác thực và ủy quyền
PostgreSQL: Database chính
MongoDB: Database phụ (cho một số chức năng)
Redis: Cache và lưu trữ tạm thời
2. Xác thực và Bảo mật
JWT Authentication
Apply to auth.py
Cách hoạt động:
Client gửi username/password đến /api/v1/auth/login
Server xác thực và trả về JWT token
Client gửi JWT token trong header Authorization: Bearer {token} cho các API tiếp theo
Middleware get_current_user xác thực token và lấy thông tin user
Flow code:
Apply to auth.py
3. Tài liệu API
Authentication API
| Endpoint | Method | Mô tả | Request Body | Response |
|----------|--------|-------|-------------|----------|
| /api/v1/auth/register | POST | Đăng ký tài khoản mới | {"username": string, "email": string, "password": string, ...} | User object |
| /api/v1/auth/login | POST | Đăng nhập và lấy token | {"username": string, "password": string} | {"access_token": string, "token_type": "bearer"} |
User API
| Endpoint | Method | Mô tả | Request Body | Response |
|----------|--------|-------|-------------|----------|
| /api/v1/users/me | GET | Lấy thông tin user hiện tại | - | User object |
| /api/v1/users/me | PUT | Cập nhật thông tin user | {"full_name": string, ...} | User object |
Product API
| Endpoint | Method | Mô tả | Query Params | Response |
|----------|--------|-------|-------------|----------|
| /api/v1/products | GET | Lấy danh sách sản phẩm | skip, limit, category_id, search | Product list |
| /api/v1/products/{product_id} | GET | Lấy chi tiết sản phẩm | - | Product object |
| /api/v1/products/favorites | GET | Lấy sản phẩm yêu thích | - | Product list |
| /api/v1/products/{product_id}/favorites | POST | Thêm vào yêu thích | - | Success response |
| /api/v1/products/barcode/{barcode} | GET | Tìm sản phẩm theo mã vạch | - | Product object |
Cart API
| Endpoint | Method | Mô tả | Request Body | Response |
|----------|--------|-------|-------------|----------|
| /api/v1/carts | GET | Lấy giỏ hàng hiện tại | - | Cart object |
| /api/v1/carts/items | POST | Thêm sản phẩm vào giỏ hàng | {"product_id": int, "quantity": int} | Cart object |
| /api/v1/carts/items/{item_id} | PUT | Cập nhật số lượng | {"quantity": int} | Cart object |
| /api/v1/carts/items/{item_id} | DELETE | Xóa sản phẩm khỏi giỏ hàng | - | Cart object |
Shopping List API
| Endpoint | Method | Mô tả | Request Body | Response |
|----------|--------|-------|-------------|----------|
| /api/v1/shopping-lists | GET | Lấy danh sách mua sắm | - | List of shopping lists |
| /api/v1/shopping-lists | POST | Tạo danh sách mới | {"list_name": string, ...} | Shopping list object |
| /api/v1/shopping-lists/{list_id}/items | POST | Thêm sản phẩm vào danh sách | {"product_id": int, ...} | List item object |
Order API
| Endpoint | Method | Mô tả | Request Body | Response |
|----------|--------|-------|-------------|----------|
| /api/v1/orders | GET | Lấy danh sách đơn hàng | skip, limit, status | Order list |
| /api/v1/orders | POST | Tạo đơn hàng mới | {"shipping_address_id": int, ...} | Order object |
| /api/v1/orders/{order_id} | GET | Lấy chi tiết đơn hàng | - | Order object |
Barcode API
| Endpoint | Method | Mô tả | Request Body | Response |
|----------|--------|-------|-------------|----------|
| /api/v1/barcodes/scan | POST | Quét mã vạch từ ảnh | File upload | Product object |
| /api/v1/barcodes/{barcode} | GET | Lấy sản phẩm theo mã vạch | - | Product object |
4. Luồng xử lý chính
Luồng xử lý đơn hàng
Apply to auth.py
Luồng quét mã vạch và thêm vào giỏ hàng
Apply to auth.py
5. Cấu trúc thư mục
Apply to auth.py
6. Chi tiết các module quan trọng
Services
Services xử lý logic nghiệp vụ chính:
UserService: Quản lý người dùng
ProductService: Quản lý sản phẩm, tìm kiếm, phân loại
CartService: Quản lý giỏ hàng
OrderService: Xử lý đơn hàng
PaymentService: Xử lý thanh toán
ShoppingListService: Quản lý danh sách mua sắm
BarcodeService: Xử lý quét mã vạch
Models
Models định nghĩa cấu trúc database:
User: Thông tin người dùng
Product: Thông tin sản phẩm
Cart/CartItem: Giỏ hàng và các mục
Order/OrderItem: Đơn hàng và các mục
ShoppingList/ListItem: Danh sách mua sắm và các mục
Category/Brand: Danh mục và thương hiệu
Payment: Thanh toán
Authentication
JWT Token: Token-based authentication
Role-based Authorization: Admin vs Regular User
7. Best Practices
Coding Practices
Dependency Injection: Sử dụng FastAPI Depends
Async/Await: Tất cả các handlers sử dụng async để tối ưu hiệu suất
Error Handling: Xử lý exception thống nhất
Validation: Sử dụng Pydantic để validate input/output
Security Practices
Password Hashing: Bcrypt cho mật khẩu
JWT Security: Sử dụng expiration time và algorithm an toàn
Data Validation: Tất cả input đều được validate
Database Practices
ORM: Sử dụng SQLAlchemy để tương tác với database
Migrations: Quản lý schema changes với Alembic
Transactions: Đảm bảo atomic operations
Tài liệu này cung cấp tổng quan về cấu trúc API và cách hoạt động của các phần code trong backend ecommerce. Để biết thêm chi tiết về mỗi endpoint, hãy tham khảo API documentation trực tiếp tại /api/docs khi chạy ứng dụng.