# API Endpoints

## Xác thực
- `POST /api/v1/auth/register`: Đăng ký người dùng mới
- `POST /api/v1/auth/login`: Đăng nhập và lấy token

## User
- `GET /api/v1/users/me`: Lấy thông tin người dùng hiện tại
- `PUT /api/v1/users/me`: Cập nhật thông tin người dùng
- `GET /api/v1/users/{user_id}`: Lấy thông tin người dùng theo ID
- `GET /api/v1/users`: Lấy danh sách người dùng (admin only)

### Địa chỉ
- `GET /api/v1/users/me/addresses`: Lấy danh sách địa chỉ của người dùng
- `POST /api/v1/users/me/addresses`: Thêm địa chỉ mới
- `PUT /api/v1/users/me/addresses/{address_id}`: Cập nhật địa chỉ
- `DELETE /api/v1/users/me/addresses/{address_id}`: Xóa địa chỉ

## Danh sách mua sắm
- `GET /api/v1/shopping-lists`: Lấy danh sách mua sắm của người dùng
- `POST /api/v1/shopping-lists`: Tạo danh sách mua sắm mới
- `GET /api/v1/shopping-lists/{list_id}`: Lấy chi tiết danh sách mua sắm
- `PUT /api/v1/shopping-lists/{list_id}`: Cập nhật danh sách mua sắm
- `DELETE /api/v1/shopping-lists/{list_id}`: Xóa danh sách mua sắm

### Mục trong danh sách
- `POST /api/v1/shopping-lists/{list_id}/items`: Thêm mục vào danh sách
- `PUT /api/v1/shopping-lists/{list_id}/items/{item_id}`: Cập nhật mục trong danh sách
- `DELETE /api/v1/shopping-lists/{list_id}/items/{item_id}`: Xóa mục khỏi danh sách

### Chia sẻ danh sách
- `POST /api/v1/shopping-lists/{list_id}/share`: Chia sẻ danh sách với người dùng khác

## Quét mã vạch
- `POST /api/v1/barcodes/scan`: Quét mã vạch từ ảnh
- `POST /api/v1/barcodes/manual`: Nhập mã vạch thủ công
- `GET /api/v1/barcodes/history`: Lấy lịch sử quét mã vạch

## Sản phẩm
- `GET /api/v1/products`: Tìm kiếm và lọc sản phẩm
- `POST /api/v1/products`: Tạo sản phẩm mới (admin only)
- `GET /api/v1/products/{product_id}`: Lấy chi tiết sản phẩm
- `PUT /api/v1/products/{product_id}`: Cập nhật sản phẩm (admin only)
- `DELETE /api/v1/products/{product_id}`: Xóa sản phẩm (admin only)
- `GET /api/v1/products/barcode/{barcode}`: Tìm sản phẩm theo mã vạch
- `GET /api/v1/products/compare/{product_id}`: So sánh giá sản phẩm từ các cửa hàng

### Sản phẩm yêu thích
- `GET /api/v1/products/favorites`: Lấy danh sách sản phẩm yêu thích
- `POST /api/v1/products/favorites/{product_id}`: Thêm sản phẩm vào yêu thích
- `DELETE /api/v1/products/favorites/{product_id}`: Xóa sản phẩm khỏi yêu thích

## Giỏ hàng
- `GET /api/v1/carts`: Lấy giỏ hàng hiện tại
- `POST /api/v1/carts`: Tạo giỏ hàng mới
- `DELETE /api/v1/carts`: Xóa giỏ hàng hiện tại
- `POST /api/v1/carts/items`: Thêm sản phẩm vào giỏ hàng
- `PUT /api/v1/carts/items/{item_id}`: Cập nhật số lượng sản phẩm trong giỏ hàng
- `DELETE /api/v1/carts/items/{item_id}`: Xóa sản phẩm khỏi giỏ hàng

## Đơn hàng
- `GET /api/v1/orders`: Lấy danh sách đơn hàng
- `POST /api/v1/orders`: Tạo đơn hàng mới
- `GET /api/v1/orders/{order_id}`: Lấy chi tiết đơn hàng
- `PUT /api/v1/orders/{order_id}`: Cập nhật trạng thái đơn hàng (admin only)
- `GET /api/v1/orders/{order_id}/track`: Theo dõi vận chuyển đơn hàng

## Thanh toán
- `GET /api/v1/payments/settings`: Lấy cài đặt thanh toán
- `POST /api/v1/payments/settings`: Thêm cài đặt thanh toán mới
- `PUT /api/v1/payments/settings/{setting_id}`: Cập nhật cài đặt thanh toán
- `DELETE /api/v1/payments/settings/{setting_id}`: Xóa cài đặt thanh toán
- `POST /api/v1/payments/process`: Xử lý thanh toán
- `GET /api/v1/payments/transactions`: Lấy lịch sử giao dịch
- `GET /api/v1/payments/transactions/order/{order_id}`: Lấy giao dịch của đơn hàng

## Thông báo
- `GET /api/v1/notifications`: Lấy danh sách thông báo
- `GET /api/v1/notifications/count`: Lấy số lượng thông báo chưa đọc
- `PUT /api/v1/notifications/{notification_id}`: Đánh dấu thông báo đã đọc
- `PUT /api/v1/notifications/read-all`: Đánh dấu tất cả thông báo đã đọc
- `GET /api/v1/notifications/settings`: Lấy cài đặt thông báo
- `PUT /api/v1/notifications/settings`: Cập nhật cài đặt thông báo