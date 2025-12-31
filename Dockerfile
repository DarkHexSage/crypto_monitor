FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY src ./src
COPY flask_dashboard.py .
COPY templates ./templates
COPY fix_icons.py .
COPY config.example.json ./config.json

# Create data directory
RUN mkdir -p data logs

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('https://adragportfolio.info.gf/crypto-monitor/api/prices').read()"

# Run Flask app
CMD ["python", "flask_dashboard.py"]
