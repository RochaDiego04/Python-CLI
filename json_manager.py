'''
If the .json file doesn't exist, it will be created, 
otherwise we will just read it
'''

import json
import os

def read_json():
    if not os.path.isfile('data.json'):
        with open('data.json','w') as f:
            json.dump([], f)
    with open('data.json','r') as f:
        data = json.load(f)
    return data

def write_json():
    pass