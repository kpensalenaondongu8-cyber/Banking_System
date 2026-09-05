import json

def view_balance(logged_in_user):
    with open("user.json", "r") as file:
        all_users = json.load(file)
        
        if logged_in_user in all_users:
            user_balance = all_users[logged_in_user]["balance"]
            print(f"Your current balance is: ₦{user_balance}")
        else:
            print("User not found.")