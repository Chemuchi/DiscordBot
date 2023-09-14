import json

with open("config.json","r") as f:
    config = json.load(f)

def owner_id():
    return config['owner_id']['id']

def guild_id():
    return config['guild_id']['id']

def cmd_prefix():
    return config['command_prefix']['value']

def delete_rule():
    return config['delete_rule']['rule']

def naver_clientid():
    return config['naver_token']['client_id']

def naver_clientsec():
    return config ['naver_token']['client_secret']

def imgur_token():
    return config ['imgur_token']['client_id']

def word_token():
    return config ['word_token']['token']