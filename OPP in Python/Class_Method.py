class mycls:
    clg_name = "UTC"
    def __init__(self,name):
        self.name= name

    def details(self):
        print(f"The name of student is {self.name} studied in {self.clg_name}.")
    @classmethod
    def newvar(self,newvar):
        self.clg_name= newvar

obj = mycls("Arif")
# obj.name= "Arif"
obj.clg_name = "DIU"
obj.details()
obj1 = mycls("Siam")
obj1.newvar("BUET")
obj1.details()
print(mycls.clg_name)
