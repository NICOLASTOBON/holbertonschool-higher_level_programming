#!/usr/bin/python3
""" takes in a URL and an email address, sends a POST request """

import sys
import requests

if __name__ == "__main__":
    pos = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(pos.text)
