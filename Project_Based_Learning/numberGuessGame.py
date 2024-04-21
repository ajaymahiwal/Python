import random
import math


print("Happy Guess Game :)")

name = input("Enter Your Name:")

print("Welcome, "+name+" now please enter range for guess game:")

low = int(input("Enter Lowwer Element:"))
high = int(input("Enter Higher Element:"))

number = math.floor(random.random()*(high-low+1)) + low

print(number)

print("Now you can start guessing the number between,",low," To ",high)

user_number = int(input("Guess The Number :"))
total_try = 1

while(number != user_number):
    user_number = int(input("Guess The Number :"))
    total_try+=1
    if(total_try % 5 == 0):
        response = input("You Tried "+str(total_try)+" Times, Would You Like To Continue, If Not just type N")
        if(response == "N"):
            print("Number Not Found, even after ",total_try,"tries.")
            break
        else:
            print("You Entered "+ response +" as response.So we are assuming response Yes")


if(number == user_number):
    print("Congratulations "+name+" you found the number after ", total_try ," attemptes.")
