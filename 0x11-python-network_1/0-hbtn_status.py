#!/usr/bin/python3
"""  Python script that fetch url """

import urllib.request as url


if __name__ == "__main__":
    with url.urlopen('https://intranet.hbtn.io/status') as response:
        status = response.read()
        print('Body response:')
        print('\t - type: {}'.format(type(status)))
        print('\t - content: {}'.format(status))
        print('\t - utf8 content: {}'.format(status.decode('utf8')))
