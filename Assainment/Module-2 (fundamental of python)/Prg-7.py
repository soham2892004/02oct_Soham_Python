#take number value for user
num=int(input("enter number:"))

"""check condition to reminder of 
 number devided by 2 equal to zero
,so displayed it's a even number,
when upper if condition false ,so 
 execute else part automatically,and 
 it's displayed odd number"""
if num%2==0:
    print(num,"is even number")
else:
    print(num,"is odd number")
