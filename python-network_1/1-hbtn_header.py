#!/usr/bin/python3
"""Display the X-Request-Id value from an HTTP response header."""

from sys import argv
from urllib import request


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
