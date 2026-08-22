#!/usr/bin/python3
"""Fetch a URL and display its body or HTTP error code."""

import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
