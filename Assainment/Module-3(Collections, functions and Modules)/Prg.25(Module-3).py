#define list
Sample_List=[]

#ask user input and it's include to list
for item in range(0,6):
    item=input("enter value for Tuple:")
    Sample_List.append(item)

#convert Sample_List to Sample_Tuple
Sample_Tuple=tuple(Sample_List)

#displayed reversed tuple Sample_Tuple
print ("\n",Sample_Tuple[-1],"\n",Sample_Tuple[-2],"\n",Sample_Tuple[-3],"\n",Sample_Tuple[-4],"\n",Sample_Tuple[-5],"\n",Sample_Tuple[-6])

