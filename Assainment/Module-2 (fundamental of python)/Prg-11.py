#take value of n from user
n=int(input("enter value of n:"))

#intialise variable sum and it's value is 0
sum = 0

# process for sum of first positive n numbers
for i in range(1, n+1):
    sum += i

#displayed result
print("The sum of the first", n, "positive integers is:", sum)