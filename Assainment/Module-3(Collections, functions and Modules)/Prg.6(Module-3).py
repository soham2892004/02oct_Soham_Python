# initialise function for count number of strings
def count_NumberOfString(stringList):

    #initialise variable sum value defined 0    
    sum=0

    #initialise for loop,where string include in stringList so check condition if
    for string in stringList:
        """check if condition that length of string greater than or equal to 2 
         and string last character and first character are same ,so sum added 
         1 number value"""
        if len(string)>=2 and string[-1]==string[0]:
            sum+=1  #add 1 value in sum variable

            print (sum)   #display sum variable

#initialise list stringlist
stringList=["abc","xyz","ada","1331","pop","vip","rsr"]

#call udf function name is NumberOfString
result=count_NumberOfString(stringList)

#Display final result
print (result)

    


