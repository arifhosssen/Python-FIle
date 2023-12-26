# import os
# # if (not os.path.exists("File")):
# #     os.mkdir("File")
#
# for i in range(1,10):
#     os.renames(f"File/file_{i}", f"File/file_No_{i}")

# x = 5
# print(x)
#
# def myfunc():
#     global x
#     x = 3
#     print(x)
#
#
# myfunc()
# print(x)


file = open("sumary.txt", 'r')
i = 0
while True:
    s = file.readline()
    i += 1
    if not s:
        break
    a = int(s.split(',')[0])
    b = int(s.split(',')[1])
    c = int(s.split(',')[2])
    print(f"{i} Student Marks:\n Bangla: {a}\n English: {b}\n Maths: {c}")
    print("Total Marks: ", int(a+b+c))


    # # print(f" {i} nmbe {b}")
    # print(f" {i} nmbe {c}")

    # print(s)

file.close()