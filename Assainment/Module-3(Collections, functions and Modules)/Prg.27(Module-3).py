#define Tuple name Sample_List and initialise value
Sample_List=(1,5,6,3,4,8,9,5,8,9,5)

#define empty set
seen=set()

#define empty list
repeate_elements=[]

# iterate for loop for every element in Sample_List tuple
for item in Sample_List:
    if item in seen:    #if item is already in Sample_List and seen ,so it's element include in list repeated
        repeate_elements.append(item)
    else:
        seen.add(item)  #otherwise element add to set-seen


#displayed repeate_elements
print (repeate_elements)