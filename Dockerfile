# Use official Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy local Python script to container
COPY app.py .

# Run the Python script
CMD ["python", "app.py"]
