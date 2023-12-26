# Exercise how to use user define function in python programing language.
                #________________________________#
"""
def jug(a,b,c,d):
    sum = a+b+c+d
    print(sum)

def gun(x,y):
    multiple = x - y
    print(multiple)

jug(10,20,30,40)
gun(10,10)
"""

"""

def add(*x):
    sum = 0
    for number in x:
        sum = sum + number
    print(sum)

add(10,40,23,78)

add(20,30,40,50,60,70)"""

# def multiple(*number):
#     multi = 0
#     for num in number:
#         multi = multi * num
# #     print(num)
# #
# # multiple(20,10,9)
#
# x = int(input("Enter the value bettween 8 to 11: "))
#
# if (x>15 or x<8):
# #     raise ValueError("Follow the condition of input somthing")
# # else:
# #     print(f"Your number is: {x}")
# spr = lambda a: a*a
# list2 = [1, 5, 7, 9, 3]
# # thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# newlist = []
# # for i in list2:
# #     newlist.append(spr(i))
#
# # newlist = tuple(map(spr,list2))
# # print(newlist)
#
# ages = [5, 12, 17, 18, 24, 32]
# def func(x):
#   return x >= 18
#
# adults = list(filter(func , ages))
# print(adults)

class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species

  def show_details(self):
    print(f"Name: {self.name}")
    print(f"Species: {self.species}")


class Dog(Animal):
  def __init__(self, name, breed):
    Animal.__init__(self, name, species="Dog")
    self.breed = breed

  def show_details(self):
    Animal.show_details(self)
    print(f"Breed: {self.breed}")


class GoldenRetriever(Dog):
  def __init__(self, name, color):
    Dog.__init__(self, name, breed="Golden Retriever")
    self.color = color

  def show_details(self):
    Dog.show_details(self)
    print(f"Color: {self.color}")


o = Dog("tommy", "Black")
o.show_details()
print(GoldenRetriever.mro())
