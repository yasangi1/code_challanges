# Random password generator

import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9',]
symbols = ['!','#','€','%','&','(',')','*','+']

list = []

print("Welcome to the PyPassword Generator!")
nu_letters = int(input("How many letters would you like in your password? \n "))
nu_numbers = int(input("How many numbers would you like in your password? \n "))
nu_symbols = int(input("How many symbols would you like in your password? \n "))
for i in range(1, nu_letters+1):
 random_letters = random.choice(letters)
 list.append(random_letters.upper())

for x in range(1, nu_numbers+1):
 random_numbers = random.choice(numbers)
 list.append(random_numbers)
 
for m in range(1, nu_symbols+1):
 random_symbols = random.choice(symbols)
 list.append(random_symbols)
  
#print(list)
random.shuffle(list)
random_pw = ''.join(list)
print(f"Here is your password: {random_pw}")
