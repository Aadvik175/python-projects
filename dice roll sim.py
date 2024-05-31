import random as r
import time as t
d = int(input("Enter a max number:"))
while True:
    dice = int(input("Enter 1 to roll, Enter 2 to stop:"))
    if dice == 2:
        break
    print(r.randint(1,d))