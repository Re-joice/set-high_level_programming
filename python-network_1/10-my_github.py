#!/usr/bin/python3
"""Display the GitHub user ID using Basic Authentication."""

import requests
import sys


if __name__ == "__main__":
    response = requests.get(
        "https://api.github.com/user",
        auth=(sys.argv[1], sys.argv[2])
    )
    print(response.json().get("id"))
