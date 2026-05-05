FROM python:3.11-slim

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir -e .

# Copy the capstone application code
COPY ./03_capstone_wiki_engine /app/03_capstone_wiki_engine

# Expose the FastAPI port
EXPOSE 8000

# Start the Gateway
CMD ["uvicorn", "03_capstone_wiki_engine.gateway_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
