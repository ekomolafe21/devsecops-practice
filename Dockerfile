# Use an official lightweight Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency list and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Command to run the app
CMD ["python", "app.py"]
