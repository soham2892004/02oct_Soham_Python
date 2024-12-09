#create empty list
Sample_List=[]

#values type of atring,integer,float or boolean input by user
string_data=str(input("enter string Type data:"))
integer_data=int(input("enter integer type data:"))
float_data=float(input("enter floating type data:"))
boolean_data=bool(input("enter boolean type data:"))

#values of different type of data are added to list 
Sample_List.append(string_data)
Sample_List.append(integer_data)
Sample_List.append(float_data)
Sample_List.append(boolean_data)

#displayed sample_list
print (Sample_List)