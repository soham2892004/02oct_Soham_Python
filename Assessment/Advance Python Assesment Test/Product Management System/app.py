import tkinter as tk
from tkinter import messagebox
from buisness_logic import ProductManager, Customer

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Product Management Application")
        self.root.geometry("450x450")
        self.main_menu()

    def main_menu(self):
        self.clear_frame()
        frame = tk.Frame(self.root, background="lightblue")
        frame.pack(fill="both", expand=True)
        tk.Label(frame, text="Welcome to the Product Management Application").pack(pady=10)
        tk.Button(frame, text="Product Manager", command=self.product_manager_menu).pack(pady=5)
        tk.Button(frame, text="Customer", command=self.customer_menu).pack(pady=5)

    def product_manager_menu(self):
        self.clear_frame()
        frame = tk.Frame(self.root, background="lightblue")
        frame.pack(fill="both", expand=True)
        tk.Label(frame, text="Product Manager").pack(pady=10)
        tk.Button(frame, text="Register", command=self.register_pm).pack(pady=5)
        tk.Button(frame, text="Login", command=self.login_pm).pack(pady=5)
        tk.Button(frame, text="Manage Products", command=self.manage_products_pm).pack(pady=5)
        tk.Button(frame, text="View Stocks", command=self.view_stocks_pm).pack(pady=5)
        tk.Button(frame, text="Back", command=self.main_menu).pack(pady=5)

    def customer_menu(self):
        self.clear_frame()
        frame = tk.Frame(self.root, background="lightblue")
        frame.pack(fill="both", expand=True)
        tk.Label(frame, text="Customer").pack(pady=10)
        tk.Button(frame, text="Register", command=self.register_customer).pack(pady=5)
        tk.Button(frame, text="Login", command=self.login_customer).pack(pady=5)
        tk.Button(frame, text="Purchase Stock", command=self.purchase_stock_customer).pack(pady=5)
        tk.Button(frame, text="View Orders", command=self.view_orders_customer).pack(pady=5)
        tk.Button(frame, text="Back", command=self.main_menu).pack(pady=5)

    def register_pm(self):
        self.clear_frame()
        frame = tk.Frame(self.root, background="lightblue")
        frame.pack(fill="both", expand=True)
        tk.Label(frame, text="Register Product Manager").pack(pady=10)
        username_label = tk.Label(frame, text="Username")
        username_label.pack()
        username_entry = tk.Entry(frame)
        username_entry.pack()
        password_label = tk.Label(frame, text="Password")
        password_label.pack()
        password_entry = tk.Entry(frame, show="*")
        password_entry.pack()

        def on_register():
            pm = ProductManager(username_entry.get(), password_entry.get())
            pm.register()
            messagebox.showinfo("Success", "Product Manager Registered Successfully")
            self.main_menu()

        tk.Button(frame, text="Register", command=on_register).pack(pady=5)
        tk.Button(frame, text="Back", command=self.product_manager_menu).pack(pady=5)

    def login_pm(self):
        self.clear_frame()
        frame = tk.Frame(self.root, background="lightblue")
        frame.pack(fill="both", expand=True)
        tk.Label(frame, text="Login Product Manager").pack(pady=10)
        # Add login implementation here
        tk.Button(frame, text="Back", command=self.product_manager_menu).pack(pady=5)

    def manage_products_pm(self):
        self.clear_frame()
        frame = tk.Frame(self.root, background="lightblue")
        frame.pack(fill="both", expand=True)
        tk.Label(frame, text="Manage Products").pack(pady=10)
        name_label = tk.Label(frame, text="Product Name")
        name_label.pack()
        name_entry = tk.Entry(frame)
        name_entry.pack()
        stock_label = tk.Label(frame, text="Stock")
        stock_label.pack()
        stock_entry = tk.Entry(frame)
        stock_entry.pack()
        price_label = tk.Label(frame, text="Price")
        price_label.pack()
        price_entry = tk.Entry(frame)
        price_entry.pack()

        def on_manage_products():
            pm = ProductManager("dummy", "dummy")  # Replace with actual logged-in Product Manager
            pm.manage_products(name_entry.get(), stock_entry.get(), price_entry.get())
            messagebox.showinfo("Success", "Product Added Successfully")
            self.main_menu()

        tk.Button(frame, text="Add Product", command=on_manage_products).pack(pady=5)
        tk.Button(frame, text="Back", command=self.product_manager_menu).pack(pady=5)

    def view_stocks_pm(self):
        self.clear_frame()
        frame = tk.Frame(self.root, background="lightblue")
        frame.pack(fill="both", expand=True)
        tk.Label(frame, text="Product Stocks").pack(pady=10)
        pm = ProductManager("dummy", "dummy")  # Replace with actual logged-in Product Manager
        products = pm.view_stocks()
        for product in products:
            tk.Label(frame, text=f"ID: {product['id']}, Name: {product['name']}, Stock: {product['stock']}, Price: {product['price']}").pack(pady=2)
        tk.Button(frame, text="Back", command=self.product_manager_menu).pack(pady=5)

    def register_customer(self):
        self.clear_frame()
        frame = tk.Frame(self.root, background="lightblue")
        frame.pack(fill="both", expand=True)
        tk.Label(frame, text="Register Customer").pack(pady=10)
        username_label = tk.Label(frame, text="Username")
        username_label.pack()
        username_entry = tk.Entry(frame)
        username_entry.pack()
        password_label = tk.Label(frame, text="Password")
        password_label.pack()
        password_entry = tk.Entry(frame, show="*")
        password_entry.pack()

        def on_register():
            customer = Customer(username_entry.get(), password_entry.get())
            customer.register()
            messagebox.showinfo("Success", "Customer Registered Successfully")
            self.main_menu()

        tk.Button(frame, text="Register", command=on_register).pack(pady=5)
        tk.Button(frame, text="Back", command=self.customer_menu).pack(pady=5)

    def login_customer(self):
        self.clear_frame()
        frame = tk.Frame(self.root, background="lightblue")
        frame.pack(fill="both", expand=True)
        tk.Label(frame, text="Login Customer").pack(pady=10)
        # Add login implementation here
        tk.Button(frame, text="Back", command=self.customer_menu).pack(pady=5)

    def purchase_stock_customer(self):
        self.clear_frame()
        frame = tk.Frame(self.root, background="lightblue")
        frame.pack(fill="both", expand=True)
        tk.Label(frame, text="Purchase Stock").pack(pady=10)
        product_id_label = tk.Label(frame, text="Product ID")
        product_id_label.pack()
        product_id_entry = tk.Entry(frame)
        product_id_entry.pack()
        quantity_label = tk.Label(frame, text="Quantity")
        quantity_label.pack()
        quantity_entry = tk.Entry(frame)
        quantity_entry.pack()

        def on_purchase_stock():
            customer = Customer("dummy", "dummy")  # Replace with actual logged-in Customer
            customer.purchase_stock(product_id_entry.get(), quantity_entry.get())
            messagebox.showinfo("Success", "Stock Purchased Successfully")
            self.main_menu()

        tk.Button(frame, text="Purchase", command=on_purchase_stock).pack(pady=5)
        tk.Button(frame, text="Back", command=self.customer_menu).pack(pady=5)

    def view_orders_customer(self):
        self.clear_frame()
        frame = tk.Frame(self.root, background="lightblue")
        frame.pack(fill="both", expand=True)
        tk.Label(frame, text="View Orders").pack(pady=10)
        customer = Customer("dummy", "dummy")  # Replace with actual logged-in Customer
        orders = customer.view_orders()
        for order in orders:
            tk.Label(frame, text=f"Order ID: {order['id']}, Product ID: {order['product_id']}, Quantity: {order['quantity']}, Total Price: {order['total_price']}").pack(pady=2)
        tk.Button(frame, text="Back", command=self.customer_menu).pack(pady=5)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
