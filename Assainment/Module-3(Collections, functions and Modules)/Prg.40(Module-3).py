#define list Test_List1 and Test_List2
Test_List1=[101,201,301,401,501,601]
Test_List2=['Soham','Ram','Lakshman','Bharat','Shatrughna','Rohan']

#zip function corresponding elements from 2 lists into tuples,and dict()function converts 2 tuples into dictionary
Test_Dict=dict(zip(Test_List1,Test_List2))

#displayed dictionary name Test_Dict
print (Test_Dict)