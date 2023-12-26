# class maincls:
#     def func(self):
#         print("this is the perent class.")
#     def new(self):
#         print("another main class")
# class subcls(maincls):
#     def func(self):
#         print("this is the func method of subcls")
#         super().new()
#     def func1(self):
#         print("this is the sub class.")
#         super().func()
#
# a = maincls()
# a.func()
# b = subcls()
# b.func()
#
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Teacher(Student):
    def __init__(self, name, id, sector):
        super().__init__(name, id)
        self.sector = sector

a = Teacher("Arif", 101, "ICT")
b = Student("Sohag", 120)
print(a.name, a.id, a.sector)
print(b.name, b.id)


