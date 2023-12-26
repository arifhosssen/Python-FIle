# #Exercise how to use class and object in python programing language.
#
# class student:
#     roll = " "
#     gpa = " "
#     def __init__  (self,roll,gpa):
#         self.roll = roll
#         self.gpa = gpa
#
# rahman = student(101,3.12)
# # print(f"{rahman.roll}, GPA- {rahman.gpa}")
# #import math
# import math
# from math import gcd,lcm,pow,pi,sqrt
# print(gcd(50,60))
# print(lcm(50,60))
# print(int(pow(2,4)))
# print(pi)
#
# print(sqrt(9))

import time

def set_alarm():
    alarm_time = input("Enter the alarm time (HH:MM): ")
    alarm_message = input("Enter the alarm message: ")

    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("Alarm! " + alarm_message)
            break
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    print("Simple Alarm Clock")
    set_alarm()

import datetime
import time

def set_alarm():
    try:
        alarm_time_str = input("Enter the alarm time in HH:MM format: ")
        alarm_message = input("Enter the alarm message: ")

        # Parse the input time
        alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M")

        while True:
            current_time = datetime.datetime.now().strftime("%H:%M")
            if current_time == alarm_time.strftime("%H:%M"):
                print("Alarm! " + alarm_message)
                break
            time.sleep(60)  # Check every minute

    except ValueError:
        print("Invalid input format. Please use HH:MM format for the time.")

if __name__ == "__main__":
    print("Simple Alarm Clock")
    set_alarm()

