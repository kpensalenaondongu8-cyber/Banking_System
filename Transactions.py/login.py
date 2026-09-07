import json

def user_login(number, password):

    with open("user.json", "r") as file:       
        login_details = json.load(file)

        if number not in login_details:
            print("Number Not registered")
        else:                         
            if password == login_details[number]["password"]:
                print("Login Succesfully")
            else:
                print("Wrong Password!")           
            
