class mycls():
    name = "Arif"
    age = 22
    occu = "Student"
    def details(self):
        print(f"{self.name} is {self.age} year's old and he is a {self.occu}.")

obj = mycls()
# print(obj.name,obj.age,obj.occu)
obj.details()
obj1 = mycls()
obj1.name = "Sozib"
obj1.age = 28
obj1.occu = "Intern"
obj1.details()


"""Python Constractor"""

class newcls(mycls):                #Inheritance here to take print stetment.
    def __init__(self,name,age,occu):
        self.name = name
        self.age = age
        self.occu = occu

    # def details(self):
        # print(f"{self.name} is {self.age} year's old and he is a {self.occu}")

x = newcls("Nur_Alam",55,"Post_Man")
x.details()