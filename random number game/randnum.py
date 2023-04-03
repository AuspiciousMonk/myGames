import random

def secret():
    return random.randint(1,20)
op = 'x'
while op != 'n':
    sec_num = secret()
    for i in range(1,6):
        u_num = int(input("enter your number : "))
        if sec_num == u_num:
            print("you won")
            break
        elif sec_num > u_num:
            print("you number is smaller than the secret number ")
        elif sec_num < u_num:
            print("you number is greater than the secret number ")
    if sec_num != u_num:
        print("you lost!!")
    print("if you want to quit enter n else if you want to play again enter anything else : ")
    op = input("")