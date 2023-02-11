import random

while(True):
    f=input('Wanna roll the dice?(y/n)')
    if f=='n':
        break
    a=random.randint(1,6)
    if a==1:
        print('Dice rolls\n')
        print('┌─────────┐\n│         │\n│    ●    │\n│         │\n└─────────┘\n')
    if a==2:
        print('Dice rolls\n')
        print('┌─────────┐\n│  ●      │\n│         │\n│      ●  │\n└─────────┘\n')
    if a==3:
        print('Dice rolls\n')
        print('┌─────────┐\n│  ●      │\n│    ●    │\n│      ●  │\n└─────────┘\n')
    if a==4:
        print('Dice rolls\n')
        print('┌─────────┐\n│  ●   ●  │\n│         │\n│  ●   ●  │\n└─────────┘\n')
    if a==5:
        print('Dice rolls\n')
        print('┌─────────┐\n│  ●   ●  │\n│    ●    │\n│  ●   ●  │\n└─────────┘\n')
    if a==6:
        print('Dice rolls\n')
        print('┌─────────┐\n│  ●   ●  │\n│  ●   ●  │\n│  ●   ●  │\n└─────────┘\n')
