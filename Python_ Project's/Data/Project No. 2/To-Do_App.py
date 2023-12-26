'''To-Do List Application:
Build a simple to-do list where users can add, remove, and view tasks. You can use a text file to store tasks.'''


def take_tasks():
    try:
        with open("text_file.txt") as file:
            # task = file.read().splitlines()
            task = [line.strip() for line in file.readlines()]
    except(FileNotFoundError):
        task = []

    return task


# ADD to file Text...
def add(task):
    with open("text_file.txt","a") as file:
        file.write(task + "\n")
        print(f"Added To Text File: {task}")

def remove(task):
    tasks = take_tasks()
    if task in tasks:
        tasks.remove(task)
        with open("text_file.txt","w") as file:
            for i in tasks:
                file.write(i + "\n")
                print(i)
                print(f"{task} Remove From Text File.")
    else:
        print("Text Not Found in 'text_file.txt'.")

def view():
    tasks = take_tasks()
    if tasks:
        print("\nHere the 'text_file.txt' bellow:  \n")
        for i in tasks:
            print(i)
    else:
        print("NO File Exist!")
while True:
    #Options For User what have to do...
    print("\nWhat you want to do?\n1. Add Text.\n2. Remove Text.\n3. View File.\n4. Exit.")

    #Taking Task from User...
    user = input("Enter Your Choice(1/2/3/4): ")

    if user == "1":
        task = input("Enter You Text Here: ")
        add(task)
    elif user == "2":
        task = input("\nEnter You Text Here: ")
        remove(task)
    elif user == "3":
        print("text_file.txt: ")
        view()
    elif user == "4":
        print("Exit!\n Thank's For Using This Function.")
        break
    else:
        print(f"Invaild!, Please select correct option(1/2/3/4)")