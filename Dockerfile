# 1. Base image
FROM python:3.10-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy dependency list
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy application code
COPY . .

# 6. Command to run when container starts
CMD ["python", "src/flask_app.py"]

