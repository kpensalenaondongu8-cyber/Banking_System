import json

def create_new(first_name, middle_name, last_name, number, password, pin):
    with open("user.json", "r") as file:
        new_user = json.load(file)
    
    balance = 0
    history = []
    new_user[number] = {
        "first_name": first_name,
        "middle_name": middle_name,
        "last_name": last_name,
        "number": number,
        "password": password,
        "balance": balance,
        "pin": pin,
        "history": history
    }
    with open("user.json", "w") as file:
        json.dump(new_user, file, indent=4)