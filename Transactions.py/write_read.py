import json
import os


FILE_NAME = "user.json"
def read():
    if not os.path.exists(FILE_NAME):
        return {}
        
    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def write(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)