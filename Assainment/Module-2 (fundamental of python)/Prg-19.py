# take string from user
string=input("enter string:")

#string's find method  which is find words in string and it method passed to index number
not_index=string.find("not")
poor_index=string.find("poor",not_index)

#check condition if index number of 'not' and index number of 'poor' is not equal to -1
if not_index!=-1 and poor_index!=-1:
    print (string[:not_index] + "good" + string[poor_index + len("poor"):])

else:
    print (string)