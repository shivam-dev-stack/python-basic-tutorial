import random


choice = ["rock", "paper", "scissors"]

choice_u = int(input("enter your choice  "))
userchoice = choice[choice_u]

if choice_u > 2 or choice_u < 0:
    print("invalid input")
else:
    computerchoice = choice[random.randint(0, 2)]
    print("you choose ----->",userchoice)
    print("computer choose ----->",computerchoice)

    if(userchoice == computerchoice):
        print("It's a tie!")
    else:
        if userchoice == "rock" :
            if computerchoice == "scissors":
                print("you win")
            else:
                print("computer wins")

        elif userchoice == "paper":
            if computerchoice == "rock":
                print("you  win")
            else:
                print("computer wins")

        elif userchoice=="scissors": 
            if computerchoice  == "paper" :
                print("you  win")
            else:
                print("computer wins")