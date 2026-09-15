import sqlite3 
from datetime import datetime

def deposit (number, pin, amount):
     conn = sqlite3.connect("app.db")
     cursor = conn.cursor()  

     cursor.execute("SELECT id, pin FROM users WHERE number = ?", (number,))
     row = cursor.fetchone()
    
     
     if row == None:
          print("Number not registered")
     else:
          stored_pin = row[1]
          if stored_pin == pin:
               cursor.execute(
                    "SELECT balance FROM users WHERE pin = ?", (pin, )
               )        
               result = cursor.fetchone() 
               new_balance = result[0] + amount
               cursor.execute(
                    "UPDATE users SET balance = ? WHERE id = ?",
                    (new_balance, id)
               )

               now = datetime.now()
               formatted = now.strftime("%Y-%m-%d %H:%M:%S")
               transac_type = "deposit"
               cursor.execute(
                    "INSERT INTO history transac_type, transac_amount, created_at, (VALUES) ?, ?, ?",
                    (transac_type, amount, formatted)
               )
               print(f"Deposited: {amount} to {number}")
          else:
               print("Incorrect pin")
     conn.commit()
     conn.close()          