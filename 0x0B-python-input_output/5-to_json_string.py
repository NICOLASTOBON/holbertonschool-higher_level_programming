#!/usr/bin/python3
""" Module """
import json


def to_json_string(my_obj):
    """ To JSON string """
    to_json = json.dumps(my_obj)
    return to_json
