#create empty list
Fruit_List=[]


for i in range(1,11):
    #fruit name ask by user
    Fruit_Name=input("Enter Fruit Name:")
    #fruit name add to fruit list
    Fruit_List.append(Fruit_Name)

#length of list fruit list
Result_length=len(Fruit_List)

#displayed length of list
print ("length of list:",Result_length)