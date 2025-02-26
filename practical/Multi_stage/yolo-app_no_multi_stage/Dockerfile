# Build Python environment
FROM python:3.11-slim  
WORKDIR /app


# Cài đặt các thư viện hệ thống cần thiết (bao gồm libGL)
RUN apt-get update && apt-get install -y gcc libpq-dev libgl1 libglib2.0-0 

# Cài đặt thư viện trực tiếp (bỏ qua builder stage)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt  

# Copy mã nguồn và model
COPY . .

# Chạy ứng dụng
CMD ["python", "app.py"]
