#define list testList
TestList=[]

#ask user to no of elements in list
Elements=int(input("enter no. of element in list:"))

#ask value for list from user
for item in range(Elements):
    Value=input("enter value for list:")
    TestList.append(Value)

print (TestList)
#convert list to set for remove duplicate values
TestList=set(TestList)



print (TestList)