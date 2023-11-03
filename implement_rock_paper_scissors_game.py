# This is the implementation for rock paper scissors game.
# More about game rules can be found here: https://wrpsa.com/the-official-rules-of-rock-paper-scissors/ 


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

print("Welcome to the Rock Paper Scissors Game !")

game_images =  [rock, paper, scissors]
#game_images_length = len(game_images)
user_input = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.    "))
if user_input >= 3 or user_input < 0:
  print("You typed an invalid number.")
else: 
  print(game_images[user_input])

  random_selection = random.randint(0,2)
  print("Computer Choose: ")
  print(game_images[random_selection])


  if user_input == 0 and random_selection == 2:
   print("You win !")
  elif user_input == 2 and random_selection == 1:
   print("You win !")
  elif user_input == 1 and random_selection == 0:
   print("You win !")
  elif user_input == 2 and random_selection == 0:
   print("You loss !")
  elif user_input == 1 and random_selection == 2:
   print("You loss !")
  elif user_input == 0 and random_selection == 1:
   print("You loss !")
  elif user_input == random_selection:
   print("It's a Draw !")

'''Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.'''
