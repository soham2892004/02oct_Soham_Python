#create function addition
def Addition(value1,value2):
    print("Addition=",value1+value2)

#create function substraction
def Substraction(value1,value2):
    print("substraction=",value2-value1)

#create function Multiplication
def Multiplication(value1,value2):
    print("Multiplication=",value1*value2)

#create function Division
def Division(value1,value2):
    print("division=",value2//value1)

#take input value 1 and value 2
value1=int(input("enter value.1:"))
value2=int(input("enter value.2:"))

#call function addition,substraction,multiplication,division
Addition(value1,value2)
Substraction(value1,value2)
Multiplication(value1,value2)
Division(value1,value2)