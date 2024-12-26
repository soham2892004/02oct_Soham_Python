#take input from user no1 and no2
No_1=input("Enter value for no1:")
No_2=input("Enter value for no2:")

"""initialise variables and value of no1 passed to temp,
value of no2 passed to no1 and temp value passed to no2"""
temp=No_1
No_1=No_2
No_2=temp

#display no1 and no2
print("no1:",No_1)
print("no2:",No_2)