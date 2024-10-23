string_value=input("enter string:")

if len(string_value)>=3 and not string_value.endswith("ing"):
    print(string_value+"ing")
elif string_value.endswith("ing"):
    print(string_value+"ly")
else:
    print(string_value)