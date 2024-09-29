import random

user_wins=0
computer_wins=0
options=["rock","paper","scissors"]


while True:
    user_input=input("type rock/paper/scissors or Q to quit").lower()

    if user_input=="q":
        break
    if user_input not in options:
        continue

    random_num=random.randint(0,2)
    computer_pick=options[random_num]
    print("Computer picked",computer_pick,".")

    if user_input=="rock" and computer_pick=="scissors":
        user_wins+=1
        print("YOU WON!")
        continue
    elif user_input=="paper" and computer_pick=="rock":
        user_wins+=1
        print("YOU WON!")
        continue
    elif user_input=="scissors" and computer_pick=="paper":
        user_wins+=1
        print("YOU WON!")
        continue
    elif user_input==computer_pick:
        print("DRAW!")
        continue
    else:
        computer_wins+=1
        print("YOU LOSE")

print(f"Your score: {user_wins}\nComputer score: {computer_wins}")    