# #  make quiz game that if user want to play write yes else no then we give a question to user with condition .
#
def quiz():
    print('Wellcome to Rapid fire')
    user = input("If you want to play this game type 'Yes' or 'No' : ")
    # quastion = input("Kathal ki asolei amisher kaj kore? 'Yes' or 'No' : ")

    if user == 'yes':
        answer = input("Kathal ki asolei amisher kaj kore? 'Yes' or 'No' : ")
        if answer == 'yes':
            print("You are wrong!")
        else:
            print("Youreka")
    else:
        print("Exit")
quiz()
#
#

# def play_game():
#     play = input("Do you want to play? (yes/no): ")
#
#     if play.lower() == "yes":
#         mango_response = input("Mango is test. Do you think it's true? (yes/no): ")
#
#         if mango_response.lower() == "yes":
#             print("You win!")
#         else:
#             print("You lose.")
#     else:
#         print("Alright, maybe another time.")
#
#
# play_game()
3