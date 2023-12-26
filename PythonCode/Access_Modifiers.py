# Access Modifiers in Python.......

# three type of Access Modifiers in python:
#      1. Public Access Modifiers
#      2. Privet Access Modifiers
#      3. Protected Access Modifiers

### 1-Public Access Modifiers:-

class student:
    def __init__(self):
        self.name = "Arif"          #defauls public accessable.
        self.age = 22

a = student()
print(a.name,a.age)

### 2-Privet Access Modifiers:-

class Employee(student):                            #inheritance bt perents class "student".
    def __init__(self):
        self.__name = "Sofia Khatun"                #Privet by "__".
        self.__age = 45

a = Employee()
# print(a.name,a.age)             # Get Error
print(f"{a._Employee__name} is {a._Employee__age} year's old.")          # Accessable by using "_" in class and "__" in peramiters.
a = student()
print(f"{a.name} is {a.age} year's old.")               #class "student".

### 3-Protected Access in Python:-

