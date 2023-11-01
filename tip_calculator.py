# This is a tip calculator and it can calculate the tip amount split between a given number of people.

print("Welcome to the tip calculator")

total_bill_d = input("What was the total bill?  \n")
total_bill_without_d = total_bill_d[1:]
#print(total_bill_without_d)

tip_percentage = input("What percentage tip would you like to give? \n")

tip_percentage_for_cal = 1 + (int(tip_percentage) / 100)
#print(tip_percentage_for_cal)

people = input("How many people to split the bill? \n")

each_person_pay = round((float(total_bill_without_d) * tip_percentage_for_cal) / int(people),2)

print(f"Each person should pay: €{each_person_pay}")
