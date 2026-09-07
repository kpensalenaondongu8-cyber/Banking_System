import json
from datetime import datetime
from write_read import read
from write_read import write

def transfer(number, acct_number, amount, pin):
      content = read()
      now = datetime.now()
      formatted = now.strftime("%Y-%m-%d %H:%M:%S")

      if number not in content:
            print("Unregistered Number")
      else:
            if pin == content[number]["pin"]:    
              content[number]["balance"] -= amount
              content[number]["history"].append({
                   "type": "transfer",
                   "amount": amount,
                   "Date": formatted
              })
              write(content)
              print(f"You Transfered: ${amount} to {acct_number}")
            else:
                 print("Wrong Password!") 


