#take starting and ending range from user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Initialise variables
a = 0
b = 1
fib = 0

# if starting value is lower than equal to 0 it displayed 0
if start <= 0:
    print(0)

#if starting value is lower than equal to 1 it displayed 1
if start <= 1:
    print(1)

""" when fib value is lower than equal to ending value and executes
  this process,and it repeatedly until the fib value is greater 
 than ending point"""
while fib <= end:
    fib = a + b
    a = b
    b = fib


# if fib value is lower than end value and greater than start value ,so displayed fibonacci values
    if start <= fib <= end:
        print(fib)

    # Check if the next Fibonacci number greater than end point
    if fib + b > end:
        break  # Exit the loop if the next Fibonacci number is too large