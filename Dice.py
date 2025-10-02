import random
while True:
    Res=input("Roll the dice ? (Y/N) :").upper()
    if Res=="Y":
            dice1=random.randint(1,6)
            dice2=random.randint(1,6)
            print(f"({dice1},{dice2}) ")
            #print(f"({dice1},{dice2})") 
    elif Res=="N":
        print("Thanks for Playing!")
        break
    else:
        print("Invalid Choice")
        

    

