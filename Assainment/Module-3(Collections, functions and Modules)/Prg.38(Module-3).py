#define multiple key-values dictionary
Multi_Key={1:'Soham',2:'Rohan',3:'Ram',4:'Lakshman',5:'Bharat',6:'Shatrughna'}

#it's check key 1 to 6
Check_Key=[1,2,3,4,5,6]

#check condition if key is include in dictionary and key included to check_key list so multiple key exist 
if all (key in Multi_Key for key in Check_Key):
    print ("yes,Multiple keys exist in dictionary")

#otherwise keys are don't exist
else:
    print ("no,multiple keys don't exist in dictionary")

