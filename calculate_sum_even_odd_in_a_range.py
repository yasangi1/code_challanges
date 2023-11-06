# This program is to find the sum of even numbers and sum of odd numbers of a user given range.

target = int(input(" Enter a number between 0 and 1000:  ")) 

total_even = 0
total_odd = 0
for i in range(1, target+1):
 if i % 2 == 0:
   total_even += i  
 else:
   total_odd += i
print(f"Total even = {total_even}")
print(f"Total odd = {total_odd}")

# or else we can use complete range function as: for i in range(2, target+1, 2): total_even += i to find sum of even and for i in range(1, target+1, 2): total_odd += i to find sum of odd

