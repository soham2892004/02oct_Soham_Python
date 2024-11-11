#define function remove-duplicate values
def RemoveDuplicate(SampleList):
    
    #convert list samplelist to set My_set
    My_set=set(SampleList)

    #display set My_set
    print (My_set)

#define sampleList
SampleList=["Abc","AAA","abcd","efg","AAA","abc","Abc"]

#call function removeDuplicate
RemoveDuplicate(SampleList)
