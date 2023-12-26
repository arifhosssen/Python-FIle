import random

while True:
    try:
        user = input("Rock, Paper, Seossor:  ").capitalize()
        com = random.choice(["Rock", "Paper","Seossor"])
        if user in (["Rock", "Paper","Seossor"]):
            if (user == "Rock" and com == "Seossor" or user == "Paper" and com == "Rock" or user == "Seossor" and com == "Paper"):
                print("You Win")
                break
            elif user == com:
                print("It's a tie")
            else:
                print("You Loss")
        else:
            print("Please! Enter_")
    except:
        pass