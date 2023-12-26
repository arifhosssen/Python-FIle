# f = open("text.txt")
# i = 0
# while True:
#     line = f.readline()
#     if not line:
#         break
#     i += 1
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     m4 = int(line.split(",")[3])
#     print(f"The number of {i} marit is : {m1*2}")
#     print(f"The number of {i} marit is : {m2*2}")
#     print(f"The number of {i} marit is : {m3*2}")
#     print(f"The number of {i} marit is : {m4*2}")
#
#     print(line)

class Father:
    def __init__(self,name,age,occu):
        self.name = name
        self.age = age
        self.occupation = occu

    def details(self):
        print(f"{self.name} is {self.age} year's old.\nHe is a {self.occupation}.")


class Mother(Father):
    def __init__(self, bp, rlg):
        self.blood_group = bp
        self.religion = rlg
    def details2(self):
        print("Blood group is" + self.blood_group)
        print(self.name + "religion is" + self.religion)

class Brother(Father):
    pass

class Child(Father):
    pass


a = Father("Noor Alam", 55, "Farmer")
a.details()

a = Child("Arif",22 , "Softwear Engineer")
a.details()

a=Brother("Sozib", 28, "Data Engineer")
a.details()

a = Mother("B+", "Islam")
a.details2()