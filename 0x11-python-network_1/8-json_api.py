#!/usr/bin/python3
"""
    python script to fetch given website
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    r = requests.post(
            'http://0.0.0.0:5000/search_user',
            data={'q': q})
    try:
        res_dict = r.json()
        if len(res_dict) == 0:
            print("No result")
        else:
            print("[{}] {}".format(
                res_dict.get('id'), res_dict.get('name')))
    except Exception as e:
        print("Not a valid JSON")
