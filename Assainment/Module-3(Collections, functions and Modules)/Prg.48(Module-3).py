#create user define function-Factorial
def Factorial(no):
    #if input no is lower than 0 ,so error generate
    if no<0:
        return "error occured!please enter non-negative number or number>0...."
    #if input no is zero,so 0's factorial is 1
    elif no==0:
        return 1
    #if input no is nonnegative ,so result is provide properly
    else:
        return no*Factorial(no-1)

#asked value for no for user
no=int(input("enter valid non-negative number:"))

#call function factorial 
result=Factorial(no)

#displayed result of factorial 
print (f"factorial of {no} is {result}")