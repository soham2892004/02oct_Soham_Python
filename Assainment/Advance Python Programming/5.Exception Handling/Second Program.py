"""Exception raised for invalid input (non-integer values)."""
while True:
    class InvalidNumber(Exception):
        pass

    try:
        """get input from the user"""
        no1=int(input("enter no.1:~"))
        no2=int(input("enter no.2:~"))
        
        """ Determine and print the greater number"""
        if no1>no2:
            print(f"{no1}is greater than {no2}")
        elif no2>no1:
            print(f"{no2}is greater than {no1}")
        else:
            print(f"{no1} & {no2} are Same Number....")
    #handle invalid output
    except InvalidNumber:
            print("input numbers are invalid....")
    #handle unexpected error
    except Exception as e:
            print(e)
        
