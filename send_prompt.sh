#!/bin/bash

# Read prompt from clipboard
prompt=$(pbpaste)

# Send prompt to Flask API
response=$(curl -s -X POST http://127.0.0.1:5000/api/generate \
  -H "Content-Type: application/json" \
  -d "{\"prompt\": \"$prompt\"}")

# Extract the 'response' field from JSON
generated=$(echo "$response" | /usr/bin/python3 -c "import sys, json; print(json.load(sys.stdin)['response'])")

# Copy response to clipboard
echo "$generated" | pbcopy

# Optionally: show a macOS notification
osascript -e 'display notification "Response copied to clipboard" with title "AI Reply"'

