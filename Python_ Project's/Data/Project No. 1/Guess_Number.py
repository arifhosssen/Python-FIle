#Make a random number program by useing function........

# import random
#
# def guess():
#     random_number = random.randint(1,15)
#
#     step = 1
#     while True:
#         try:
#             guess_number = int(input("Guess Your Number Between 1 To 15: "))
#             step += 1
#
#             if 1<= guess_number <= 15:
#                 if guess_number == random_number:
#                     print(f"Congratulation's! You Get It.\n The Number Was: {random_number} And You Catch It {step}th Step.")
#                 else:
#                     print(f"OH Shit!.\nYou Lose, The Number Was: {random_number}")
#                     break
#             else:
#                 print("Please!Enter The Number Between 1 To 15: ")
#
#         except(ValueError):
#             print("Invaild Syntest!, Enter The Number Between 1 To 15: ")
#
#
# guess()


#with out function.........

import random

random_number = random.randint(1,8)
step = 1
while True:
    try:
        guess = int(input("Guess Your Number Between 1 To 8: "))
        step += 1
        if 1 <= guess <= 10:
            if guess == random_number:
                print(f"Congratulation's! You Get It.\n The Number Was: {random_number} And You Catch It {step}th Step.")
                break
            else:
                print(f"OH Shit!.You Lose, The Number Was: {random_number}")
        else:
            print("(Please!Enter The Number Between 1 To 8)")

    except(ValueError):
        print("Invaild Syntest!")



