name=input("Type your name: ")
print("Welcome ",name, "to this adventure!")

answer=input("You are on a dirt road, It has come to an end and you can go left or right.").lower()

if answer=="left":
    answer=input("You come to a river, You can walk around it or swim across?  Type walk to walk around and swim to swim across: ").lower()
    if answer=="swim":
        print("You swam across and were eaten by an alligator.")
    elif answer=="walk":
        print("You walked for many miles.")
    else:
        print("Not a valid option. You lose!")
elif answer=="right":
    answer=input("You come to a bridge, it looks wobbly, do you want to cross it or head back(cross/back)?").lower()
    if answer=="back":
        print("You go back and loss")
         
    elif answer=="cross":
        answer=input("You cross the bridge and meet a stranger. Do you talk to them(yes/no)?:  ").lower()
        if answer=="yes":
            print("You talk to the stranger and they give you gold. You WIN!")

        elif answer=="no":
            print("you ignore the sranger and the are offended and you loss")

        else:
            print("not a valid option. You lose")

    else:
        print("not a valid option. You lose!")



else:
    print("not a valid option. You lose.")