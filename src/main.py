"""
Crypto Price Monitor - REAL VERSION
Fetches actual Bitcoin/Ethereum prices from API
"""

import requests
import csv
import logging
from datetime import datetime
import json
import os

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs.txt'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def load_config():
    """Load config"""
    with open('config.json') as f:
        return json.load(f)

def fetch_crypto_prices():
    """Fetch REAL crypto prices from API"""
    logger.info("Fetching crypto prices from API...")
    
    try:
        # Call real API
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Extract prices
        btc_price = data['bitcoin']['usd']
        eth_price = data['ethereum']['usd']
        timestamp = datetime.now().isoformat()
        
        logger.info(f"✅ Bitcoin: ${btc_price:,.2f}")
        logger.info(f"✅ Ethereum: ${eth_price:,.2f}")
        
        # Save to CSV
        csv_exists = os.path.exists('prices.csv')
        
        with open('prices.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            
            # Write header if new file
            if not csv_exists:
                writer.writerow(['Timestamp', 'Bitcoin (USD)', 'Ethereum (USD)'])
            
            # Write data
            writer.writerow([timestamp, btc_price, eth_price])
        
        logger.info(f"✅ Saved to prices.csv")
        return {'btc': btc_price, 'eth': eth_price, 'timestamp': timestamp}
        
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        raise

def main():
    """Main function"""
    logger.info("=" * 60)
    logger.info("Starting Crypto Price Monitor")
    logger.info("=" * 60)
    
    try:
        config = load_config()
        logger.info(f"✅ Config loaded: {config['name']}")
        
        # Fetch prices
        result = fetch_crypto_prices()
        
        logger.info("=" * 60)
        logger.info("✅ Process completed successfully!")
        logger.info("=" * 60)
        
        return result
        
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    main()
