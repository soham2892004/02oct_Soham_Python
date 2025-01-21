class Animal:
    # Base class method to be overridden
    def speak(self):
        print("The animal speaks")

class Dog(Animal):
    # Overriding the speak method of the base class
    def speak(self):
        print("The dog barks")

# Usage
animal = Animal()
animal.speak()  # Output: The animal speaks

dog = Dog()
dog.speak()     # Output: The dog barks
