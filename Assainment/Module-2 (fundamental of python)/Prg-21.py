#take input string from user
string = input ("enter a string:")

#check condition,if length of string reminder to 4 equal to 0
if len(string) % 4 == 0:
    reverse_string = string[::-1]
else:
    reverse_string = string

#displayed reversed string
print ("Reverse string:",reverse_string)
