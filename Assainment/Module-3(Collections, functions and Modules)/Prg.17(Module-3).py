#define empty list
SampleList=[]

#take value from user
for item in range(0,6):
    item=input("enter value for list:")
    SampleList.append(item)     #user input value include to SampleList

# split list values to different variables    
var1=SampleList[0]
var2=SampleList[1]
var3=SampleList[2]
var4=SampleList[3]
var5=SampleList[4]

# displayed all variables
print (var1 , var2 , var3 , var4 , var5)