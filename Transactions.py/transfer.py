import json

def transfer(number, acct_number, amount, password):
      with open("user.json", "r") as file:
            content = json.load(file)

      if number not in content:
            print("Unregistered Number")
      else:
            if password == content[number]["password"]:    
              content[number]["balance"] -= amount
              print(f"You Transfered: ${amount} to {acct_number}")

              with open("user.json", "w") as file:
                   json.dump(content, file, indent=4)
            else:
                 print("Wrong Password!") 


