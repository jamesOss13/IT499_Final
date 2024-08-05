import tkinter as tk
from tkinter import messagebox
import sqlite3

class ProductManager:
    def __init__(self, app):
        self.app = app

    def show_products(self):
        self.clear_screen()
        tk.Label(self.app.root, text="Products", font=("Helvetica", 16)).pack(pady=20)
        conn = sqlite3.connect('ecommerce.db')
        c = conn.cursor()
        c.execute('SELECT * FROM products')
        products = c.fetchall()
        conn.close()
        for product in products:
            frame = tk.Frame(self.app.root, relief=tk.RAISED, borderwidth=1)
            frame.pack(fill=tk.X, padx=5, pady=5)
            tk.Label(frame, text=f"Name: {product[1]}", font=("Helvetica", 12)).pack()
            tk.Label(frame, text=f"Description: {product[2]}", font=("Helvetica", 10)).pack()
            tk.Label(frame, text=f"Price: ${product[3]:.2f}", font=("Helvetica", 10)).pack()
            tk.Label(frame, text=f"Stock: {product[4]}", font=("Helvetica", 10)).pack()
            tk.Button(frame, text="Add to Cart", command=lambda p=product: self.add_to_cart(p), bg="lightblue").pack(pady=5)
        tk.Button(self.app.root, text="Go to Cart", command=self.app.show_cart_screen, bg="lightgreen").pack(pady=10)

    def add_to_cart(self, product):
        conn = sqlite3.connect('ecommerce.db')
        c = conn.cursor()
        c.execute('SELECT * FROM cart WHERE product_id=?', (product[0],))
        item = c.fetchone()
        if item:
            c.execute('UPDATE cart SET quantity = quantity + 1 WHERE product_id=?', (product[0],))
        else:
            c.execute('INSERT INTO cart (product_id, quantity) VALUES (?, ?)', (product[0], 1))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Added {product[1]} to cart")

    def clear_screen(self):
        for widget in self.app.root.winfo_children():
            widget.destroy()
