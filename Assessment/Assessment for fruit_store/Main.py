import Fruit_Manager
import customer


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
                    FruitPrice = float(input("Enter Fruit Price per Fruit:"))
                    Fruit_Manager.add_fruit(FruitName, FruitQty, FruitPrice)

                elif choice == 2:
                    Fruit_Manager.view_stock()

                elif choice == 3:
                    FruitName = input("enter Fruit name to update:")
                    NewQty = int(input("enter new quantity:"))
                    Fruit_Manager.update_stock(FruitName, NewQty)

                elif choice == 4:
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif role == "customer":
            while True:
                print("\n\tFruit Market Customer")
                print("\n\n\t1. View Products")
                print("\n\t2. Purchase Fruit")
                print("\n\t3. Exit")
                choice = int(input("Enter Your Choice:"))

                if choice == 1:
                    customer.view_product()

                elif choice == 2:
                    FruitName = input("Enter Fruit Name to purchase:")
                    try:
                        FruitQty = int(input("Enter Quantity:"))
                        customer.purchase_product(FruitName, FruitQty)
                        return FruitName,FruitQty
                    except Exception as e:
                        print ("error occured!")

                elif choice == 3:
                    break

                else:
                    print("Invalid role. Please enter 'manager' or 'customer'.")

main()

f1=open('Fruit_Store.txt','a')
f1.write(f"{main}")
