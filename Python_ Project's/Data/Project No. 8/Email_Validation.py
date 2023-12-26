# min 6 chrecture
# use lowercase alphabets
# only alow '@','.' and '-' one time
# ^ with letter
#
while True:

    email = input("Enter your Email: ")
    a, b, c = 0, 0, 0
    if len(email) >= 6:
        if email[0].isalpha():
            if ('@' in email) and (email.count('@') == 1):
                if (email[-4] == '.') ^ (email[-3] == '.'):
                    for i in email:
                        if i.isspace():
                            a = 1
                        elif i.isalpha():
                            if i == i.upper():
                                b = 2
                        elif i.isdigit():
                            continue
                        elif i == '_' or '.' or '@':
                            continue
                        else:
                            c = 1
                    if a == 1 or b == 2 or c == 3:
                        print("You enter a wrong Email 5")
                    else:
                        print("It's Right Email")
                        break
                else:
                    print(";You enter a wrong Email 4")
            else:
                print("You enter a wrong Email 3")

        else:
            print("Your enter a wrong Email 2")
    else:
        print("You enter a wrong Email 1")


# there are another way to write this shortly.......
# # we use a Module in this code..........

# import re
#
# while True:
#     pattern ="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
#
#     email = input("Enter your Email: ")
#     if re.search(pattern,email):
#         print("Right Email")
#         break
#     else:
#         print("Wrong Email!")

