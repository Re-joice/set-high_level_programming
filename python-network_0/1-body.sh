#!/bin/bash
# Displays the response body only when the server returns a 200 status code.
curl -s -w "%{http_code}" "$1" | sed 's/200$//'
