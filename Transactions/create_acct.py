import sqlite3
from werkzeug.security import generate_password_hash

def create_new(first_name, middle_name, last_name, number, password, pin):
    print("Starting create_new for", number)
    password_hash = generate_password_hash(password)
    print("Password hashed")

    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    print("Connected, cursor ready")

    balance = 0
    try:
        cursor.execute(
            "INSERT INTO users (first_name, middle_name, last_name, number, password_hash, pin, balance) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (first_name, middle_name, last_name, number, password_hash, pin, balance)
        )
        print("Insert executed")
    except sqlite3.IntegrityError:
        print("The number:", number, "is already registered")

    conn.commit()
    print("Committed")
    conn.close()
    print("Closed")

if __name__ == "__main__":
    create_new("Thomas", "", "Doe", "08011112222", "mypassword", "1234")