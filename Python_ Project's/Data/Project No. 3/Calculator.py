# Calculator:
# Create a basic calculator program that can perform operations
# like addition, subtraction, multiplication, and division.

def add(a, b):
    print(f"{a}+{b}= {a + b}\n")
def sub(a, b):
    print(f"{a}-{b}= {a - b}\n")
def mul(a, b):
    print(f"{a}*{b}= {a * b}\n")
def div(a, b):
    print(f"{a}/{b}= {a / b}\n")

def calculate():
    a = float(input("Enter your 1st number: "))
    b = float(input("Enter your 2st number: "))

    while True:
        print("What's Your Choice:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Divition")
        user = input("Enter Your Choice (1/2/3/4/5): ")

        if user == "1":
            add(a, b)
        elif user == "2":
            sub(a, b)
        elif user == "3":
            mul(a, b)
        elif user == "4":
            div(a, b)
        elif user == "5":
            print("Exit!\nThanks For Using This Functin.")
            break
        else:
            print(f""
                  f"Invaild Input!:  {user}\n Please try again.\n")


calculate()