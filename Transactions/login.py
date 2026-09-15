import sqlite3
from werkzeug.security import check_password_hash

def user_login(number, password):

   conn = sqlite3.connect("app.db")
   cursor = conn.cursor()
    
   cursor.execute("SELECT id, password_hash FROM users WHERE number = ?", (number,))
   row = cursor.fetchone()
   conn.close()

   if row is None:
      print("No account with that number")
      return False
   
   stored_hash = row[1]
   stored_id = row[0]
   if check_password_hash(stored_hash, password):
      print("Login succesful")
      return stored_id
   else:
      print("Wrong password")
      return False   

if __name__ == "__main__":
    print(user_login("08011112222", "mypassword"))   
    print(user_login("08011112222", "wrongpassword"))
    print(user_login("09999999999", "anything"))     