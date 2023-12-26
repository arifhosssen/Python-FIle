# # from abc import ABC,abstractmethod
# # class a():
# #     def border(self):
# #         print("its the proparty of a")
# #     @abstractmethod
# #     def area(self):
# #         pass
# #
# # class b():
# #     def border(self):
# #         print("its the proparty of b")
# #
# #
# # class c(a,b):
# #     """    def border(self):
# #         print("its the proparty of c")"""
# #     pass
# #
# #
# # obj = c()
# # obj.border()
#
# f = open("text.txt")
# # # print(f.readline())
# # # print(f.readline())
# # while True:
# #     line = f.readline()
# #     print(line)
# #     if not line:
# #         break
# #
# # # line = f.readline()
# # # print(line)
#
# class mycls:
#     # name = "Arif"
#     # occupation = "Softwear Engineer"
#     def __init__(self,name,occu):
#         self.name = name
#         self.occupation = occu
#     # def details(self):
#         print(f"{self.name} ia a {self.occupation}.")
#
# a = mycls("Sozib","Data Engineer")
# b = mycls("bijoy","Tiktoker")
# c = mycls("rabbi","Player")
# # a.name = "Sozib"
# # # a.occupation = "Data Engineer"
# # a.details()
# # b.details()
#
#
# # # for i in range(1,10):
# #     for x in range(i):
# #         print(x+1,end = "")
# # #     print(' ')
# #
# # def myfunc(a,b):
# #     print(a+b,a-b,a*b,a**b)
# # myfunc(20,2)
# #
# # def pluse(a,b,c):
# #     print(a+b+c)
# # pluse(1,2,3)
# #
# # import calendar
# # yy = 2022
# # mm = 11
# # # print(calendar.month(yy,mm))
# #
# # def make_pretty(func):
# #     def inner():
# #         print("I got decorated")
# #         func()
# #         print("I am ordinary")
# #     return inner
# #     # def ordinary():
# #     #     print("I am ordinary")
# #
# # @make_pretty
# # def myfunc():
# #     print("Hello World")
# #
# # x = myfunc()
# # print(x)
#
# class father:
#     name = ""

# a = lambda a: a*a
# b = lambda b: a/2
#
# # print(a(2,3))
#
#
# def x (X,y):
#     return 4 + X(y)
#
# print(x(a,3))


# class cls:
    # def __init__(self,number):
    #     self.num = number
    #
    # def multiple(self,m):
    #     self.num = self.num *m

    # @staticmethod
    # def mult(a,b):
    #     return a*b

# a = cls()
# print(a.num)
# a.multiple(5)
# print(a.num)

# print(a.mult(3,4))

#
# import win32com.client
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# l = ["Swastik Mishra", "Virat Kohli", "CodeWithHarry"]
# for i in l:
# 	speaker.speak(f"shout out to {i}")

import re

text = "ndustry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lo"

match = re.findall("to",text)
print(match)