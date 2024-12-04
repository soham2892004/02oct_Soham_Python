#create Sample_string variable,which asked string type value for user
Sample_String=input("Enter such as a string type Data:")

#displayed string
print (Sample_String)

#create empty dictionary,which name is char_Dictionary
char_Dictionary={}

#iterate each character in the Sample_String
for character in Sample_String:
    #if character exist in char_Dictionary,so character value add in this dictionary
    if character in char_Dictionary:
        char_Dictionary[character]+=1
    #if character doesn't exist in char_dictionary,so add a new entry with current character
    else:
        char_Dictionary[character]=1

#displayed char_Dictionary
print (char_Dictionary)