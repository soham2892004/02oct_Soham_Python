#initialise UDF function test
def Test(number):
    Large=max(number) #it's find largest number in list

    Small=min(number) #it's find smallest number in list
    
    ListSum=sum(number) #it's count sum of number in list

    #displayed largest , smallest and sum of list value
    print (Large)
    print (Small)
    print (ListSum)

#initialise list 
ListNumber=[11,13,15,17,19]

#call function test and pass value of listnumber
Test(ListNumber)



