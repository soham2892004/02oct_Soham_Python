#take input from user
Number=int(input("enter number:"))

#check condition when number is lower than 0 it's a negative number
if Number<0:
    print(Number,"is Negative Number")
#check condition when number is greater than 0 it's a positive number    
elif Number>0:
    print(Number,"is Positive Number")
#when upper condition's are false ,so it's a zero number
else:
    print(Number,"is Zero")