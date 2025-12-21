# Setup Guide

## Installation

### Prerequisites
- Python 3.8+
- pip

### Steps

1. **Clone repository**
   ```bash
   git clone <repo-url>
   cd python-automation-portfolio
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure project**
   ```bash
   cd projects/[project-name]
   cp config.example.json config.json
   ```

4. **Edit config.json**
   - Add API keys if needed
   - Configure schedule
   - Set logging preferences

5. **Run**
   ```bash
   python src/main.py
   ```

## Configuration

See config.json for all options.

## Troubleshooting

### Import errors
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (must be 3.8+)

### Config errors
- Verify config.json is valid JSON
- Check file paths are correct
- Ensure required keys exist

### Runtime errors
- Check logs in logs.txt
- Verify internet connection for API calls
- Check API credentials if used
