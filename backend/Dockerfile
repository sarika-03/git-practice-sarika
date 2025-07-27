FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Flask app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
