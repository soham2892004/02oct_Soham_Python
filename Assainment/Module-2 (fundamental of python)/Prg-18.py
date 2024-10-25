#take input string from user
string=input("enter string:")

#check condition if length of string is greater than equal to 3 and not string ending character "ing"
if len(string)>=3 and not string.endswith("ing"):
    print(string+"ing")
#check condition if string ending characters "ing" so added "ly" include with string
elif string.endswith("ing"):
    print(string+"ly")
#when upper two condition are false ,so displayed only string without modified
else:
    print(string)