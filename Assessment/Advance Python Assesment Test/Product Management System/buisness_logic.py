import setup_database
import pymysql

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class ProductManager(User):
    def register(self):
        try:
            connection = setup_database.get_connection()
            with connection.cursor() as cursor:
                sql = "INSERT INTO product_manager (username, password) VALUES (%s, %s)"
                cursor.execute(sql, (self.username, self.password))
            connection.commit()
            print("Product Manager registered successfully!")
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
        finally:
            connection.close()

    def login(self):
        # Implement login logic
        pass

    def manage_products(self):
        try:
            connection = setup_database.get_connection()
            with connection.cursor() as cursor:
                # Example product management: adding a product
                product_name = input("Enter product name: ")
                product_stock = int(input("Enter product stock: "))
                product_price = float(input("Enter product price: "))
                sql = "INSERT INTO product (name, stock, price) VALUES (%s, %s, %s)"
                cursor.execute(sql, (product_name, product_stock, product_price))
            connection.commit()
            print("Product added successfully!")
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
        finally:
            connection.close()

    def view_stocks(self):
        try:
            connection = setup_database.get_connection()
            with connection.cursor() as cursor:
                sql = "SELECT * FROM product"
                cursor.execute(sql)
                products = cursor.fetchall()
                for product in products:
                    print(f"ID: {product['id']}, Name: {product['name']}, Stock: {product['stock']}, Price: {product['price']}")
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
        finally:
            connection.close()

class Customer(User):
    def __init__(self, username, password, balance=0.0):
        super().__init__(username, password)
        self.__balance = balance

    def register(self):
        try:
            connection = setup_database.get_connection()
            with connection.cursor() as cursor:
                sql = "INSERT INTO customer (username, password, balance) VALUES (%s, %s, %s)"
                cursor.execute(sql, (self.username, self.password, self.__balance))
            connection.commit()
            print("Customer registered successfully!")
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
        finally:
            connection.close()

    def login(self):
        # Implement login logic
        pass

    def purchase_stock(self):
        try:
            connection = setup_database.get_connection()
            with connection.cursor() as cursor:
                product_id = int(input("Enter product ID: "))
                quantity = int(input("Enter quantity to purchase: "))
                sql = "SELECT * FROM product WHERE id = %s"
                cursor.execute(sql, (product_id,))
                product = cursor.fetchone()
                if product:
                    total_price = product['price'] * quantity
                    if product['stock'] >= quantity:
                        # Check if customer has enough balance
                        if self.__balance >= total_price:
                            # Update product stock
                            new_stock = product['stock'] - quantity
                            sql = "UPDATE product SET stock = %s WHERE id = %s"
                            cursor.execute(sql, (new_stock, product_id))

                            # Update customer balance
                            self.__balance -= total_price
                            sql = "UPDATE customer SET balance = %s WHERE username = %s"
                            cursor.execute(sql, (self.__balance, self.username))

                            # Insert order record
                            sql = "INSERT INTO orders (customer_id, product_id, quantity, total_price) VALUES (%s, %s, %s, %s)"
                            cursor.execute(sql, (self.id, product_id, quantity, total_price))

                            connection.commit()
                            print("Purchase successful!")
                        else:
                            print("Insufficient balance.")
                    else:
                        print("Insufficient stock.")
                else:
                    print("Product not found.")
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
        finally:
            connection.close()

    def view_orders(self):
        try:
            connection = setup_database.get_connection()
            with connection.cursor() as cursor:
                sql = "SELECT * FROM orders WHERE customer_id = %s"
                cursor.execute(sql, (self.id,))
                orders = cursor.fetchall()
                for order in orders:
                    print(f"Order ID: {order['id']}, Product ID: {order['product_id']}, Quantity: {order['quantity']}, Total Price: {order['total_price']}")
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
        finally:
            connection.close()
