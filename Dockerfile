# Use a full Debian-based image with Python 3.11 installed
FROM python:3.11-buster

# Install any additional dependencies you need
RUN apt-get update && apt-get install -y \
    && apt-get clean

# Copy your app into the container
COPY . /app

# Set the working directory
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app will run on
EXPOSE 8765

# Run your application
CMD ["python", "main.py"]
