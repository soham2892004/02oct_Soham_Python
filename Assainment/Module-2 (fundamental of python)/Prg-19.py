input_string=input("enter string:")

not_index=input_string.find("not")
poor_index=input_string.find("poor",not_index)

if not_index!=-1 and poor_index!=-1:
    print (input_string[:not_index] + "good" + input_string[poor_index + len("poor"):])

else:
    print (input_string)