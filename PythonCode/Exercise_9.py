
"""
class fruits:
    def apple(self):
        print("this is a sweet fruits")

    def banana(self):
        print("its also sweet")

class food (fruits):

    def rice(self):
        print("its a diffrent test")

f = food()
f.apple()
f.banana()
f.rice()
"""

# class food:
#     def __init__(self):
# #         print("You can eat")
# #
# # class banana(food):
# #     def __init__(self):
# # #         super().__init__()
# # #         print("its a fruit")
# # #
# # # b=banana()
# #
# # x = 80
# #
# # def fnc():
# #     global x
# #     x = 70
# #     y = 5
# #     print(y,x)
# #
# # fnc()
# # print(x)
#
# f = open("text.txt2" ,"r")
# a = f.read()
# print(a)
# f.close()
# f = open("text.txt","r")
# b =f.read()
# print(b)
# f.close
#
# with open("text.text","a") as f:
#     f.write("hay I'm inside with you")

class animal:
    def __init__(self,name,Specify):
        self.name = name
        self.Specify = Specify

    def show(self):
        print(f"Name: {self.name}")
        print(f"Specify: {self.Specify}")

class cat(animal):
    def __init__(self,name, sound):
        animal.__init__(self, name, Specify = "cat")
        self.sound = sound

    def show(self):
        animal.show(self)
        print(f"Sound: {self.sound}")

class view(cat):
    def __init__(self,name,view):
        cat.__init__(self, name, sound = "View")
        self.view = view

    def show(self):
        cat.show(self)
        print(f"View: {self.view}")

obj = cat("Cat","Brawn")
obj.show()
print(view.mro())


class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species

  def show_details(self):
    print(f"Name: {self.name}")
    print(f"Species: {self.species}")


class cat(Animal):
  def __init__(self, name, sound):
    Animal.__init__(self, name, species="cat")
    self.breed = sound

  def show_details(self):
    Animal.show_details(self)
    print(f"Breed: {self.breed}")


class GoldenRetriever(cat):
  def __init__(self, name, color):
    cat.__init__(self, name, sound="Golden Retriever")
    self.color = color

  def show_details(self):
    cat.show_details(self)
    print(f"Color: {self.color}")


o = GoldenRetriever("tommy", "Black")
o.show_details()
print(GoldenRetriever.mro())