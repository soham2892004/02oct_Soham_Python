#define list DemoList
TestList=[]

#ask user to no of elements in list
Elements=int(input("enter no. of element in list:"))

#ask value for list from user
for item in range(Elements):
    Value=input("enter value for list:")
    TestList.append(Value)

#it's sort method which is sorting list to ascending order
TestList.sort()

#displayed second smallest number to list
print (TestList[1])