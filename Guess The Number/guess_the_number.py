import random

n=random.randint(1,100)
for i in range(5):
    f=0
    g=int(input("Your guess?"))
    if g==n:
        print("Congrats!!!...Your guess is right!")
        f=1
        break
    elif g>n:
        print("Your guess is high!")
    else:
        print("Your guess is low!")
if f==0:
    print("You are out of chance")