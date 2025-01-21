class MathOperations:
    # Method with default argument to demonstrate method overloading
    def add(self, a, b, c=0):
        # Adding two or three numbers based on the arguments provided
        return a + b + c

# Usage
math_op = MathOperations()

# Calling add method with two arguments
print(math_op.add(10, 20))        # Output: 30

# Calling add method with three arguments
print(math_op.add(10, 20, 30))    # Output: 60
