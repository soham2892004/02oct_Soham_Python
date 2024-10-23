string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

temp1 = string1[:2]
temp2 = string2[:2]
string1 = temp2 + string1[2:]
string2 = temp1 + string2[2:]

merge_string = string1 + " " + string2


print("Combined string:", merge_string)