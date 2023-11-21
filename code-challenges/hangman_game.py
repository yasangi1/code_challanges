# Program to play Hangman game

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
display = ""

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You have already guessed {guess}")
    
    for letter in range(0,len(random_word)):
        if random_word[letter] == guess:
            blank_list[letter] = guess
            display = ''.join(blank_list)
    print(display)
    
    if guess not in random_word:
        print(f"You guessed {guess}, that is not in the word. You lose a life.")
        lives -= 1
        #print(lives)
        if lives == 0:
            end_of_game = True
            print("You Lose! ")

    if "_" not in blank_list:
        end_of_game = True
        print("You Win! ")
        
    print(stages[lives])
            
        
        

    

