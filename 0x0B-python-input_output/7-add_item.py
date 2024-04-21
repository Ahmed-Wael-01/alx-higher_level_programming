#!/usr/bin/python3
"""document again and again and again"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

a_list = list(sys.argv[1:])

try:
    recent_data = load_from_json_file("add_item.json")
except Exception:
    recent_data = []

new_data = recent_data + a_list

save_to_json_file(new_data, "add_item.json")
