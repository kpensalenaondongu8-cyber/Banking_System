import sqlite3
from datetime import datetime

def withdraw(number, pin, amount):
    
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()

    now = datetime.now()
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")

    if number not in details:
        print("Unregistered number!")
    else:
        if pin == details[number]["pin"]:
            details[number]["balance"] -=amount
            details[number]["history"].append({
                "type": "withdraw",
                "amount": amount,
                "Date": formatted
            })
            print("Success")
            write(details)     
        else:
            print("Incorrect password")


