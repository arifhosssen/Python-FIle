# Python Decorator...........

# def greed(func):
#     def mfunc(*args):
#         print("Well_Come")
#         func(*args)
#         print("Thank's For Using This Function")
#     return mfunc
#
# @greed
# def a(a , b):
#     print(a + b)
# # a( 2 , 3 )
# # greed(a)(3,4)
# a(4,5)


def wellcome(fx):
    def mfx(*args):
        print("Hay there, Good Morning")
        fx(*args)
        print("thank's For Using This Program")
    return mfx

@wellcome
def myfunc(a,b):
    print(a + b)

myfunc(2,3)
