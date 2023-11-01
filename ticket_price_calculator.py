#This is a rolllercoaster ticket price calculator

height = int(input("Enter your height in cm  "))
bill = 0
if height > 120:
  age = int(input("Enter your age  "))
  if age < 12:
    bill = 5
    print("Your ticket price is €5")
  elif (age >= 12) & (age < 18):
    bill = 7
    print("Your ticket price is €7")
  else:
    bill = 12
    print("Your ticket price is €12")
    
  photo = input("Do you want photos - y or n  ")
  if photo == "y":
    print(f"Your total bill is € {bill + 3}")
  else:
    print(f"Your total bill is € {bill}")
else:
  print("You can't ride")
