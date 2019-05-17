#!/usr/local/bin/python3

import requests
import getpass
import json
import os.path

token = open(".key")
#token = getpass.getpass("Slack API Token: ")

token_array = {'token': token}
r = requests.get('https://slack.com/api/users.list', params=token_array)

response_json = r.text
response = json.loads(response_json)

def print_dict(dict):
    for key, value in dict.items():
        print(key, value, sep=" - ")

def diff(first, second):
    value = { k : first[k] for k in set(first) - set(second) }
    return value

if 'error' in response.keys():
    print("Invalid API Token")
    exit()

members = response['members']

deleted_accounts = {}
added_accounts = {}

for member in members:
    if member["deleted"]:
        deleted_accounts[member['profile']['real_name']] = member['profile']['title']
    else:
        added_accounts[member['profile']['real_name']] = member['profile']['title']

if os.path.exists("slackdiff.json"):
    file_read = open("slackdiff.json", "r")
    file_contents = []
    for line in file_read:
        file_contents.append(line)
    old_list_removed = json.loads(file_contents[0
    ])
    old_list_added = json.loads(file_contents[1])
    file_read.close()

    removed_diff = (diff(deleted_accounts, old_list_removed))
    added_diff = (diff(added_accounts, old_list_added))
    
    print("Removed Accounts:")
    print_dict(removed_diff)
    print()
    print("Added Accounts:")
    print_dict(added_diff)
else:
    print("No Json file found, will work on subsequent runs.")

file_write_remove = open("slackdiff.json", "w+")
file_write_remove.write(json.dumps(deleted_accounts))
file_write_remove.write("\n")
file_write_remove.write(json.dumps(added_accounts))

file_write_remove.close()
