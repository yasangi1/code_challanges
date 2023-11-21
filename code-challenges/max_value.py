# This is a program to find the maximum number of a list.

student_heights = input("Enter students heights seperated by space:   ").split()

for n in range(0, len(student_heights)-1):
 student_heights[n] = int(student_heights[n])
 
max_height = 0
for height in student_heights:
 if max_height < int(height):
     max_height = height
     
print(f"The highest score in the class is: {max_value}")
