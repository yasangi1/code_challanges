'''
Love Calculator

This is a program that tests the compatibility between two people. To work out the love score between two people:
1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
2. Then check for the number of times the letters in the word LOVE occurs.
3. Then combine these numbers to make a 2 digit number. '''

print("The Love Calculator is calculating your score...")
name1 = input("What is your name?    ") 
name2 = input("What is their name?   ") 

name1_lower = name1.lower()
name2_lower = name2.lower()

t = name1_lower.count('t') + name2_lower.count('t')
r = name1_lower.count('r') + name2_lower.count('r')
u = name1_lower.count('u') + name2_lower.count('u')
e = name1_lower.count('e') + name2_lower.count('e')

true_score = t+r+u+e

l = name1_lower.count('l') + name2_lower.count('l')
o = name1_lower.count('o') + name2_lower.count('o')
v = name1_lower.count('v') + name2_lower.count('v')
e1 = name1_lower.count('e') + name2_lower.count('e')

love_score = l+o+v+e1

total_score = str(true_score)+str(love_score)

if int(total_score) < 10 or int(total_score) > 90:
 print(f"Your score is {total_score}, you go together like coke and mentos.")
elif int(total_score) > 40 and int(total_score) < 50:
 print(f"Your score is {total_score}, you are alright together.")
else:
  print(f"Your score is {total_score}.")

