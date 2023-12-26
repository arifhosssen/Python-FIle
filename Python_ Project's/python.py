class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    # def speak(self):
    #     print("Dog barks")
    pass

class Cat(Animal):
    # def speak(self):
    #     print("Cat meows")
    pass

# Create instances of the subclasses
dog = Dog()
cat = Cat()

# Call the overridden methods
dog.speak()  # Output: "Dog barks"
cat.speak()  # Output: "Cat meows"
