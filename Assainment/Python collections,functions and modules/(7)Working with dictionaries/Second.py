#create List1 and List2
List1=[1,2,3,4,5,6]

List2=['Jamnagar','Ahemdabad','Surendranagar','Bhavnagar','Junagadh','Rajkot']

#create empty Demo_Dict
Demo_Dict={}

#iterate over the list1 and list2 
for i in range(len(List2)):
    Demo_Dict[List1[i]]=List2[i]

#displayed Demo_Dictionary
print (Demo_Dict)
     