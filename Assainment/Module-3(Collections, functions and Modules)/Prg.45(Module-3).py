#define Sample_Dictionary
Sample_Dict={10:'ashutosh',25:'bharat',15:'chetan',35:'dipak',20:'elvish',30:'faruk'}

#it's sort to dictionary element to ascending order
Sorted_Dict=dict(sorted(Sample_Dict.items()))

#convert dictionary to list,because displayed last 3 maximum values 
Displayed_element=list(Sorted_Dict)

#displayed last 3 maximum values
print(Displayed_element[3:])