#define tuple name Sample_Tuple and inititalise value include in tuple
Sample_Tuple=(1,22,333,4444,55555)

#initialise element for check in tuple
check_Element=333

#check element in sample_tuple process....
if check_Element in Sample_Tuple:
        print (f"{check_Element} exist in the tuple")
else:
        print (f"{check_Element} doesn't exist in the tuple")