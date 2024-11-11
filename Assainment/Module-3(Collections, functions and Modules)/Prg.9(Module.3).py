#define SampleTest function
def SampleTest(list_1,list_2):
#check for loop condition ,that which item in list1,and after if condition check it's item element same as list2 any element so print true,otherwise false
 for item in list_1:
    if item in list_2:
        print ("True")
    else:
        print ("False")

#initialise list name list_1 and list_2
list_1=[]
list_2=[]

#define elements=6 ,which is input list value by user untill elements=6
elements=6

#taken value ask for user include in list1 & list2
for i in range(elements):
        value_list1=input("enter value for list:")
        list_1.append(value_list1)
        print (list_1)

for i in range(elements):
        value_list2=input("enter value for list:")
        list_2.append(value_list2)
        print (list_2)

#call function SampleTest for check common member in list_1 and List_2
SampleTest(list_1,list_2)
