#take input to no1,no2 and no3 from user
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))

#check condition if num1 equal to num2 or 
# num2 equal to num3 or num3 equal to num1 
# ,so sum value is zero
if num1==num2 or num2==num3 or num3==num1:
    print("sum is zero")
#when if condition false, so else part automatically executed
else:
    result = num1 + num2 + num3
    print("sum is",result)  #displayed sum of no1,no2 and no3
