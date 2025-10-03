#Rolling Dice Game 
#Modify the program so the user can specify how many dice they want to roll. 
import random
while True:
    Res=input("Roll the dice ? (Y/N) :").upper()
    if Res=="Y":
        n=int(input("How many Dices you want to roll ?: "))
        i=1
        arr=[]
        while i<=n:
            dice=random.randint(1,6)
            arr.append(dice)
            i=i+1
        print("(",end=" ")
        print(",".join(map(str,arr)),end=" ")
        print(")")
    elif Res=="N":
        print("Thanks for Playing!")
        break
    else:
        print("Invalid Choice")
