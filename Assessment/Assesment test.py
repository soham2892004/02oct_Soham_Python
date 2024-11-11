#display simple message 
print("Welcome to Fruit Market...")

#display roles
print("1)Manager")
print("2)Customer")

FruitName={}
FruitQty={}
FruitPrice={}

def SelectRole():
    while True:
        choise_role=int(input("select your role(only 1 or 2):"))
        if choise_role==1 or choise_role==2:
            match choise_role:
                case 1:
                    print ("Fruit Market Manager")
                    print ("1.Add Fruit Stock")
                    print ("2.View Fruit Stock")
                    print ("3.Update Fruit Stock")
                case 2:
                    print ("Customer")
                    print ("1.Purchase Product")
            break
        else:
            print("input value is invalid,please select roll only 1 or 2..")
            

def SelectAct(choise_role):
    if choise_role==1:
        choise_Act=int(input("enter your choise for purpose(1 to 3):"))
        match choise_Act:
            case 1:
                print("Add Fruit Stock")
                AddFruit=input("Enter Fruit Name:")
                FruitName.update({AddFruit})
                AddFruitQty=input("Enter Qty(in kg):")
                FruitQty.update({AddFruitQty})
                AddFruitPrice=input("Enter Price:")
                FruitPrice.update({AddFruitPrice})

            case 2:
                print("View Fruit Stock")    
                


            case 3:
                print("Update Fruit Stock")

    












SelectRole()
SelectAct()






