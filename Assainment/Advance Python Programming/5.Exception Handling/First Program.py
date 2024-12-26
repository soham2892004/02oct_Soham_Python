while True:
    try:
        #get user inputs
        no1=int(input("enter no1:"))
        no2=int(input("enter no2:"))
        operator=input("enter operator(+,-,*,/):")
        
        #perform calculation based on the operator
        if operator=='+':
            Result=no1+no2
        elif operator=='-':
            Result=no1-no2
        elif operator=='*':
            Result=no1*no2
        elif operator=='/':
            Result=no1/no2
        else:
            print("Invalid Operator.Use one of +,-,*,/.")
            
        print (f"Result:~{Result}")
        
    except ZeroDivisionError:
        print("Error ! Division by Zero is not allowed")
        
    except Exception as e:
        print(e)
        
    action=input("Do user perform another operations(Yes/No):").lower()
    if action!='yes':       
        break