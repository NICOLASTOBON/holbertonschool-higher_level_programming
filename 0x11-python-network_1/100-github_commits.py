#!/usr/bin/python3
"""  script that takes 2 arguments in order to solve this challenge """

import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(
        'https://api.github.com/repos/{}/{}/commits'
        .format(argv[2], argv[1]))

    res = response.json()

    i = 0
    while i < 9:
        print(
            res[i].get('sha'),
            res[i].get('commit').get('author').get('name'))
        i += 1
