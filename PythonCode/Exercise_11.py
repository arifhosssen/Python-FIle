class car:
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand

    def __str__(self):
        return(f"Model - {self.model}, Brand - {self.brand}")

    def __eq__(self, other):
        return  self.model == other.model and self.brand == other.brand

    def display(self):
        print(f"Model - {self.model}, Brand - {self.brand}")

c1 = car("BMW","bm-439s")
c2 = car("BMW","bm-439s")
print(c1 == c2)