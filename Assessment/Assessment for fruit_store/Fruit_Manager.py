FruitStock = {}  # Define empty dictionary FruitStock

# Define add_fruit function for add fruit to stock, including price
def add_fruit(FruitName, FruitQty, FruitPrice):
    if FruitName in FruitStock:
        FruitStock[FruitName]['quantity'] += FruitQty
    else:
        FruitStock[FruitName] = {'quantity': FruitQty, 'price': FruitPrice}
    print(f"{FruitQty} {FruitName} added to stock at ₹{FruitPrice} per Fruit.")
    log_transaction('Added', FruitName,FruitQty)

# Define view_stock function for view fruit stock
def view_stock():
    if not FruitStock:
        print("Stock is empty...")
    else:
        print("Current Stock:")
        for fruit, details in FruitStock.items():
            print(f"{fruit}: {details['quantity']} Fruit, ₹{details['price']} per Fruit")
            log_transaction('viewed','All',0)


# Define update_stock function for update fruit stock
def update_stock(FruitName, NewQty):
    if FruitName in FruitStock:
        FruitStock[FruitName]['quantity'] = NewQty
        print(f"Stock of {FruitName} updated to {NewQty} Fruits.")
        log_transaction('updated',FruitName,NewQty)
    else:
        print(f"{FruitName} not found in stock.")

def log_transaction(action, fruit_name, quantity): 
    """Logs transactions to a file.""" 
    with open("transactions.log", "a") as file: 
        file.write(f"{action} {quantity} of {fruit_name}\n")