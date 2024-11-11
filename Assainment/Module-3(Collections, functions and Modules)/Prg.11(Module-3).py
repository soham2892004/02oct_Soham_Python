#define function test
def Test(input_list):

    #initialise unique list
    unique_list=[]

    #take values from input list to unique list
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    print (unique_list)


#initialise list current list,and define values
Current_list=[11,1331,11,15551,121,1331,15551,177771]

#call function test 
Test(Current_list)
