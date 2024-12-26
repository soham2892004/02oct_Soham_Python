FruitStock = {}  # Define empty dictionary FruitStock


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
        print("No Fruits available...")
    else:
        print("Available Fruits:")
        for fruit, details in FruitStock.items():
            print(f"{fruit}: {details['quantity']} Fruits, ₹{details['price']} per Fruits")