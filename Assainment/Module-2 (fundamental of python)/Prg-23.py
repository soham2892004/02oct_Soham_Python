original_string = input("Enter the original string: ")

string_to_insert = input("Enter the string to be inserted: ")

middle_index = len(original_string) // 2

print (original_string[:middle_index] + string_to_insert + original_string[middle_index:])

