import random
 
traget =  random.randint(1,100)

while True:
    userchoice = int(input("Guess The Number or Quit(Q): "))
    if(userchoice == "Q"):
        break
    if(userchoice == traget):
        print("Success : Correct Guess!!")
        break
    elif(userchoice < traget):
        print("Your Number to Small! please choice bigger number...")
    else:
        print("Your Number to Big! please choice smaller number...")


print("-------Game Over--------")