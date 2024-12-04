#define dictionary D1 and D2
D1={'a':100,'b':200,'c':300}

D2={'a':300,'b':200,'d':400}

#define Empty Dictionary Test 
Test={}

Test['a']=D1['a']+D2['a']

Test['b']=D1['b']+D2['b']

Test['c']=D1['c']

Test['d']=D2['d']

print (D1,D2)

print (Test)