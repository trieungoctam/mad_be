# Xác thực và Bảo mật

## Tổng quan
Hệ thống API E-commerce sử dụng JWT (JSON Web Tokens) để xác thực và phân quyền người dùng. Cơ chế này cho phép ứng dụng xác thực người dùng mà không cần duy trì trạng thái phiên làm việc ở phía máy chủ, phù hợp với kiến trúc RESTful.

## Quy trình đăng ký và đăng nhập

### Đăng ký tài khoản
1. Client gửi request `POST /api/v1/auth/register` với thông tin:
   ```json
   {
     "email": "user@example.com",
     "password": "secure_password",
     "full_name": "Nguyễn Văn A",
     "phone_number": "0123456789"
   }
   ```

2. Hệ thống kiểm tra tính hợp lệ của dữ liệu:
   - Email chưa được sử dụng
   - Mật khẩu đáp ứng các yêu cầu bảo mật (ít nhất 8 ký tự, bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt)
   - Các trường bắt buộc đã được cung cấp

3. Mật khẩu được băm (hash) bằng thuật toán bcrypt trước khi lưu vào cơ sở dữ liệu

4. Tài khoản được tạo và trả về thông tin người dùng (không bao gồm mật khẩu)

### Đăng nhập
1. Client gửi request `POST /api/v1/auth/login` với:
   ```json
   {
     "email": "user@example.com",
     "password": "secure_password"
   }
   ```

2. Hệ thống kiểm tra email và mật khẩu

3. Nếu xác thực thành công, hệ thống tạo và trả về:
   - Access token (JWT, hết hạn sau 30 phút)
   - Refresh token (JWT, hết hạn sau 7 ngày)

## Cấu trúc JWT Token

### Access Token
```
Header: {
  "alg": "HS256",
  "typ": "JWT"
}

Payload: {
  "sub": "user-uuid",
  "is_superuser": false,
  "exp": 1680000000,  // Thời gian hết hạn
  "iat": 1679998200,  // Thời gian phát hành
  "jti": "unique-token-id"
}
```

### Refresh Token
```
Header: {
  "alg": "HS256",
  "typ": "JWT"
}

Payload: {
  "sub": "user-uuid",
  "token_type": "refresh",
  "exp": 1680604800,  // Thời gian hết hạn (7 ngày)
  "iat": 1679998200,  // Thời gian phát hành
  "jti": "unique-token-id"
}
```

## Xác thực API Endpoints

Hầu hết các API endpoints yêu cầu xác thực bằng cách gửi JWT token trong header:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Quy trình xác thực request
1. Client gửi request với access token trong header
2. Middleware xác thực kiểm tra:
   - Token có tồn tại không
   - Token có đúng định dạng không
   - Token có hợp lệ không (chữ ký, thời hạn)
3. Nếu token hợp lệ, request được xử lý với thông tin người dùng được trích xuất từ token
4. Nếu token không hợp lệ hoặc hết hạn, trả về lỗi 401 (Unauthorized)

## Làm mới Token

Khi access token hết hạn, client có thể sử dụng refresh token để lấy access token mới:

1. Client gửi request `POST /api/v1/auth/refresh` với refresh token:
   ```json
   {
     "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
   }
   ```

2. Nếu refresh token hợp lệ, hệ thống tạo access token mới và trả về:
   ```json
   {
     "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
     "token_type": "bearer"
   }
   ```

## Đăng xuất

Để đăng xuất, client gửi request `POST /api/v1/auth/logout` với access token trong header. Khi đó:

1. Refresh token hiện tại được thêm vào danh sách token bị vô hiệu hóa
2. Client xóa access token và refresh token đã lưu trữ

## Phân quyền

Hệ thống có hai vai trò chính:
- `User`: Người dùng thông thường
- `Admin`: Quản trị viên với quyền truy cập bổ sung

Các endpoint được bảo vệ bằng cách kiểm tra vai trò người dùng:

```python
# Ví dụ middleware kiểm tra quyền Admin
async def admin_required(request: Request, current_user = Depends(get_current_user)):
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Không đủ quyền truy cập"
        )
    return current_user
```

## Bảo mật

### Lưu trữ mật khẩu
- Mật khẩu được băm bằng bcrypt với salt ngẫu nhiên
- Cơ sở dữ liệu không lưu trữ mật khẩu gốc

### Bảo vệ chống tấn công
- Rate limiting để ngăn chặn tấn công brute force
- Validation đầu vào để ngăn chặn tấn công injection
- HTTPS cho tất cả các request
- CORS được cấu hình đúng cách để ngăn chặn truy cập trái phép
- Headers bảo mật như X-Content-Type-Options, X-Frame-Options, và Content-Security-Policy

### Xử lý thông tin nhạy cảm
- Thông tin thanh toán được mã hóa
- Dữ liệu người dùng nhạy cảm được bảo vệ theo quy định GDPR/PDPA