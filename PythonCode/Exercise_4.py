# # # # # # #
# # # # # # #
# # # # # # # x = ("apple", "banana", "cherry", "strawberry","cherry", "raspberry","cherry")
# # # # # # # # y = x.count("cherry")
# # # # # # # print(y)
# # # # # #
# # # # # # # thisset = ["apple", "banana", "cherry"]
# # # # # # tropical = {"pineapple", "mango", "papaya"}
# # # # # # tropical.discard("mango")
# # # # # # print(tropical)
# # # # #
# # # # #
# # # # # student_list = {
# # # # #     101:{
# # # # #         "name" : "Suhag",
# # # # #         "roll" : 101,
# # # # #         "id" : "Dual",
# # # # #         "study" : "PSSC"
# # # # #     },
# # # # #     102:{
# # # # #         "name": "ruma",
# # # # #         "roll": 102,
# # # # #         "group": "LION",
# # # # #         "study": "sawC"
# # # # #     }
# # # # # }
# # # # # print(student_list.keys())
# # # #
# # # # set = {
# # # #   "brand": "Ford",
# # # #   "model": "Mustang",
# # # #   "year": 1964
# # # # }
# # # # #
# # # # # #set["model"] = "BMW"
# # # # # # set.update({"color":"green"})
# # # # # # print(set)
# # # # # set.pop("model")
# # # # # print(set)
# # # #
# # # # x = 0
# # # # while x < 10:
# # # #     if x == 7:
# # # #         continue
# # # #     print(x , "Hay  How are you")
# # # #     x+=1
# # # #
# # # # def my_function():
# # # #     print("Hello from a function")
# # # #     my_function()
# # # #
# # # # my_function()
# # # class Person:
# # #     def __init__(self, fname, lname):
# # #         self.firstname = fname
# # #         self.lastname = lname
# # #
# # #     def printname(self):
# # #         print(self.firstname, self.lastname)
# # #
# # # class Student(Person):
# # #     def __init__(self, fname, lname):
# # #         Person.__init__(self, fname, lname)
# # #
# # # x = Student("Arif","Hossen")
# # # x.printname()
# # #
# # #
# # #
# # a = 29
# # b = 78
# #
# # def myfunc():
# #     x = 34
# #     print(x)
# #     print(b)
#
# x = open("text.txt", "a")
# print(x.write("this is new append item"))
# x.close()
# x = open("text.txt", "r")
# print(x.read())
#
# f = open("text.txt", "w")
# f.write("Now the file has more content!")
# f.close()
#
# #open and read the file after the appending:
# f = open("text.txt", "r")
# print(f.read())

#
#
#
# x = int(input("Enter number between 5 to 9: "))
#
# if x<5 or x>9:
#     raise ValueError("Value should be between 5 to 9")
#
# else:
#     print("Program Fnished")
#
#
# a = 33
# b = 3303
# print("A") if a>b else print("=") if a==b else print("B")

mlist=[32,45,67,45,34,76,345,63]
for index,x in enumerate(mlist,start=1):
    print(index,x)
    if (index == 3):
        print( "number is importent")