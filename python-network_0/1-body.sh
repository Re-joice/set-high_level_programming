#!/bin/bash
# Displays the response body only when the server returns a 200 status code.
curl -s -w "%{http_code}" "$1" | { read -r body; if [ "$body" = "200" ]; then printf '%s' "$body"; fi; }
