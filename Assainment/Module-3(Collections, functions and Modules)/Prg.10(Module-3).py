#initialise list Sample_List
Sample_List=[]

#ask to user for number of elements in list
Element_List=int(input("enter number of elements:"))

#ask to user for value of element include in list
for i in range(Element_List):
    value_list=int(input("enter numeric value for list:"))
    Sample_List.append(value_list*value_list)

#displayed first 5 and last 5 value to square of input values 
print(Sample_List[:5]+Sample_List[-5:])