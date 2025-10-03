'''Add a feature that keeps track of how many times the user has rolled the dice
during the session. This will require a counter that increments each time the
dice are rolled'''

import random
counter=0
while True:
    Res=input("Roll the dice ? (Y/N) :").upper()
    if Res=="Y":
        dice1=random.randint(1,6)
        print(dice1)
        counter=counter+1
    elif Res=="N":
        print("Thanks for Playing!")
        print(f"User rolled the dice {counter} times ")
        break
    else:
        print("Invalid Choice")


