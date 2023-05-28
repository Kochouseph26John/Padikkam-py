import random

while True:
    
    n=random.randint(1,100)
    i=0
    while True:
        i+=1
        g=int(input("Your guess?"))
        if g==n:
            print("Congrats!!!...Your guess is right!")
            f=1
            break
        elif g>n:
            print("Your guess is high!")
        else:
            print("Your guess is low!")
        if i == 5:
            f=0
            break
    if f==0:
        print("You are out of chance")
        
    r = input("Do u want to continue (y/n)")
    if r=='n':
        break