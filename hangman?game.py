# Program to play Hangman game


import random

word_list = ["ardvark", "baboon", "camel"]
choosen_word = random.choice(word_list)
print(choosen_word)

blank_word_list = []
word_list_replace = []
choosen_word_distinct_length = len(set(choosen_word))
print(choosen_word_distinct_length)

for i in range(len(choosen_word)):
    blank_word_list.append("_")
print(blank_word_list)

while choosen_word_distinct_length > 0:
    guess = input("Guess a letter: ").lower()

    for letter in range(0,len(choosen_word)):
        if choosen_word[letter] == guess:
            blank_word_list[letter] = guess
        #else:
            #print("wrong")
    print(blank_word_list)
    choosen_word_distinct_length -= 1
    

