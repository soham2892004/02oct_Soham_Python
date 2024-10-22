num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))

if num1==num2 or num2==num3 or num3==num1:
    print("sum is zero")
else:
    result = num1 + num2 + num3
    print("sum is",result)
