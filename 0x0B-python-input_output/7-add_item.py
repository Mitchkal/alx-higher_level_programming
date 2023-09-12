#!/usr/bin/python3
"""
module 7-add_item
Script that adds arguments topython list and saves to file
save_to_jso_file - saves content to a json file
load_from_json_file - loads string from json file
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    existing_content = load_from_json_file('add_item.json')
except FileNotFoundError:
    existing_content = []

save_to_json_file(existing_content + argv[1:], 'add_item.json')
