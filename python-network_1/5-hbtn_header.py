#!/usr/bin/python3
"""Display the X-Request-Id value from an HTTP response header."""

import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
