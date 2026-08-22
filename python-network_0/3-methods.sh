#!/bin/bash
# Displays the HTTP methods accepted by the server at the specified URL.
curl -s -X OPTIONS -i "$1" | grep -i '^Allow:' | cut -d' ' -f2-
