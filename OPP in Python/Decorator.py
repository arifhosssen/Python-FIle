# Make a decorator Function**********
#
# def welcome(wc):
#     def dec():
#         print("Wellcome Here")
#         wc()
#         print("thanks for useing this function")
#     return dec
#
# @welcome
# def add():
#     print("My name is Arif.")
# @welcome
# def multi():
#     print("hay")
#
# add()
# multi()

# Decoratore with args and kwargs(****************

def hay(greater):
    def greet(*args):
        print("Yur result:")
        greater(*args)
        print("Have a nice day")
    return greet
def Hospitality(greet):
    def hptl(*args):
        print("Nice to meet you.")
        Hospitality(*args)
        print("Good to see you.")
    return hptl


@hay
def plus(a,b,c):
    print(a+b-c)

plus(2,3,4)

def Hospitality(greet):
    def hptl(*args):
        print("Nice to meet you.")
        greet(*args)
        print("Good to see you.")
    return hptl


@Hospitality
def func(a,b,c):
    print(a-b+c)

func(10,4,2)

def ccc(a,b,c):
    print(a+b-c)

Hospitality(ccc)(2,3,4)
