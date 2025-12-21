# API Reference

## Configuration

### config.json

```json
{
  "name": "Project Name",
  "version": "1.0.0",
  "debug": false,
  "logging": true,
  "schedule": "daily"
}
```

## Functions

### main()
Entry point for the application.

**Usage:**
```python
from src.main import main
main()
```

## Error Handling

All errors are logged to logs.txt with full traceback.

## Logging

Logs are written to:
- Console (INFO level)
- logs.txt (DEBUG level)
