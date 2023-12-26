import random


def password_generator():
    # Get the desired length of the password.
    length = int(input("How long do you want the password to be? "))

    # Generate a random password.
    password = "".join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for m in range(length))

    # Print the password.
    print("Your password is:", password)


if __name__ == "__main__":
    password_generator()