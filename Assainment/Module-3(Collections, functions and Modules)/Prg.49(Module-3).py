#create udf define function for check number in given range or not
def Check_Num(no, start, end):
    #if given number is middle number to starting range or ending range,so displayed message yes
    if start <= no and no <= end:
        print(f"Yes, {no} is greater than or equal to {start} and lower than or equal to {end}...")
    #if given number is not middle number to starting range or editing range,so displayed message no
    else:
        print(f"No, {no} is not greater than or equal to {start} and lower than or equal to {end}...")

#take input from user to 'no' variable
no=int(input("enter any number:"))

#define starting range 10
start=10
#define ending range 80
end=80

#call Check_Num function
Check_Num(no,start,end)