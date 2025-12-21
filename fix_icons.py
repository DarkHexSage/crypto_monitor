#!/usr/bin/env python3
"""
Quick Fix Script - Update Crypto Dashboard Icons
Replaces old icons with proper BTC, ETH, SOL icons
"""

import os

# Get the HTML file path
html_file = os.path.join(os.path.dirname(__file__), 'templates/crypto_dashboard.html')

# Read the file
with open(html_file, 'r') as f:
    content = f.read()

# OLD ICONS TO REPLACE
old_btc = '<div class="icon btc">₿</div>'
old_eth = '<div class="icon eth">Ξ</div>'
old_sol = '<div class="icon sol">◎</div>'

# NEW ICONS - PROFESSIONAL
new_btc = '<div class="icon btc" style="font-size: 2.2em; font-weight: bold; background: linear-gradient(135deg, #f7931a, #f9a825);">₿</div>'

new_eth = '''<div class="icon eth" style="background: linear-gradient(135deg, #627eea, #6f9aff); display: flex; align-items: center; justify-content: center;">
                    <svg width="45" height="45" viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 2L2.5 12L12 17.5L21.5 12L12 2Z"/>
                        <path d="M12 17.5L2.5 12L12 22L21.5 12L12 17.5Z" opacity="0.6"/>
                    </svg>
                </div>'''

new_sol = '''<div class="icon sol" style="background: #000; display: flex; align-items: center; justify-content: center; position: relative;">
                    <svg width="50" height="50" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <defs>
                            <linearGradient id="solGrad1" x1="0%" y1="0%" x2="100%">
                                <stop offset="0%" style="stop-color:#9945ff"/>
                                <stop offset="100%" style="stop-color:#14f195"/>
                            </linearGradient>
                            <linearGradient id="solGrad2" x1="0%" y1="0%" x2="100%">
                                <stop offset="0%" style="stop-color:#14f195"/>
                                <stop offset="100%" style="stop-color:#00d4ff"/>
                            </linearGradient>
                            <linearGradient id="solGrad3" x1="0%" y1="0%" x2="100%">
                                <stop offset="0%" style="stop-color:#00d4ff"/>
                                <stop offset="100%" style="stop-color:#9945ff"/>
                            </linearGradient>
                        </defs>
                        <rect x="4" y="7" width="16" height="3" rx="1.5" fill="url(#solGrad1)" transform="skewX(-15)" style="transform-origin: center"/>
                        <rect x="4" y="11" width="16" height="3" rx="1.5" fill="url(#solGrad2)" transform="skewX(-15)" style="transform-origin: center"/>
                        <rect x="4" y="15" width="16" height="3" rx="1.5" fill="url(#solGrad3)" transform="skewX(-15)" style="transform-origin: center"/>
                    </svg>
                </div>'''

# Replace in content
content = content.replace(old_btc, new_btc)
content = content.replace(old_eth, new_eth)
content = content.replace(old_sol, new_sol)

# Write back
with open(html_file, 'w') as f:
    f.write(content)

print("✅ Icons updated successfully!")
print("✓ Bitcoin icon: ₿ (golden gradient)")
print("✓ Ethereum icon: Ξ (blue diamond)")
print("✓ Solana icon: ☀️ (gradient bars)")
print()
print("Next step: python flask_dashboard.py")
print("Then visit: http://localhost:5000")