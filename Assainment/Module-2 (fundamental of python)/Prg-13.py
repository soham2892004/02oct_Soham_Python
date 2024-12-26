# take user input for string
string = input("Enter a string: ")

#Create an empty string to store characters 
counted_chars = ""

# for loop displayed each character in the input string
for char in string:
        
        #initialise count variable and value passed to 0
        count = 0
        for c in string:
            if c == char:
                count += 1
        # displayed to the character and its frequency
        print("Character:", char,", Frequency:", count)
        # Add the character to the string of counted characters
        counted_chars += char
        
