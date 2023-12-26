def take():
    try:
        with open("text.txt","r") as file:
            takes = file.read().splitlines()
    except(FileNotFoundError):
        takes = []
    return takes

def add(takes):
    with open("text.txt", 'a') as file:
        file.write(takes + "\n")
        print("Text Added Successfully.")

def remove(tasks):
    doc = take()
    with open("text.txt") as file:
        if tasks in doc:
            doc.remove(tasks)
            print("Text Remove Successfully.")
            for i in doc:
                print(i)

        else:
            print("File Not Found!")

def view():
    f = take()
    if f:
        print("Here You Text File: \n")
        for num, i in enumerate(f, 1):
            print(f"{num}. {i}")
    else:
        print("No file exsit")

while True:
    print("\nWhat you want to do?\n1. Add Text.\n2. Remove Text.\n3. View File.\n4. Exit.")
    user = int(input("Chose Your Option (1/2/3/4): "))

    if user == 1:
        takes = input("Enter Your Text Here: ")
        add(takes)
    elif user == 2:
        tasks = input("\nEnter Your Text Here: ")
        remove(tasks)
    elif user == 3:
        view()
    elif user == 4:
        print("Exit!\n Thank's For Using This Funciton.")
        break
    else:
        print("Invaild Input!\nPlease Enter Correct Choice in (1/2/3/4): ")