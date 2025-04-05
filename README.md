# Beam Analytics (FastAPI)

A lightweight redirect service that captures UTM parameters and logs them.

## How to Use

Visit a URL like:
```
/track?redirect=https://example.com&utm_source=google&utm_medium=cpc&utm_campaign=spring
```

The service will:
1. Log the click (including IP and user agent).
2. Redirect the user to the final destination.
