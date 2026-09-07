from write_read import read

def view_balance(number, password):
        all_users = read()
        if number not in all_users:
            print("User not found.")
        else:
            if password == all_users[number]["password"]:      
              user_balance = all_users[number]["balance"]
              print(f"Your current balance is: ${user_balance}")
            else:
                print("incorrect Password!")  

           