# import random

# Generate a random number between 1 and 10
# secret_number = random.randint(1, 10)

# Ask the user to guess the number
# while True:
#     try:
#         guess = int(input("Guess the number between 1 and 10: "))
#         if 1 <= guess <= 10:
#             break
#         else:
#             print("Please enter a number between 1 and 10.")
#     except ValueError:
#         print("Invalid input. Please enter a number between 1 and 10.")
#
# # Check if the guess is correct
# if guess == secret_number:
#     print("Congratulations! You guessed the correct number.")
# else:
#     print(f"Sorry, the correct number was {secret_number}. Try again!")

# import random
#
#
# def guess_number():
#     # Generate a random number between 1 and 10
#     secret_number = random.randint(1, 10)
#
#     attempts = 0
#
#     while True:
#         try:
#             # Ask the player to guess the number
#             guess = int(input("Guess the number between 1 and 10: "))
#             attempts += 1
#
#             # Check if the guess is correct
#             if guess == secret_number:
#                 print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
#                 break
#             elif guess < secret_number:
#                 print("Too low! Try again.")
#             else:
#                 print("Too high! Try again.")
#         except ValueError:
#             print("Invalid input. Please enter a valid number between 1 and 10.")
#
#
# # if __name__ == "__main__":
# guess_number()

def add(n):
    if n <= 0:
        return 0
    return n + add(n-1)
print(add(10))
