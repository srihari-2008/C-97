import random
print("Number Guessing Game")
number=random.randint(1,9)
chances=0
print("Guess A Number Between 1 and 9")
while(chances<5):
    guess=int(input("Enter Your Guess:"))
    if(guess==number):
        print("CONGRATULATIONS!!! YOU WON")
        break
    elif(guess>number):
        print("Your Guess is Too High, Please Enter A Small Number")
    else:
        print("Your Guess Is Too Low Enter A Bigger Number")
    chances=chances+1
if not chances<5:
    print("YOU LOST, The Number Is",number)