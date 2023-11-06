# This is a program to find the maximum number of a list.

student_scores = input("Please enter student scores:  ").split()
max_value = student_scores[0]

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
 # print(n)

# Write your code below this row 👇
  if int(max_value) > student_scores[n]:
    max_value = max_value
  elif int(max_value) < student_scores[n]:
    max_value = student_scores[n]
  elif int(max_value) == student_scores[n]:
    max_value = max_value
print(f"The highest score in the class is: {max_value}")
