#!/usr/bin/python3
"""saving object to file"""
import json


def save_to_json_file(my_obj, filename):
    """saves jsons"""
    with open(filename, "w", encoding="utf-8") as ob_file:
        ob_file.write(json.dumps(my_obj))
