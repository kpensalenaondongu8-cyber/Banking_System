import json

def withdraw(number, password, amount):
    
    with open("user.json", "r") as file:
        details = json.load(file)

        if number not in details:
            print("Unregistered number!")
        else:
            if password == details[number]["password"]:
              details[number]["balance"] -=amount
              print("Success")

              with open("user.json", "w") as file:
                  json.dump(details, file, indent=4)
            else:
                print("Incorrect password")


