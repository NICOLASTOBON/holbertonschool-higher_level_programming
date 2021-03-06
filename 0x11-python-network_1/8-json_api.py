#!/usr/bin/python3
""" takes in a letter and sends a POST request """

import sys
import requests

if __name__ == "__main__":
    data = {'q': ''}
    if len(sys.argv) > 1:
        data['q'] = sys.argv[1]
    res = requests.post('http://0.0.0.0:5000/search_user', data)
    if 'json' in res.headers.get('content-type'):
        if res.json():
            print('[{}] {}'.format(
                res.json().get('id'), res.json().get('name')))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
