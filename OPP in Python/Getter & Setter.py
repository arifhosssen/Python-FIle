# class mycls:
#     def __init__(self,value):
#         self._value = value
#
#     def details(self):
#         print(f"The value you enter is : {self._value}")
#
#     @property                                        # Making setter.........
#     def five_value(self):
#         return 5 + self._value
#
#     @five_value.setter                               # Make a setter for changing value.........
#     def five_value(self,new_value):
#         self._value = new_value-5
#
#
# obj = mycls(10)
# obj.five_value= 55
# print(obj.five_value)
# obj.details()


# class a:
#     def __init__(self,num):
#         self.num = num
#
#     def show(self):
#         print(f"The number is: {self.num}")
#
#     @property
#     def getter(self):
#         return self.num * self.num
#
#     @getter.setter
#     def getter(self,new):
#         self.num = new / new
#
# object = a(5)
# object.num = 4
# print(object.getter)
# object.show()
#
#
# class a:
#     def __init__(self,numbers):
#         self.num = numbers
#
#     def show(self):
#         print(f"the number is {self.num}")
#
#     @property
#     def advalue(self):
#         return self.num
#     @advalue.setter
#     def advalue(self,value):
#         self.num = self.num ** value
#
# obj = a(20)
# obj.advalue = 2
# print(obj.advalue)
# obj.show()

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a // b)
    print(a / b)