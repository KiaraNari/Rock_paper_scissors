import random

print("*******************GAME*******************")
print("***********STONE/SCISSORS/PAPER***********")

comp = random.randint(1,3)

if comp == 1:
    tmp = "Stone"
elif comp == 2:
    tmp = "Scissors"
else:
    tmp = "Paper"

print("1) Stone")
print("2) Scissors")
print("3) Paper")

try:
    x = int(input("Make your choice: "))
    if x == 1:
        print("*****")
        print("Your choice: Stone")
        print("Computer choice: " + str(tmp))
        print("*****")
        if comp == 1:
            print("DRAW")
        elif comp == 2:
            print("You WIN\nComputer LOSE")
        else:
            print("Computer WIN\nYou lose")
        print("*****")
    elif x == 2:
        print("*****")
        print("Your choice: Scissors")
        print("Computer choice: " + str(tmp))
        print("*****")
        if comp == 1:
            print("Computer WIN\nYou lose")
        elif comp == 2:
            print("DRAW")
        else:
            print("You WIN\nComputer LOSE")
        print("*****")
    elif x == 3:
        print("*****")
        print("Your choice: Paper")
        print("Computer choice: " + str(tmp))
        print("*****")
        if comp == 1:
            print("You WIN\nComputer LOSE")
        elif comp == 2:
            print("Computer WIN\nYou lose")
        else:
            print("DRAW")
        print("*****")
    else:
        print("Write omly numbers 1/2/3!")
except:
    print("ERROR!")

