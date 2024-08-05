import sqlite3

def create_tables():
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    price REAL NOT NULL,
                    stock INTEGER NOT NULL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    products TEXT NOT NULL,
                    total_amount REAL NOT NULL,
                    status TEXT NOT NULL,
                    FOREIGN KEY(user_id) REFERENCES users(id))''')
    c.execute('''CREATE TABLE IF NOT EXISTS cart (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER NOT NULL,
                    quantity INTEGER NOT NULL,
                    FOREIGN KEY(product_id) REFERENCES products(id))''')

    # Insert initial products
    products = [
        ('Laptop', 'A high performance laptop', 999.99, 10),
        ('Smartphone', 'A latest model smartphone', 699.99, 20),
        ('Headphones', 'Noise-cancelling headphones', 199.99, 30),
        ('Smartwatch', 'A smartwatch with various features', 149.99, 25),
        ('Tablet', 'A tablet with a large screen', 299.99, 15)
    ]
    c.executemany('INSERT INTO products (name, description, price, stock) VALUES (?, ?, ?, ?)', products)
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
