FROM python:3.11-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PLAYWRIGHT_BROWSERS_PATH=/usr/local/lib/playwright

# Install system dependencies (formatted for reliability)
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    git \
    procps \
    gcc \
    python3-dev \
    libffi-dev \
    libssl-dev \
    libx11-dev \
    libxtst-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/project

# Copy requirements first for caching
COPY requirements.txt .

# Install Python packages with error handling
RUN pip install --upgrade pip && \
    { pip install --no-cache-dir -r requirements.txt || \
    pip install --no-cache-dir -r requirements.txt --ignore-installed; } && \
    pip install debugpy

# Install Playwright browsers
RUN playwright install --with-deps chromium

# Copy application
COPY . .

CMD ["pytest", "tests/test_login.py"]