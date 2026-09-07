from write_read import read
from write_read import write

def users_history(number):
    
    details = read()
    if number not in details:
        print("Unregistered number!")
    else:
        user_history = details[number]["history"]
        if user_history == "":
            print("You have'nt done any transaction")
        else:
            for history  in user_history:
                type = history["type"]
                amount = history["amount"]
                date = history["date"]
            print(f"Type: {type}\nAmount: {amount}\nDate: {date}")

