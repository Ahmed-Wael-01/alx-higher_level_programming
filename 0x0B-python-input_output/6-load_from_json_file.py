#!/usr/bin/python3
"""useless documenting"""
import json


def load_from_json_file(filename):
    """obj from json file"""
    with open(filename, "r", encoding="utf-8") as obj_file:
        return json.loads(obj_file.read())
