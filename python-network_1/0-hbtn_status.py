#!/usr/bin/python3
"""Fetch and display the status of the ALX intranet webpage."""

from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode("utf-8"))
