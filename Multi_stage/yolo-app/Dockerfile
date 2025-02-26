# Stage 1: Build Python environment
FROM python:3.11 AS builder
WORKDIR /app

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
