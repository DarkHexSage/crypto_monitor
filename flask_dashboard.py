"""
Beautiful Crypto Price Dashboard
Real-time BTC, ETH, SOL prices with beautiful UI
"""

import os
from flask import Flask, render_template, jsonify, send_from_directory
import requests
from datetime import datetime
import threading
import time

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['APPLICATION_ROOT'] = os.getenv('APPLICATION_ROOT', '/')
BASE_PATH = os.getenv('APPLICATION_ROOT', '/').rstrip('/')

# Store latest prices
crypto_data = {
    'BTC': {'price': 0, 'symbol': '₿', 'change': 0},
    'ETH': {'price': 0, 'symbol': 'Ξ', 'change': 0},
    'SOL': {'price': 0, 'symbol': '◎', 'change': 0},
    'last_update': None
}

def fetch_crypto_prices():
    """Fetch real crypto prices from API"""
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        crypto_data['BTC']['price'] = data['bitcoin']['usd']
        crypto_data['BTC']['change'] = data['bitcoin']['usd_24h_change']
        
        crypto_data['ETH']['price'] = data['ethereum']['usd']
        crypto_data['ETH']['change'] = data['ethereum']['usd_24h_change']
        
        crypto_data['SOL']['price'] = data['solana']['usd']
        crypto_data['SOL']['change'] = data['solana']['usd_24h_change']
        
        crypto_data['last_update'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        print(f"✅ Updated prices at {crypto_data['last_update']}")
        return True
    except Exception as e:
        print(f"❌ Error fetching prices: {e}")
        return False

def update_prices_continuously():
    """Update prices every 30 seconds"""
    while True:
        fetch_crypto_prices()
        time.sleep(30)

# Favicon route - explicit serving for non-root paths
@app.route('/favicon.ico')
@app.route(f'{BASE_PATH}/favicon.ico')
def favicon():
    """Serve favicon.ico from static folder"""
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

@app.route('/')
@app.route(f'{BASE_PATH}/')
def index():
    """Home page - crypto dashboard"""
    return render_template('crypto_dashboard.html', api_path=f'{BASE_PATH}/api')

@app.route('/api/prices')
@app.route(f'{BASE_PATH}/api/prices')
def api_prices():
    """API endpoint for current prices"""
    return jsonify(crypto_data)

if __name__ == '__main__':
    updater = threading.Thread(target=update_prices_continuously, daemon=True)
    updater.start()
    
    fetch_crypto_prices()
    
    print(f"🚀 Crypto Dashboard running on http://localhost:5000")
    if BASE_PATH != '/':
        print(f"📍 Base path: {BASE_PATH}")
    app.run(debug=True, host='0.0.0.0', port=5000)
