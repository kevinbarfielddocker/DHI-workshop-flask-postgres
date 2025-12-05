FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
RUN pip install psycopg2-binary
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]