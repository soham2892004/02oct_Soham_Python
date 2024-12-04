#create list of dictionaries name Test_Data
Test_Data=[{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]

#create empty dictionary ,which stored combine amount
merge_amount={}

#iterate each dictionary in the Test_Data list
for item in Test_Data:
    #if item exist,so amount add to exist amount
    if item['item'] in merge_amount:
        merge_amount[item['item']]+=item['amount']
    #if item doesn't exist,so add a new entry with current amount
    else:
        merge_amount[item['item']]=item['amount']

#displayed merge_amount dictionary,which stored combine amount
print (merge_amount)