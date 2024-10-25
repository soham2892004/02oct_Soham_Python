#take value of string type from user
string = input("Enter a string: ")

# initialise length equal to zero
length = 0

# this loop is working act as a add 1 in length
#and it execute until the string character completed
for char in string:
    length += 1

#displayed length of string
print("The length of the string is:", length)