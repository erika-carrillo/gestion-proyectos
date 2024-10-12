import sqlite3

def create_database():
    conn = sqlite3.connet("store.db")
    with open ("schema.sql","r") as f:
        conn.executescript(f.read())
    conn.close()
if __name__ == "__main__":
            create_database()
            