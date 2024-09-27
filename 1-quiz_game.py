
print("welcome to my compute quiz")

playing=input("Do you want to play [yes] ? ").lower()

if playing!="yes":
    quit()
print("Okey, let's play!")
score=0

answer=input("What does CPU stand for? ").lower()
if answer=="central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What does GPU stand for? ").lower()
if answer=="grafics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

answer=input("What does RAM stand for? ").lower()
if answer=="random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What does PSU stand for? ").lower()
if answer=="power supply":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

success_per=(score/4)*100
print("The exam is finished. Your score is: ",str(success_per))