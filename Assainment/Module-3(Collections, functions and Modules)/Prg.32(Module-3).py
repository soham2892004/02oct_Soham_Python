#define dictionary which initialise id_no,name
Sample_Dictionary={4:"Soham",1:"Rajan",2:"Mayank",5:"Avinash",3:"Dhruvik"}

#method for represent ascending order 
Ascending_Order=dict(sorted(Sample_Dictionary.items()))

#method for represent descending order
Descending_Order=dict(sorted(Sample_Dictionary.items(),reverse=True))

#displayed Dictionary to ascending order
print (Ascending_Order)

#displayed Dictionary to descending order
print(Descending_Order)