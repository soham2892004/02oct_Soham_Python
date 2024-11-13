FruitStock={}   #define empty dictionary FruitStock

#define add_fruit function for add fruit to stock
def add_fruit(FruitName,FruitQty):
    if FruitName in FruitStock:
        FruitStock[FruitName]+=FruitQty     #add Fruitname and quantity to fruitstock
    else:
        FruitStock[FruitName]=FruitQty
    print(f"{FruitQty}{FruitName} add to stock") #display message to successfully added

#define view_stock function for view fruit stock
def view_stock():
    if  not  FruitStock:
        print ("Stock is empty...")
    else:
        print ("current Stock...")
    # displayed stock fruits and its quantities
    for fruit,FruitQty in FruitStock.items():
        print (f"{fruit}:{FruitQty}")

#define update_stock function for update fruit stock
def update_stock(FruitName,NewQty):
    if FruitName in FruitStock:
        FruitStock[FruitName]=NewQty #new Quantity passed to certain fruitname a
        print (f"stock of {FruitName} updated to {NewQty}")     #after than stock is updated
    else:
        print (f"{FruitName} not found in stock")

#define Purchase_product function for customer purchase product
def purchase_product(FruitName,FruitQty):
        if FruitName in FruitStock:
            if FruitStock[FruitName] >= FruitQty:
                FruitStock[FruitName] -= FruitQty
                print(f"{FruitQty} {FruitName}(s) purchased successfully.")
            else:
                print(f"Insufficient stock for {FruitName}.")
        else:
            print(f"{FruitName} not available.")

#define view product function for viewing product list by customer
def view_product():
    if not FruitStock:
        print("no products available...")
    else:
        print("Available products...")
    for fruit,FruitQty in FruitStock.items():
        print(f"{fruit}:{FruitQty}")

#define main function it's a main part of this program 
def main():
    while True:
        print("\t Welcome to Fruit Market")
        print("\n\n\t1.Manager")
        print("\n\t2.Customer")
        #it's ask user to choose role of user
        role=input("Select your Role(Manager/Customer):").lower() #.lower used for convert input to small alphabet value

        if role=="manager":
            while True:
                print("\n\tFruit Market Manager")
                print("\n\n\t1.Add Fruit Stock")
                print("\n\t2.View Fruit Stock")
                print("\n\t3.Update Fruit Stock")
                print("\n\t4.Exit")
                #it's ask user to choose choise of action 
                choice=int(input("Enter Your Choise:"))

                if choice==1:
                    FruitName=input("Enter Fruit Name:")
                    FruitQty=int(input("Enter Fruit Quantity:"))
                    add_fruit(FruitName,FruitQty)
                
                elif choice==2:
                    view_stock()

                elif choice==3:
                    FruitName=input("enter Fruit name to update:")
                    NewQty=int(input("enter new quantity:"))
                    update_stock(FruitName,NewQty)

                elif choice==4:
                    break

                else:
                    print("invalid choice.please try again.")

        elif role=="customer":
            while True:
                print ("\n\tFruit Market Customer")
                print ("\n\n\t1.View Products")
                print ("\n\t2.Purchase Product")
                print ("\n\t3.Exit")
                #it's ask user to choose choise of action 
                choice=int(input("Enter Your Choice:"))

                if choice==1:
                    view_product()

                elif choice==2:
                    FruitName=input("Enter Fruit Name to purchase:")
                    FruitQty=int(input("Enter Quantity:"))
                    purchase_product(FruitName,FruitQty)
                
                elif choice==3:
                    break

                else:
                    print("invalid role.please enter 'manager' or 'customer'.")

main()


















