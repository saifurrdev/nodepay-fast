# nodepay-fast

Automated NodePay mining ping script with multi-proxy support. Uses `np_token` authentication and cloudscraper for requests.

## Usage

1. Add proxies to `proxy.txt` (one per line)
2. Get your `np_token` from NodePay dashboard (browser console: `localStorage.getItem('np_token')`)
3. Run the script:

```bash
python nodepay.py
```

## Requirements

- Python 3.12+
- `cloudscraper`

## Files

| File | Purpose |
|------|---------|
| `nodepay.py` | Main mining script |
| `proxy.txt` | Proxy list (one per line) |
