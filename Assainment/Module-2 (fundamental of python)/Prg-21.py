string = input ("enter a string:")

if len(string) % 4 == 0:
    reverse_string = string[::-1]
else:
    reverse_string = string

print ("Reverse string:",reverse_string)
