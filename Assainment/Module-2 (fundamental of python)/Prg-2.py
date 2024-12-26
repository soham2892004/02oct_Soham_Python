#take input number from user
num = int(input("Enter a number: "))

#checks the condition,that if the number is less than 0,so it cannot find the factorial
if num < 0:
     print("Factorial is not defined for negative numbers.")

#checks the condition,that if the number is 0,so 0's factorial value is 0
elif num == 0:
     print(num,"is zero")

#so when upper two conditon are false ,it represent positive value and process for find factorial
else:
    result = 1
    for i in range(1, num + 1):
      result *= i

#display result for finding factorial
print("The factorial of", num, "is", result)