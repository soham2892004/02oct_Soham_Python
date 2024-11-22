#define dictionary Test_Dict,initialise key and key values id and names
Test_Dict={101:"Ram",102:"Lakshman",103:"Bharat",104:"Shatrughna",105:"Rahul"}

#ask user input ,which key check for exist in dictionary
choise_Key=int(input("Enter key value:"))

if choise_Key in Test_Dict:
    print (f"Key'{choise_Key}'is exist in the dictionary")
else:
    print (f"Key'{choise_Key}'is doesn't exist in the dictionary")

