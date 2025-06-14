#!/bin/bash

# Build valid JSON from clipboard contents
payload=$(pbpaste | jq -Rs '{prompt: .}')

# Default endpoint (can be changed by passing argument)
endpoint="${1:-generate-code}"

# Send prompt to Flask API
response=$(curl -s -X POST http://127.0.0.1:5000/api/$endpoint \
  -H "Content-Type: application/json" \
  -d "$payload")

# Extract the 'response' field from JSON safely
generated=$(echo "$response" | /usr/bin/python3 -c "
import sys, json
data = json.load(sys.stdin)
print(data.get('response') or f'ERROR: {data.get(\"error\", \"Unknown error\")}')")

# Copy result to clipboard
echo "$generated" | pbcopy


