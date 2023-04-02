# importing important modules

import random
import sys
from termcolor import colored

# function for generating random number


def randomnum():
    a = random.randint(10000, 99999)
    return a


# setting up loop for playing again

op = "y"
while op == "y":
    sys.stdout.write("\x1b[1A")
    sys.stdout.write("\x1b[2K")

    while True:  # loop for making sure that there is no two same digit in number
        num = randomnum()
        b = [int(x) for x in str(num)]
        c = any(b.count(x) > 1 for x in b)
        if c == True:
            continue
        else:
            break
    for i in range(5):  # loop for taking input and checking u won or not
        n2 = input("\nguess a 5 digit number : ")
        print("chance no. ", i + 1)
        n3 = list(n2)
        for i in range(5):
            if b[i] == int(n3[i]):
                print(colored(n3[i], "green"), end="")
            elif int(n3[i]) in b:
                print(colored(n3[i], "yellow"), end="")
            else:
                print(int(n3[i]), end="")
        if num == int(n2):
            print("\nyou won")
            break

    if num != int(n2):
        print("\nyou lost")
    op = input("if you wnat to play again enter y else enter anything else : \n")