import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choise = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 Scissors: ")
choise1 = int(choise)

cpu = random.randint(0, 2)

tools = ["rock", "paper", "scissors"]
game_images = [rock, paper, scissors]

jogador = tools[choise1 - 1]
cpu2 = tools[cpu -1]


if choise1 >= 3 or choise1 < 0:
    print("You lose, type a valid number")
else:      
    print(f"You choose {game_images[choise1]}")
    print(f"Computer choose {game_images[cpu]}")

    if jogador == "rock" and cpu2 == "scissors":
        
    
        print("You win")
    elif jogador == "paper" and cpu2 == "rock":

    
        print("You win")
    elif jogador == "scissors" and cpu2 == "paper":
    
        
        print("You win")
    elif choise1 == cpu:
        print("Draw")

    else:
        if cpu2 == "rock":

            print("You lose")
        elif cpu2 == "paper":
            
            print("You lose")
        elif cpu2 == "scissors":
        
            print("You lose")
