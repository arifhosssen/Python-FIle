# x = lambda a: a+ 40
# print(x(40))
#
# def myfunc(m,n):
#     return m(n)
#
# lfunc = lambda b: b*3
#
# print(myfunc(lfunc,8))
from functools import reduce
#
def myfunc(a):
    return a*a
mylist = [3,45,76,34,65,25,45]
x = map(myfunc,mylist)
print(list(x))

print(list(filter(lambda a: a>=40, mylist)))
print(list(filter(lambda a: a>=40, mylist)))
print(list(map(lambda a: a+5, mylist)))
print(reduce(lambda x,y:x+y, mylist))
sum = 0
for x in mylist:
    sum = sum + x
print(sum)