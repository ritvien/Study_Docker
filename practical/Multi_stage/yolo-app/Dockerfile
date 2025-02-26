# Stage 1: Build Python environment
FROM python:3.11 AS builder
WORKDIR /app


# Cài đặt các thư viện hệ thống cần thiết (bao gồm libGL)
RUN apt-get update && apt-get install -y gcc libpq-dev libgl1 libglib2.0-0 


# Cài đặt thư viện trước để tối ưu cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt  

# Stage 2: Tạo image nhẹ hơn để chạy API
FROM python:3.11-slim  
WORKDIR /app

# Copy toàn bộ thư viện đã cài từ builder stage
COPY --from=builder /usr/local /usr/local

# Copy mã nguồn và model
COPY . .

# Chạy ứng dụng
CMD ["python", "app.py"]
