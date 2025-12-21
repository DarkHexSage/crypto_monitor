# Architecture

## Overview

This project uses a simple, scalable architecture.

## Components

### main.py
- Entry point
- Orchestrates workflow
- Error handling

### config.py
- Configuration management
- Environment variables

### utils.py
- Helper functions
- Reusable code

## Data Flow

1. Load configuration
2. Initialize components
3. Run main process
4. Log results
5. Error handling

## Scalability

This design scales to:
- Higher frequencies (hourly → minute)
- More sources (API, web scraping, databases)
- Multiple destinations
- Complex transformations

## Testing

Unit tests in `tests/` directory.

Run with:
```bash
pytest
```
