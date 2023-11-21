# Hangman game

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print("Welcome to the HANGMAN Game!")

words = ["Rabbit", "Library", "University", "Employee", "Daughter"]
random_word = random.choice(words).lower()
#print(random_word)

blank_list = []
for i in range(len(random_word)):
    blank_list.append("_")
print(blank_list)

end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    for letter in range(0,len(random_word)):
        if random_word[letter] == guess:
            blank_list[letter] = guess
    print(blank_list)
    
    if guess not in random_word:
        lives -= 1
        #print(lives)
        if lives == 0:
            end_of_game = True
            print("You Lose! ")

    if "_" not in blank_list:
        end_of_game = True
        print("You Win! ")
        
    print(stages[lives])
            
        
        
