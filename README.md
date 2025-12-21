# Crypto Price Monitor

> Real-time cryptocurrency price tracker | Live Bitcoin, Ethereum, Solana | Production-ready

![Status](https://img.shields.io/badge/status-production%20ready-brightgreen)
![Docker](https://img.shields.io/badge/docker-available-blue)
![Python](https://img.shields.io/badge/python-3.11+-blue)
![API](https://img.shields.io/badge/api-free-orange)

## Overview

Crypto Price Monitor displays **real-time cryptocurrency prices** from the free CoinGecko API with a beautiful, professional dashboard. Perfect for traders, investors, and platforms needing live crypto data.

## ✨ Features

- **Real-time Prices** - Live Bitcoin, Ethereum, Solana prices
- **24h Change Tracking** - Green/red indicators for price movement
- **Beautiful Dashboard** - Professional UI with gradient design
- **Auto-refresh** - Updates every 30 seconds automatically
- **Responsive Design** - Works on desktop, tablet, mobile
- **Free API** - Uses CoinGecko (unlimited, no auth needed)
- **REST API** - Easy integration endpoints
- **Production Ready** - Error handling, logging included
- **Fully Containerized** - Docker support

Use Cases

**Applications:**
- Trading dashboards
- Investment portfolio tracking
- Price analysis platforms
- Embedded crypto widgets
- SaaS crypto features
- Educational platforms


## 🚀 Quick Start

### Local Setup (5 minutes)

```bash
# Install dependencies
pip install -r requirements.txt

# Start dashboard
python flask_dashboard.py
```

Open http://localhost:5000

### Docker Setup

```bash
# Build image
docker build -t crypto_monitor:1.0 .

# Run container
docker run -p 5000:5000 crypto_monitor:1.0

# View logs
docker logs <container_id>
```

## 📚 Usage

### View Dashboard

Open http://localhost:5000 to see:
- Live BTC, ETH, SOL prices in USD
- 24-hour % change (↑ green, ↓ red)
- Price direction indicators
- Last update timestamp
- Auto-refreshes every 30 seconds


## 🏗️ Architecture

**Tech Stack:**
- Backend: Python Flask + Threading
- API: CoinGecko (free, unlimited)
- Frontend: HTML5 + CSS3 + JavaScript
- Storage: JSON (in-memory)
- Deployment: Docker

**Data Flow:**
```
CoinGecko API → Background Thread → Flask App → Web Dashboard
(every 30s)       (price updates)     (REST)      (real-time)
```

## 🔧 Configuration

### Add More Cryptocurrencies

Edit `flask_dashboard.py`:
```python
crypto_data = {
    'BTC': {...},
    'ETH': {...},
    'SOL': {...},
    'XRP': {...},      # Add XRP
    'DOGE': {...},     # Add Dogecoin
}

# Update API call:
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,ripple,dogecoin&vs_currencies=usd&include_24hr_change=true"
```

### Change Update Interval

In `flask_dashboard.py`:
```python
time.sleep(30)  # Change to 60 for every minute
```

### Support Multiple Currencies

```python
# Show prices in EUR, GBP, JPY
url = "...&vs_currencies=usd,eur,gbp,jpy"
```

## 📊 API Endpoints

### Get Current Prices
```bash
curl http://localhost:5000/api/prices
```

Response:
```json
{
  "BTC": {"price": 89453.50, "change": 2.45},
  "ETH": {"price": 3040.98, "change": -1.32},
  "SOL": {"price": 189.25, "change": 3.18},
  "last_update": "2025-12-21T17:30:00"
}
```

### Get Single Price
```bash
curl http://localhost:5000/api/price/BTC
```

### Get Price History
```bash
curl http://localhost:5000/api/history/BTC
```

## 🐳 Docker

### Build Image
```bash
docker build -t crypto_monitor:1.0 .
```

### Run Container
```bash
docker run -p 5000:5000 crypto_monitor:1.0
```

### With Volume Mounting
```bash
docker run -p 5000:5000 \
  -v $(pwd)/prices.csv:/app/prices.csv \
  crypto_monitor:1.0
```

## 🧪 Testing

```bash
# Install test dependencies
pip install pytest

# Run tests
pytest tests/ -v

# Test API endpoints
curl http://localhost:5000/api/prices
```

## 📝 License

MIT - Free to use and modify

---
