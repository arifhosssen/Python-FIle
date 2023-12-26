class student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def details(self):
        print(f"The student name is {self.name} and id id ({self.id}).")

class teacher(student):
    def details(self):
        print(f"The teacher name is {self.name} and id is ({self.id}).")

a = student("Arif",101)
a.details()
a1 = teacher("Akash", 15)
a1.details()
teacher.details(a1)

