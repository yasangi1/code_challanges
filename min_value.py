# This is a program to find the minimum value of a list.

student_heights = input("Enter students heights seperated by space:   ").split()

min_value = student_heights[0]
for n in range(0, len(student_heights)-1):
    #print(int(height))
    if int(min_value) < int(student_heights[n+1]):
        min_value = min_value
    elif int(min_value) > int(student_heights[n+1]):
        min_value = student_heights[n+1]
    elif int(student_heights[n]) == int(student_heights[n+1]):
        min_value = min_value
print(min_value)
