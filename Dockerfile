# Use official Python image as a base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Install system dependencies required for mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install Python dependencies from requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application into the container
COPY . .

# Expose the port for the application
EXPOSE 8000

# Command to run the application using uvicorn for async support
CMD ["uvicorn", "NewsPortal.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--reload"]
