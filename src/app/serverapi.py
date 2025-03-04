import requests
import json

servers = ["http://192.168.0.193"] ## This will need to be set from the gui - need initial setup window and settings page.

def info():
    type = "GET" # "GET"/"POST"
    path = "/printer/objects/query?toolhead=position&display_status=progress&print_stats=filename"
    return make_request(type, path)

def make_request(type, path):
    # returns {'server': {key:value}}
    retval = {}

    for server in servers:
        if type == "GET":
            response = requests.get(server + path)
        elif type == "POST":
            response = requests.post(server + path)
        retval[server] = json.loads(response.text)
    
    return retval