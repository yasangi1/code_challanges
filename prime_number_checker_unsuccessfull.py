# Still modifing this code since this is not complately working properly.

# Write your code below this line 👇

def prime_checker(number):
  for i in range(2,number):
    if number%i != 0:
      if (number/1 == number) and (number/number == 1):
        print("It's a prime number.")
        break
      else:
        ("It's not a prime number.")
        break
    else:
      print("It's not a prime number.")
      break

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)
