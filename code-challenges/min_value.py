# This is a program to find the minimum value of a list.

student_heights = input("Enter students heights seperated by space:   ").split()

for n in range(0, len(student_heights)-1):
 student_heights[n] = int(student_heights[n])
 
min_height = student_heights[0]
for height in student_heights:
 if min_height > int(height):
     min_height = height
     
print(f"The highest score in the class is: {min_height}")
