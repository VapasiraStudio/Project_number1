# use official lightweight python image as base
FROM python:3.11-slim AS builder

# Installing dependencies needed to build Python packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Create a virtual environment
RUN python -m venv /opt/venv
# Activate the virtual environment for subsequent commands
ENV PATH="/opt/venv/bin:$PATH"

# Copy the file with dependencies
COPY requirements.txt .

# Installing dependencies into a virtual environment
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


# The final image
FROM python:3.11-slim AS runtime

# Install system dependencies required for runtime
RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq5 gcc && \
    rm -rf /var/lib/apt/lists/*

# Copying the virtual environment from the builder stage
COPY --from=builder /opt/venv /opt/venv

# Setting environment variables
ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Create and switch to an unprivileged user
RUN adduser --disabled-password --gecos "" appuser
USER appuser

# Set the working directory
WORKDIR /app

# Copy the source code of the application
COPY --chown=appuser:appuser ./src/ ./src/

# Open the port that FastAPI listens to
EXPOSE 8000

# Command to run the application
CMD ["python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]