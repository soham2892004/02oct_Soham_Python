#create empty list
Sample_Tuple=[]

#take input from user for different type of data
String_Data=str(input("enter string type data:"))
integer_Data=int(input("enter integer type data:"))
floating_Data=float(input("enter floating type data:"))
boolean_Data=bool(input("enter boolean type data:"))


#value of diffrent type add to Sample_tuple
Sample_Tuple.insert(1,String_Data)
Sample_Tuple.insert(2,integer_Data)
Sample_Tuple.insert(3,floating_Data)
Sample_Tuple.insert(4,boolean_Data)

#convert list into tuple using tuple() and displayed tuple
print (tuple(Sample_Tuple))
