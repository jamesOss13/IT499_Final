import tkinter as tk
from tkinter import messagebox
import sqlite3

class Auth:
    def __init__(self, app):
        self.app = app

    def show_login(self):
        self.clear_screen()
        tk.Label(self.app.root, text="Login", font=("Helvetica", 16)).pack(pady=20)
        tk.Label(self.app.root, text="Email").pack()
        self.email_entry = tk.Entry(self.app.root)
        self.email_entry.pack()
        tk.Label(self.app.root, text="Password").pack()
        self.password_entry = tk.Entry(self.app.root, show='*')
        self.password_entry.pack()
        tk.Button(self.app.root, text="Login", command=self.login, bg="lightblue").pack(pady=10)
        tk.Button(self.app.root, text="Register", command=self.app.show_register_screen, bg="lightgreen").pack()

    def show_register(self):
        self.clear_screen()
        tk.Label(self.app.root, text="Register", font=("Helvetica", 16)).pack(pady=20)
        tk.Label(self.app.root, text="Username").pack()
        self.username_entry = tk.Entry(self.app.root)
        self.username_entry.pack()
        tk.Label(self.app.root, text="Email").pack()
        self.email_entry = tk.Entry(self.app.root)
        self.email_entry.pack()
        tk.Label(self.app.root, text="Password").pack()
        self.password_entry = tk.Entry(self.app.root, show='*')
        self.password_entry.pack()
        tk.Button(self.app.root, text="Register", command=self.register, bg="lightblue").pack(pady=10)
        tk.Button(self.app.root, text="Login", command=self.app.show_login_screen, bg="lightgreen").pack()

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        conn = sqlite3.connect('ecommerce.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE email=? AND password=?', (email, password))
        user = c.fetchone()
        conn.close()
        if user:
            self.app.show_product_screen()
        else:
            messagebox.showerror("Error", "Invalid email or password")

    def register(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        conn = sqlite3.connect('ecommerce.db')
        c = conn.cursor()
        c.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Registration successful")
        self.app.show_login_screen()

    def clear_screen(self):
        for widget in self.app.root.winfo_children():
            widget.destroy()
