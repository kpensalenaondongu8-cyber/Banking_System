import json
from datetime import datetime 
def deposit (number, amount):
    with open("user.json", "r") as file:
        user_info = json.load(file)
        now = datetime.now()
        formatted = now.strftime("%Y-%m-%d %H:%M:%S")


        if number in user_info:
            user_info[number]["balance"] += amount
            user_info[number]["history"].append({
               "type": "deposit",
               "amount": amount,
               "date": formatted
            })
            print(f"You deposited ${amount} to your acct")

            with open("user.json", "w") as file:
             json.dump(user_info, file, indent=4)
        else:
            print("Unregistered Number!")
