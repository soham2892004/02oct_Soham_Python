# take input string1 and string2
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# first 2 character string 1 and 2 passed to temp1 and temp2
temp1 = string1[:2]
temp2 = string2[:2]
# swapping first two character string 1 and string 2 and temp1 and temp2 include in string 2 and string1
string1 = temp2 + string1[2:]
string2 = temp1 + string2[2:]

# displayed to combined string
print("Combined string:", string1,string2)