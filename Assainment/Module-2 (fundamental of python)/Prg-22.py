#take input string from user
string=input("enter a string:")

#check condition if length of string greater than equal to 2
if len(string)>=2:
    #displayed fitst 2 character and last two character of string
    print (string[:2]+string[-2:])
#when if condition false,so else part executed
else:
    print ("")