import sqlite3

DB_NAME = "app.db"

def init_db():
    print("Starting init_db...")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    print("Connected")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            middle_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            number TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            balance INTEGER NOT NULL,
            pin TEXT NOT NULL       
        )
    """)
    print("Table created")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            transac_type TEXT NOT NULL,
            transac_amount INTEGER NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)

    conn.commit()
    print("Committed")
    conn.close()
    print("Closed")

if __name__ == "__main__":
    init_db()