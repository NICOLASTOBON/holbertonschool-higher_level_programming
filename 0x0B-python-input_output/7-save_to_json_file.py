#!/usr/bin/python3
""" Module """
import json


def save_to_json_file(my_obj, filename):
    """ Save Object to a file """
    str_json = json.dumps(my_obj)
    with open(filename, 'w') as f:
        f.write(str_json)
    f.close()
