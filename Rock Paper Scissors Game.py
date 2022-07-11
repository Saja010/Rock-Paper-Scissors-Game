import random


uesr_scor=0
compuetr_scor=0

Option=["rock","paper","scissor"]

print("welcome to the Rock Paper Scissor  Game :) ")
play=input("Do you want to play the Game ? ")


if play != "yes":
    quit()


while True:
    uesr_input=input("enter Rock:Paper:Scissor or for exit enter Q : ").lower()
    if uesr_input =="q":
        break

    if uesr_input  not in Option :
        continue

    # 0:Rock 1:Paper 2:Scissor
    random_num=random.randint(0,2)
    computer_input=Option[random_num]
    print("Computer Picked ",computer_input + ".")

    if uesr_input=="rock" and computer_input == "scissor":
        print("you get one !")
        uesr_scor +=1   
    elif uesr_input=="paper" and computer_input == "rock":
        print("you get one !")
        uesr_scor +=1    
    elif uesr_input=="scissor" and computer_input == "paper":
        print("you get one !")
        uesr_scor +=1
    else:
        print("you lose :( ") 
        compuetr_scor +=1  
        
print("you score ", uesr_scor )
print("computer score ", compuetr_scor )
print("GoodBye! :) ")



