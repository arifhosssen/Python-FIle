# from random import randint
# for x in range(5):
#     gusenum = int(input("Enter Yout Number: "))
#     randomnumber = randint(1,10)
#
#     if randomnumber == gusenum:
#         print("Your Have Own")
# #     else:
# #         print("Your Have Loss")
# # #     print("The random number is: ",randomnumber)
# #
# # f = open("myfile.txt","w")
# # text = "bangladesh is beautifull\n","its beautifull\n","dhaka is its capital\n","im also here form it\n","hay i am arif\n"
# # print(f.writelines(text))
#
# f = open("text.txt")
# f.seek(5)
# print(f.tell())
# print(f.read(9))

f = open("sumary.txt","w")
f.write("Hello World")
f.truncate(5)
