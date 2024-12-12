#create empty list1 & list2
List1=[]
List2=[]

for i in range(1,11):
    
    #ask input from user for list1
    Value_List1=input("enter value for list 1:")
    
    #insert value of list1 in list1
    List1.insert(i,Value_List1)
    
    #sort the list using sort() 
    List1.sort()
    


for i in range(1,11):
    #ask input from user for list2
    Value_List2=input("enter value for list 2:")

    #insert value of list2 in list2
    List2.insert(i,Value_List2)

    #create a sorted list using sorted()
    Sorted_list=sorted(List2)

print (List1)

print(Sorted_list)

