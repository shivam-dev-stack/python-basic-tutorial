import random

choice = ["rock", "paper", "scissors"]

choice_u = int(input("enter your choice  rock:1, paper:2, scissors:3\n"))


ui = [ '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
 
''',

'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

''',

'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
]

if choice_u > 3 or choice_u < 1:
    print("invalid input")
else:
    userchoice = choice[choice_u-1]
    ch = random.randint(0, 2)
    computerchoice = choice[ch]
    print(ui[choice_u-1])
    print(ui[ch])
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