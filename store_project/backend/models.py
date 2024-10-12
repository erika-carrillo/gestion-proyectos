import sqlite3

def get_db_connetion():
    conn = sqlite3.connect("store.db")
    conn.row_factory = sqlite3.Row
    return conn

def get_products():
    conn = get_db_connetion()
    products = conn.execute("SELECT * FROM products")

    conn.close()
    return products
def add_product(name, descripcion, price, stock):
    conn = get_db_connetion()
    conn.execute(
        "INSERT INTO products(name, descripcion, price, stock) VALUES (?,?,?,?)",(name, descripcion, price, stock)
    )
    conn.commit()
    conn.close()
