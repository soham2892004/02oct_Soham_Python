#define list DemoList
DemoList=[]

#ask user to no of elements in list
ElementList=int(input("enter no. of element in list:"))

#ask value for list from user
for item in range(ElementList):
    Value=input("enter value for list:")
    DemoList.append(Value)

#import random module
import random

#displayed randomly selected value
print (random.choice(DemoList))

