# Xử lý lỗi trong API

## Tổng quan

Hệ thống API E-commerce được thiết kế để xử lý lỗi một cách nhất quán, trả về các phản hồi lỗi theo định dạng chuẩn, giúp client xử lý lỗi dễ dàng và người dùng có thể hiểu được vấn đề.

## Cấu trúc phản hồi lỗi

Tất cả các phản hồi lỗi API đều tuân theo cấu trúc JSON sau:

```json
{
  "status_code": 400,
  "message": "Thông báo lỗi cho người dùng",
  "detail": "Chi tiết kỹ thuật về lỗi hoặc hướng dẫn cụ thể",
  "errors": [
    {
      "field": "email",
      "message": "Email không hợp lệ"
    }
  ],
  "request_id": "unique-request-identifier"
}
```

Trong đó:
- `status_code`: Mã HTTP status code
- `message`: Thông báo lỗi ngắn gọn, thân thiện với người dùng
- `detail`: Thông tin chi tiết hơn về lỗi (tùy chọn)
- `errors`: Mảng các lỗi cụ thể nếu có nhiều lỗi (ví dụ: validation errors)
- `request_id`: ID duy nhất cho request, hữu ích cho việc debug và ghi log

## Phân loại mã lỗi HTTP

### 400 Bad Request
- Lỗi validation dữ liệu đầu vào
- Thiếu tham số bắt buộc
- Định dạng dữ liệu không hợp lệ

### 401 Unauthorized
- Không cung cấp thông tin xác thực
- Token xác thực không hợp lệ hoặc hết hạn
- Thông tin đăng nhập không chính xác

### 403 Forbidden
- Người dùng không có quyền truy cập vào tài nguyên
- Tài khoản bị khóa hoặc bị hạn chế

### 404 Not Found
- Tài nguyên không tồn tại
- Endpoint không tồn tại

### 409 Conflict
- Xung đột dữ liệu (ví dụ: email đã tồn tại)
- Điều kiện ràng buộc không được đáp ứng

### 422 Unprocessable Entity
- Dữ liệu hợp lệ về định dạng nhưng không thể xử lý vì lý do nghiệp vụ
- Ví dụ: Sản phẩm hết hàng, số lượng vượt quá giới hạn

### 429 Too Many Requests
- Vượt quá giới hạn số lượng request (rate limiting)

### 500 Internal Server Error
- Lỗi không xác định từ phía server
- Lỗi này không bao giờ hiển thị chi tiết kỹ thuật cho client, chỉ hiển thị thông báo chung

## Xử lý lỗi validation

Hệ thống sử dụng Pydantic để validation dữ liệu đầu vào. Khi dữ liệu không hợp lệ, phản hồi lỗi sẽ bao gồm chi tiết về từng trường không hợp lệ:

```json
{
  "status_code": 400,
  "message": "Dữ liệu không hợp lệ",
  "errors": [
    {
      "field": "email",
      "message": "Email không đúng định dạng"
    },
    {
      "field": "password",
      "message": "Mật khẩu phải có ít nhất 8 ký tự"
    }
  ],
  "request_id": "req-123456"
}
```

## Xử lý lỗi nghiệp vụ

Lỗi nghiệp vụ là các lỗi phát sinh từ logic ứng dụng, ví dụ:

```json
{
  "status_code": 422,
  "message": "Không thể xử lý đơn hàng",
  "detail": "Sản phẩm 'Điện thoại XYZ' đã hết hàng",
  "request_id": "req-123456"
}
```

## Xử lý lỗi hệ thống

Lỗi hệ thống (500) được xử lý đặc biệt:

1. Chi tiết kỹ thuật về lỗi KHÔNG bao giờ được trả về cho client
2. Lỗi được ghi đầy đủ vào hệ thống log với request_id
3. Thông báo lỗi chung chung được trả về cho client

```json
{
  "status_code": 500,
  "message": "Đã xảy ra lỗi, vui lòng thử lại sau",
  "request_id": "req-123456"
}
```

## Ghi log lỗi

Tất cả các lỗi được ghi log với các thông tin sau:

- Request ID
- Thời gian xảy ra
- Endpoint bị ảnh hưởng
- HTTP method
- IP người dùng
- User ID (nếu đã xác thực)
- Chi tiết kỹ thuật về lỗi
- Stack trace (chỉ với lỗi 500)

## Xử lý lỗi trên client

Client được khuyến nghị xử lý lỗi theo cách sau:

1. Kiểm tra `status_code` để xác định loại lỗi
2. Hiển thị `message` cho người dùng
3. Với lỗi validation, hiển thị các lỗi cụ thể từ mảng `errors`
4. Lưu trữ `request_id` để báo cáo vấn đề nếu cần thiết

## Ví dụ cách triển khai xử lý lỗi

```python
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    error_response = {
        "status_code": exc.status_code,
        "message": exc.detail,
        "request_id": request.state.request_id
    }

    if hasattr(exc, "errors"):
        error_response["errors"] = exc.errors

    return JSONResponse(
        status_code=exc.status_code,
        content=error_response
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    # Log detailed error info with stack trace
    logger.error(
        f"Unhandled exception: {str(exc)}",
        extra={
            "request_id": request.state.request_id,
            "path": request.url.path,
            "method": request.method,
            "client_ip": request.client.host
        },
        exc_info=True
    )

    return JSONResponse(
        status_code=500,
        content={
            "status_code": 500,
            "message": "Đã xảy ra lỗi, vui lòng thử lại sau",
            "request_id": request.state.request_id
        }
    )
```