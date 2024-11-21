#define Test_Tuple name list,that include to many tuples
Test_Tuple=[("a","b","c","d"),(),(1,2,3,4),("e","f","g","h"),()]

#define empty list
Demo_List=[]

#check condition ,if tuple in Test_Tuple list,so tuple's detail s
for tuple in Test_Tuple:
    if tuple:
        Demo_List.append(tuple)

#displayed Demo_List
print (Demo_List)
