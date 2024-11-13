FruitStock = {}  # Define empty dictionary FruitStock

# Define add_fruit function for add fruit to stock, including price
def add_fruit(FruitName, FruitQty, FruitPrice):
    if FruitName in FruitStock:
        FruitStock[FruitName]['quantity'] += FruitQty
    else:
        FruitStock[FruitName] = {'quantity': FruitQty, 'price': FruitPrice}
    print(f"{FruitQty} {FruitName} added to stock at ₹{FruitPrice} per product.")

# Define view_stock function for view fruit stock
def view_stock():
    if not FruitStock:
        print("Stock is empty...")
    else:
        print("Current Stock:")
        for fruit, details in FruitStock.items():
            print(f"{fruit}: {details['quantity']} product, ₹{details['price']} per product")

# Define update_stock function for update fruit stock
def update_stock(FruitName, NewQty):
    if FruitName in FruitStock:
        FruitStock[FruitName]['quantity'] = NewQty
        print(f"Stock of {FruitName} updated to {NewQty} products.")
    else:
        print(f"{FruitName} not found in stock.")

# Define Purchase_product function for customer purchase product
def purchase_product(FruitName, FruitQty):
    if FruitName in FruitStock:
        if FruitStock[FruitName]['quantity'] >= FruitQty:
            FruitStock[FruitName]['quantity'] -= FruitQty
            print(f"{FruitQty} {FruitName}(s) purchased successfully. Total cost: ₹{FruitQty * FruitStock[FruitName]['price']}")
        else:
            print(f"Insufficient stock for {FruitName}.")
    else:
        print(f"{FruitName} not available.")

# Define view product function for viewing product list by customer
def view_product():
    if not FruitStock:
        print("No products available...")
    else:
        print("Available products:")
        for fruit, details in FruitStock.items():
            print(f"{fruit}: {details['quantity']} products, ₹{details['price']} per products")

# Main function
def main():
    while True:
        print("\tWelcome to Fruit Market")
        print("\n\n\t1. Manager")
        print("\n\t2. Customer")
        role = input("Select your Role(Manager/Customer):").lower()

        if role == "manager":
            while True:
                print("\n\tFruit Market Manager")
                print("\n\n\t1. Add Fruit Stock")
                print("\n\t2. View Fruit Stock")
                print("\n\t3. Update Fruit Stock")
                print("\n\t4. Exit")
                choice = int(input("Enter Your Choice:"))

                if choice == 1:
                    FruitName = input("Enter Fruit Name:")
                    FruitQty = int(input("Enter Fruit Quantity:"))
                    FruitPrice = float(input("Enter Fruit Price per product:"))
                    add_fruit(FruitName, FruitQty, FruitPrice)

                elif choice == 2:
                    view_stock()

                elif choice == 3:
                    FruitName = input("enter Fruit name to update:")
                    NewQty = int(input("enter new quantity:"))
                    update_stock(FruitName, NewQty)

                elif choice == 4:
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif role == "customer":
            while True:
                print("\n\tFruit Market Customer")
                print("\n\n\t1. View Products")
                print("\n\t2. Purchase Product")
                print("\n\t3. Exit")
                choice = int(input("Enter Your Choice:"))

                if choice == 1:
                    view_product()

                elif choice == 2:
                    FruitName = input("Enter Fruit Name to purchase:")
                    FruitQty = int(input("Enter Quantity:"))
                    purchase_product(FruitName, FruitQty)

                elif choice == 3:
                    break

                else:
                    print("Invalid role. Please enter 'manager' or 'customer'.")

main()