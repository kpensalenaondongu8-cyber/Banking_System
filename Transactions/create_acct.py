import sqlite3
from werkzeug.security import generate_password_hash
from write_read import read
from write_read import write

def create_new(first_name, middle_name, last_name, number, password, pin):

    password_hash = generate_password_hash(password)   
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    balance = 0
    try:
        cursor.execute(
        "INSERT INTO users (first_name, middle_name, last_name, number, password_hash, pin, balance) VALUES (?, ?, ?, ?, ?, ?, ?)",
          (first_name, middle_name, last_name, number, password_hash, pin, balance) 
        )
    except  sqlite3.IntegrityError:
        print("The number:", number, "is already registered")

    conn.commit()
    conn.close()

    if __name__ == "__main__":
       create_new("Thomas", "", "Doe", "08011112222", "mypassword", "1234")