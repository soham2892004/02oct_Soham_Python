#create UDF function for check perfect no or not
def Check_PerfectNum(number):
  
  #define variable to store the sum of divisors
  divisor_sum = 0  

  # Iterate over numbers from 1 to number-1
  for i in range(1, number):
    # Check if i is a divisor of number
    if number % i == 0:
      # Add the divisor to the sum
      divisor_sum += i

  # Return True if the sum of divisors equals the number, otherwise False
  return divisor_sum == number

num1 = 6
num2 = 28
num3 = 12

print(f"{num1} is perfect: {Check_PerfectNum(num1)}")
print(f"{num2} is perfect: {Check_PerfectNum(num2)}")
print(f"{num3} is perfect: {Check_PerfectNum(num3)}")