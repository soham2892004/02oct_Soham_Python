#take input from user no1 and no2
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

#check condition to if num1==num2 or sum of num1 and num2=5 of difference from num1 and 2 is 5
#then displayed true
if num1==num2 or (num1+num2)==5 or (num1+num2)==-5 or (num1-num2)==5:
    print("true")
#check upper condition,if upper condition false,then else part executed
else:
    print("false")
