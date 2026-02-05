# Use official Python slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependency list and install
COPY requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements-dev.txt

# Copy the rest of the project
COPY . .

# Default command: run tests
CMD ["pytest", "-v"]