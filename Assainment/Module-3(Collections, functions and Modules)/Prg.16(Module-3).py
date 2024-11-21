# Define the main list and the sublist 
main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sub_list = [6,7,8]

found = False

# Iterate thraough the main list, checking for the sublist
for i in range(len(main_list) - len(sub_list) + 1):
    # Create a window of the same size as the sublist
    window = main_list[i:i+len(sub_list)]

    # Check if the current window matches the sublist
    if window == sub_list:
        
        found = True
        break

# Print the result based on the found flag
if found:
    print("Sublist found")
else:
    print("Sublist not found")