#define 3 Dictionary variables and initialise key and elements
dictionary1={101:"Vikram Shetty",102:"Sunil Sharma"}
dictionary2={201:"Rahul Jain",202:"Himanshu vyas"}
dictionary3={301:"Sahil Tiwari",302:"Vansh Chauhan"}

#concatenate dictionary 1,2 and 3 and it's concate to Demo_Dictionary
Demo_Dictionary={*dictionary1.items(),*dictionary2.items(),*dictionary3.items()}

#displayed Demo Dictionary variable
print (Demo_Dictionary)