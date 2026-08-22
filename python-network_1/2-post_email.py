#!/usr/bin/python3
"""Send an email as a POST parameter and display the response body."""

from sys import argv
from urllib import parse, request


if __name__ == "__main__":
    data = parse.urlencode({"email": argv[2]}).encode("utf-8")
    with request.urlopen(argv[1], data=data) as response:
        print(response.read().decode("utf-8"))
