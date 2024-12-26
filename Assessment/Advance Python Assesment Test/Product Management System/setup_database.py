import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",  
        database="productmanagement",
        cursorclass=pymysql.cursors.DictCursor
    )

def create_tables():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            
            
            
            cursor.execute("CREATE TABLE  product_manager (id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(50) NOT NULL,password VARCHAR(100) NOT NULL)")
            
            # Create Customer table
            cursor.execute("CREATE TABLE customer (id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(50) NOT NULL,password VARCHAR(100) NOT NULL,balance DECIMAL(10, 2) DEFAULT 0.00)")
            
            # Create Product table
            cursor.execute("CREATE TABLE product (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100) NOT NULL,stock INT NOT NULL,price DECIMAL(10, 2) NOT NULL)")
            
            # Create Orders table
            cursor.execute("CREATE TABLE orders (id INT AUTO_INCREMENT PRIMARY KEY,customer_id INT,product_id INT,quantity INT,total_price DECIMAL(10, 2),FOREIGN KEY (customer_id) REFERENCES customer(id),FOREIGN KEY (product_id) REFERENCES product(id))")
        
        connection.commit()
        print("Database and tables created successfully!")
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    create_tables()
