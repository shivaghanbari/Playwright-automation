FROM python:3.11-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/opt/project
# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget git procps gcc python3-dev libffi-dev libssl-dev libx11-dev libxtst-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/project

# Copy entire project structure
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install debugpy

# Install Playwright browsers
RUN playwright install --with-deps chromium

CMD ["pytest", "-s", "tests/test_login.py"]