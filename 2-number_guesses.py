import random

top_of_range=input("enter the number: ");

if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range<=0:
        print("please enter the number greater than zero!")
        quit()
else:
    print("please enter the valid character next!")
    quit()

bot_num=random.randint(0,top_of_range)
total_guess=0

while True:
    your_guess=input("enter your guess: ")

    if your_guess.isdigit():
        your_guess=int(your_guess)

    else:
        print("enter the number")
        continue

    if your_guess==bot_num:
        print("You got it")
        break
    elif your_guess<bot_num:
        print("enter the greater number than your guess")
        total_guess+=1
    else:
        print("enter the less number than your guess")
        total_guess+=1

print("You got it in", total_guess ,"guesses")
