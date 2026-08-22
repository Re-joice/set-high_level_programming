#!/usr/bin/python3
"""Fetch and display the status of the ALX intranet webpage."""

import requests


if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
