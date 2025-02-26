# Build Python environment
FROM python:3.11-slim  
WORKDIR /app

# Cài đặt thư viện trực tiếp (bỏ qua builder stage)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt  

# Copy mã nguồn và model
COPY . .

# Chạy ứng dụng
CMD ["python", "app.py"]
