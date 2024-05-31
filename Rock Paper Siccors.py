import random as r
import time as t
choices = "Rock","Paper","Scissors"
plpoint= 0
computorpoint = 0
tie = 0
while True:
    Item = r.choice(choices)
    u_item = str(input("Enter R, P or S for Rock Paper Scissors or stop to stop the game:"))
    u_item = u_item.lower()
    if u_item == "s" or u_item == "r"or u_item ==  "p":
        print("Rock!")
        t.sleep(1)
        print("Paper!")
        t.sleep(1)
        print("Scissors!")
        t.sleep(1)
        print("Shoot!")
        t.sleep(1.25)
        print("Computer:",Item)
        if u_item == "s":
            u_item = "Scissors"
        elif u_item == "r":
            u_item = "Rock"
        else:
            u_item = "Paper"
        print("You:",u_item)
        #print("." "." ".", end=" ")
        if Item == "Rock" and u_item == "Scissors" or Item == "Scissors" and u_item == "Paper" or Item == "Paper" and u_item == "Rock":
            print("You lost!")
            computorpoint += 1
        elif Item == "Rock" and u_item == "Rock" or Item == "Scissors" and u_item == "Scissors" or Item == "Paper" and u_item == "Paper":
            print("TIE!")
            tie  += 1
        else:
            print("You won!")
            plpoint += 1
        print("computor's points:",computorpoint,"\nYour points:",plpoint,"\nThe number of ties you had:",tie)

    elif u_item == "stop":
        print("ok")
        if computorpoint > plpoint:
            print("The computor won with", computorpoint, "points.\n"
                                                          "You had", plpoint, "points")
        elif plpoint > computorpoint:
            print("Congratulations, You won with",plpoint,"points.\n"
            "The computor had",computorpoint,"points")
        elif plpoint == computorpoint:
            print("It was a tie.")

        break
