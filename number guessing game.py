print("*****Number Guessing Game*****\n"
    "---Intructions--- \n"
      "* You have 3 attempts if you put in a range less than 10, else you have 5 attempts\n"
      "*You enter a range for the difficulty\n"
      "*You can't enter 0 or negative numbers\n"
      "*Enter your number and have fun!")
import random as r
Range = int(input("Enter a range:"))
if Range > 10:
    att = 5
else:
    att = 3
num = r.randint(1, Range)
for i in range(att):
    num2 = int(input("Enter your number:"))
    if num == num2:
        print("You won!")
        break
    else:
        att -= 1
        print("You lost!")
        if att > 0:
            print("You have",att,"more attempts")

print("The number was...",num,"!")
