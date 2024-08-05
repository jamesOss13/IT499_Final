import tkinter as tk
from tkinter import messagebox
import sqlite3

class OrderManager:
    def __init__(self, app):
        self.app = app

    def show_cart(self):
        self.clear_screen()
        tk.Label(self.app.root, text="Cart", font=("Helvetica", 16)).pack(pady=20)
        conn = sqlite3.connect('ecommerce.db')
        c = conn.cursor()
        c.execute('SELECT p.name, p.price, c.quantity FROM cart c JOIN products p ON c.product_id = p.id')
        cart_items = c.fetchall()
        conn.close()
        total = 0
        for item in cart_items:
            total += item[1] * item[2]
            tk.Label(self.app.root, text=f"Product: {item[0]}, Quantity: {item[2]}, Price: ${item[1]:.2f}").pack()
        tk.Label(self.app.root, text=f"Total: ${total:.2f}").pack()
        tk.Button(self.app.root, text="Checkout", command=self.show_shipping_info, bg="lightblue").pack(pady=10)

    def show_shipping_info(self):
        self.clear_screen()
        tk.Label(self.app.root, text="Checkout - Shipping Info", font=("Helvetica", 16)).pack(pady=20)
        tk.Label(self.app.root, text="Shipping Address").pack()
        self.address_entry = tk.Entry(self.app.root)
        self.address_entry.pack()
        tk.Button(self.app.root, text="Next", command=self.show_payment_info, bg="lightblue").pack(pady=10)

    def show_payment_info(self):
        self.clear_screen()
        tk.Label(self.app.root, text="Checkout - Payment Info", font=("Helvetica", 16)).pack(pady=20)
        tk.Label(self.app.root, text="Card Number").pack()
        self.card_number_entry = tk.Entry(self.app.root)
        self.card_number_entry.pack()
        tk.Label(self.app.root, text="Expiry Date (MM/YY)").pack()
        self.expiry_date_entry = tk.Entry(self.app.root)
        self.expiry_date_entry.pack()
        tk.Label(self.app.root, text="CVV").pack()
        self.cvv_entry = tk.Entry(self.app.root, show='*')
        self.cvv_entry.pack()
        tk.Button(self.app.root, text="Place Order", command=self.place_order, bg="lightblue").pack(pady=10)

    def place_order(self):
        address = self.address_entry.get()
        card_number = self.card_number_entry.get()
        expiry_date = self.expiry_date_entry.get()
        cvv = self.cvv_entry.get()

        # Simulate payment process
        if not (card_number and expiry_date and cvv):
            messagebox.showerror("Error", "Please fill in all payment details")
            return
        
        conn = sqlite3.connect('ecommerce.db')
        c = conn.cursor()
        c.execute('SELECT p.name, p.price, c.quantity FROM cart c JOIN products p ON c.product_id = p.id')
        cart_items = c.fetchall()
        total = sum(item[1] * item[2] for item in cart_items)
        products = ', '.join([f"{item[2]} x {item[0]}" for item in cart_items])
        c.execute('INSERT INTO orders (user_id, products, total_amount, status) VALUES (?, ?, ?, ?)',
                  (1, products, total, 'Pending'))
        c.execute('DELETE FROM cart')
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Order placed successfully")
        self.app.show_product_screen()

    def clear_screen(self):
        for widget in self.app.root.winfo_children():
            widget.destroy()
