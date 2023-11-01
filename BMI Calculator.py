# This is the Body Mass Index (BMI) based on a user's weight and height. It tells the user the interpretation of their BMI based on the BMI value.

# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())

bmi_value = float(weight / (height ** 2))
#print(bmi_value)

if bmi_value <= 18.5:
  print(f"Your BMI is {bmi_value}, you are underweight.")
elif (bmi_value > 18.5) & (bmi_value < 25):
  print(f"Your BMI is {bmi_value}, you are a normal weight.")
elif (bmi_value >= 25) & (bmi_value < 30):  
  print(f"Your BMI is {bmi_value}, you are slightly overweight.")
elif (bmi_value >= 30) & (bmi_value < 35):  
  print(f"Your BMI is {bmi_value}, you are slightly obese.")
else:
 print(f"Your BMI is {bmi_value}, you are clinically obese.")
