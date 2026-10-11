FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

# Expose port (default Flask port)
EXPOSE 5000

ENV PORT=5000 \
    PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
