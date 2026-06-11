# Use official lightweight Python image
FROM python:3.12-slim

# Create a non-root user for security
RUN useradd -m appuser

# Set working directory
WORKDIR /app

# Copy dependency file first for layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Change ownership of application files
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Document application port
EXPOSE 5000

# Start Flask application
CMD ["python", "app.py"]