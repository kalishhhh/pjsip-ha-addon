#!/bin/sh
set -e

CONFIG_DIR=/data
ACCOUNT_FILE="$CONFIG_DIR/accounts"

SERVER=$(jq -r '.server_ip' /data/options.json)
EXT=$(jq -r '.extension' /data/options.json)
PASS=$(jq -r '.password' /data/options.json)

mkdir -p "$CONFIG_DIR"

echo "sip:$EXT@$SERVER;auth_user=$EXT;auth_pass=$PASS" > "$ACCOUNT_FILE"

echo "Starting baresip..."
exec baresip -f "$CONFIG_DIR"
