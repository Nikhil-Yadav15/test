# vuln-lab (Local Security Lab)

## What this contains
- A tiny intentionally vulnerable Flask app on port **5000** with a simple SQL injection vulnerability.
- A WordPress instance (official image) on port **8080** with MySQL (for use with WPScan).

## WARNING / LEGAL
Run this **only** on your local machine or an isolated lab VM that you own. Do NOT scan or attack systems you don't own or have permission to test.

## Run the lab
1. Build and start everything:
   ```bash
   docker compose up --build
