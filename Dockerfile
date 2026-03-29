# Use a lightweight Python base image
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Upgrade pip and install the package
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir .

# Define the entry point so the container acts like the CLI executable
ENTRYPOINT ["shellens"]

# Default command if none is provided
CMD ["--help"]