#define Sample_List list ,that include many tuples
Sample_List=[(1,2,3),(4,5,6),(7,8,9)]

#unzip using (*) operator and it's passed to list1,list2,list3
list1,list2,list3=zip(*Sample_List)

#displayed list1,list2,list3
print (list1)
print (list2)
print (list3)