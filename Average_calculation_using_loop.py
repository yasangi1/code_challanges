# This is a program that calculates the average student height from a List of heights.

student_heights = input("Enter students heights seperated by space:   ").split()

nu_of_students = 0
sum_height = 0

for height in student_heights:
  sum_height =  sum_height + int(height)
  nu_of_students = nu_of_students + 1
  
print(f"total height = {sum_height}")
print(f"number of students = {nu_of_students}")
print(f"average height = {round(sum_height / nu_of_students)}")
