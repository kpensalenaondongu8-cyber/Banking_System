import json

def deposit (number, amount):
    with open("user.json", "r") as file:
        user_info = json.load(file)
        
        if number in user_info:
            user_info[number]["balance"] += amount
            print(f"You deposited ${amount} to your acct")
            json.dump(user_info)
        else:
            print("Unregistered Number!")
