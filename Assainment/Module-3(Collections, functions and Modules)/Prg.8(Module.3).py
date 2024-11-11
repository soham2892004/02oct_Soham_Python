#define function checkEmptyList
def CheckEmptyList(SampleList):
    
    #check condition to value contained yes or no in list
    if not SampleList:
        print("List is Empty")
    else:
        print("List is contain values")

#define list SampleList
SampleList=[21,54,65,54,35,45]

#call CheckEmptyList function
CheckEmptyList(SampleList)