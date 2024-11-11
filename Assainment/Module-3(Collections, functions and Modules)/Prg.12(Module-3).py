#define function convert list to string
def Convert_List_String(Sample_List):
    #display string using join method for join Sample List
    print ("".join(Sample_List))

#initialise empty list
Sample_List=[]

#value asked to user for Sample List
for i in  range(0,12):
    value=input("enter value for list:")
    Sample_List.append(value)

#call function for convert list character into string
Convert_List_String(Sample_List)



