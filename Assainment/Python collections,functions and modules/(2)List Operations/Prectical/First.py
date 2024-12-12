#create a list Demo_list
Demo_List=[1,20]

#create a list Test_list
Test_List=[1,20]

for i in range(1,6):
    #ask input for Demo_list 
    value1=input("enter value for Demo List:")
    #insert method-insert value to list at a specific index
    Demo_List.insert(i,value1)

print(Demo_List)

for i in range(6,11):
    #ask input for Test_list
    value2=input("enter value for Test List:")
    #append method-insert value to end of list
    Test_List.append(value2)
    
print(Test_List)