#!/usr/bin/python3
"""Fetch and display the status of a web server."""

from urllib import request


if __name__ == "__main__":
    with request.urlopen("http://0.0.0.0:5050/status") as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode("utf-8"))
