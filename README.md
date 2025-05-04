# E-commerce Backend API

Backend API cho ứng dụng E-commerce trên di động, xây dựng bằng FastAPI và Python.

## Chạy ứng dụng với Docker Compose

Bạn có thể chạy toàn bộ ứng dụng bao gồm API và các cơ sở dữ liệu (PostgreSQL, MongoDB, Redis) sử dụng Docker Compose:

```bash
# Tạo file .env từ file mẫu
cp .env.example .env

# Khởi động tất cả dịch vụ
docker-compose up -d

# Kiểm tra trạng thái các dịch vụ
docker-compose ps

# Xem logs
docker-compose logs -f

# Xem logs của một dịch vụ cụ thể
docker-compose logs -f api

# Dừng các dịch vụ
docker-compose down

# Xóa toàn bộ dữ liệu (cẩn thận)
docker-compose down -v
```

Sau khi khởi động, bạn có thể truy cập:
- API Documentation: http://localhost:8000/api/docs
- API Endpoints: http://localhost:8000/api/v1/...

### Chỉ chạy cơ sở dữ liệu

Nếu bạn muốn chạy API từ môi trường phát triển cục bộ, bạn có thể chỉ chạy các dịch vụ cơ sở dữ liệu:

```bash
docker-compose up -d postgres mongodb redis
```

Lưu ý: Khi sử dụng với môi trường phát triển cục bộ, bạn cần cập nhật file `.env` để sử dụng `localhost` thay vì tên service:

```
POSTGRES_SERVER=localhost
MONGO_URL=mongodb://localhost:27017
REDIS_HOST=localhost
```

### Thông tin kết nối cơ sở dữ liệu

PostgreSQL:
- Host: postgres (hoặc localhost khi chạy từ máy host)
- Port: 5432
- Username: postgres
- Password: postgres
- Database: ecommerce

MongoDB:
- URL: mongodb://mongodb:27017 (hoặc mongodb://localhost:27017 khi chạy từ máy host)
- Database: ecommerce

Redis:
- Host: redis (hoặc localhost khi chạy từ máy host)
- Port: 6379

## Cài đặt phát triển cục bộ

1. Sao chép file môi trường:

```bash
cp .env.example .env
```

2. Cài đặt các thư viện Python:

```bash
pip install -r requirements.txt
```

## Khởi chạy ứng dụng trong môi trường phát triển

```bash
# Chạy ứng dụng với uvicorn
uvicorn app.main:app --reload

# Hoặc sử dụng Python
python -m uvicorn app.main:app --reload
```

## Chạy Database Migrations

```bash
# Tạo migration
alembic revision --autogenerate -m "description"

# Áp dụng migration
alembic upgrade head
```

## Chạy migration với Docker Compose

```bash
# Chạy migration
docker-compose exec api alembic upgrade head

# Tạo migration mới
docker-compose exec api alembic revision --autogenerate -m "description"
```

## Thành phần của dự án

- **app/**: Mã nguồn chính của ứng dụng
  - **core/**: Cấu hình, bảo mật và các thành phần cốt lõi
  - **models/**: Models cho cơ sở dữ liệu
  - **schemas/**: Pydantic models cho validation và serialization
  - **routers/**: Route handlers cho API
  - **services/**: Business logic
  - **db/**: Kết nối và cấu hình cơ sở dữ liệu
  - **auth/**: Xác thực và phân quyền
- **migrations/**: Alembic migrations
- **docs/**: Tài liệu API
- **tests/**: Unit và integration tests

## License

MIT