#take input string which is currently using string
original_string = input("Enter the original string: ")

#take input string which is insert to current string
string_to_insert = input("Enter the string to be inserted: ")

#initialise middle index variable ,it's equal to length of current string devide-devide to 2 
middle_index = len(original_string) // 2

#displayed string value which is represent current string first part + insert string + current string end part
print (original_string[:middle_index] + string_to_insert + original_string[middle_index:])

