# Sample input - Angela, Ben, Jenny, Michael, Chloe

import random

names = names_string.split(", ")
# The code above converts the input into an array seperating

random_name = random.randrange(len(names))
print(f"{names[random_name]} is going to buy the meal today!")
