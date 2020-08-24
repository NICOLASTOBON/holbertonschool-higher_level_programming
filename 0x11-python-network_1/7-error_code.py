#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the response """

import sys
import requests

if __name__ == "__main__":
    err = requests.get(sys.argv[1])
    if err.status_code >= 400:
        print('Error code: {}'.format(err.status_code))
    else:
        print(err.text)
