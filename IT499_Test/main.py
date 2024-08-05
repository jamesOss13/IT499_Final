import tkinter as tk
from auth import Auth
from products import ProductManager
from orders import OrderManager

class ECommerceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("E-Commerce Application")
        self.root.geometry("400x600")
        self.auth = Auth(self)
        self.product_manager = ProductManager(self)
        self.order_manager = OrderManager(self)
        self.show_login_screen()

    def show_login_screen(self):
        self.auth.show_login()

    def show_register_screen(self):
        self.auth.show_register()

    def show_product_screen(self):
        self.product_manager.show_products()

    def show_cart_screen(self):
        self.order_manager.show_cart()

    def show_checkout_screen(self):
        self.order_manager.show_shipping_info()

if __name__ == "__main__":
    root = tk.Tk()
    app = ECommerceApp(root)
    root.mainloop()
