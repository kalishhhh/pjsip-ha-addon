#!/bin/sh
set -e

echo "Starting PJSIP Client..."

# Run SIP service in foreground
exec python3 /app/sip_service.py
