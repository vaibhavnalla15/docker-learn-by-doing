# Use official Python lightweight image
FROM python:3.12-slim 

# Create a non-root user
RUN useradd -m appuser

# Set working directory 
WORKDIR /app 

# Copy dependencies first for layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code 
COPY app.py .

# Change ownership to non-root user
RUN chown -R appuser:appuser /app 
 
# Switch to non-root user
USER appuser

# Document Flask port
EXPOSE 5000

# Start the application 
CMD [ "python", "app.py" ]