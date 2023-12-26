class state:
    a = 'Love'

    def show(self):
        print(f"the name of employee is {self.name}. a is {self.a}")
    @classmethod
    def change_a(self,new_a):
        self.a = new_a

obj = state()
obj.name = 'life' 
obj.show()
obj.change_a('look')
obj.show()
print(state.a)