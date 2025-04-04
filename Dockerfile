# Use official lightweight Python image
FROM python:3.11.8-slim

# Set working directory inside the container
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Ensure logs are unbuffered so they appear in `docker logs`
ENV PYTHONUNBUFFERED=1
EXPOSE 8000

# Run Gunicorn with proper logging
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-", "--log-level", "info", "main:app"]
