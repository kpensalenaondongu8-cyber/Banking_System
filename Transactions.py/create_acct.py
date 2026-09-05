import json

def create_new(first_name, middle_name, last_name, number, password):
    with open("user.json", "r") as file:
        new = json.load(file)
    

    with open("user.json", "w") as file:
        json.dump(new, file, indent=4)