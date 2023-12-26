# # # # # import random as rn
# # # # # # random as rn
# # # # #
# # # # # rnnmbr = rn.randrange(1,10)
# # # # # mynmbr= int(input("Enter Your Number: "))
# # # # #
# # # # # if mynmbr < rnnmbr:
# # # # #     print("'You  are lower then rand_nmbr'\nThe random number is: ", rnnmbr )
# # # # #
# # # # #
# # # # # elif mynmbr > rnnmbr:
# # # # #     print("You are grater then rand_nmbr\nThe random number is: ", rnnmbr)
# # # # #
# # # # # else:
# # # # #     print("You are equals\nThe random number is: ", rnnmbr)
# # # #
# # # # import math
# # # # y = math.lcm(20,10)
# # # # x = math.gcd(20,10)
# # # # print(x,y)
# # # # print(math.pi)
# # #
# # # my_list = ['mango','bnana', 'cherry','guava', 23,45,678,'joy']
# # # #
# # mylist= []
# # for i in range(10):
# #     print('Enter the ',i,'th number')
# #     x = input()
# #     mylist.append(int(x))
# # # print(mylist)
# # bigger = mylist[0]
# # smaller = mylist[0]
# # for nmbr in mylist:
# #     if bigger < nmbr:
# #         bigger = nmbr
# #     if smaller> nmbr:
# #         smaller = nmbr
# # s = 0
# # for nmbr in mylist:
# #     s = s + nmbr
# # avg = s/len(mylist)
# # print(mylist,'\nThe biggest number is: ', bigger,'\nThe smallest number is: ',smaller,'\naverag number is:',avg)
# #
# #
# # # print("bangladesh is 'Beautifull' country.\n It has \"beautifull\"place to hang out .\n its almost moslim contrise", end ="\nLObely conutry")
# #
# # x = "arif I love Allah"
# # y = "hossen1"
# # # print(x.replace("arif","Hossen"),x,y)
# #
# # print(x.split())
# # print(x.upper())
# # print(y.center(50))
# # print(y.isalnum())
# # print(y.isalpha())
#
#
# # x = 0
# # mylist = []
# # while x<10:
# #     x= int(input("Enter Your Number"))
# #     a = mylist.append(x)
# #     print(a)
# #
# # for x in range(11):
# #     print("2 X", x ,"=",2*x)
# #     print("3 X", x ,"=",3*x)
# #     print("4 X", x ,"=",4*x)
# #     print("5 X", x ,"=",5*x)
# #     print("6 X", x ,"=",6*x)
# #     print("7 X", x ,"=",7*x)
# #     print("8 X", x ,"=",8*x)
# #     print("9 X", x ,"=",9*x)
# #     print("10 X", x ,"=",10*x)
#
#
# # def f(*a):
# #     sum = 0
# #     for i in a:
# #         sum = sum + i
# #     x = sum/len(a)
# #     print(x)
# #
# # f(3,4,5,6,7,8,9,0,5,4,3)
# #
# #
# # l = ["apple", "banana", "cherry", "apple", "cherry"]
# #
# #
# # print(l[-3])
# # print(l[len(l)-3])
# # print()
#
#
# a = "Hay my name is {}. I'm from {}."
# name = "Arif"
# country = "Bangladesh"
# x = a.format(name,country)
# print(x)
# print(f"Hay my name is {name}.I'm from {{country}}.")

for i in range(10):
    if i ==3:
        continue
    print(i)

else:
    print('Sorry no more i')