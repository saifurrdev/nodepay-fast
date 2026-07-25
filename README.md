# NodePay Fast ⚡

Automated **NodePay** mining ping script with high-concurrency multi-proxy support. Continuously sends ping signals to the NodePay network to maintain active mining sessions and earn rewards.

## Features

- **Multi-proxy support** — reads proxies from `proxy.txt` and rotates across them
- **High concurrency** — uses `ThreadPoolExecutor` with up to 70 workers for parallel pings
- **Cloudflare bypass** — leverages `cloudscraper` to evade Cloudflare anti-bot protection
- **Random browser ID** — generates a unique `browser_id` per request via `uuid4()`
- **Session management** — automatically fetches user session and obtains `uid` on first run
- **Real-time IP score** — displays the IP reputation score returned by the NodePay API

## Prerequisites

- Python **3.12+**
- A valid NodePay account with an authentication token (`np_token`)
- A list of proxies (HTTP/HTTPS)

## Installation

```bash
# Clone the repository
git clone https://github.com/saifurrdev/nodepay-fast.git
cd nodepay-fast

# Install dependencies
pip install requests cloudscraper
```

## Usage

1. **Prepare your proxy list** — add one proxy per line in `proxy.txt`:
   ```
   http://user:pass@1.2.3.4:8080
   http://user:pass@5.6.7.8:3128
   ```

2. **Get your `np_token`**:
   - Open [app.nodepay.ai](https://app.nodepay.ai) in your browser
   - Open Developer Console (`F12`)
   - Run: `localStorage.getItem('np_token')`
   - Copy the returned token

3. **Run the script**:
   ```bash
   python nodepay.py
   ```
   Paste your auth token when prompted. The script will loop forever, sending pings across all proxies.

## File Structure

```
nodepay-fast/
├── nodepay.py      # Main mining script
├── proxy.txt       # Proxy list (one per line)
└── README.md       # This file
```

## Configuration

| Option | Source | Description |
|--------|--------|-------------|
| Auth token | User input (stdin) | NodePay API bearer token |
| Proxies | `proxy.txt` | List of HTTP/HTTPS proxies |
| Max workers | Hardcoded (`70`) | Number of concurrent ping threads |
| API endpoints | Hardcoded in code | Session and ping URLs |

## How It Works

1. Reads all proxies from `proxy.txt`
2. Authenticates using the provided `np_token` to obtain a user `uid`
3. Spawns 70 worker threads, each continuously submitting ping requests with a random `browser_id`
4. Each ping request uses a different proxy from the list
5. Displays the IP score after each successful ping

## API Endpoints Used

- `POST https://api.nodepay.ai/api/auth/session` — session authentication
- `POST http://nw.nodepay.ai/api/network/ping` — network ping

## License

This project is provided for educational purposes. Use at your own risk.
