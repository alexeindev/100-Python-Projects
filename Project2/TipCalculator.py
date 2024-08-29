#Learned in the exercise:
#Data Types, Operations, Type Conversion , f-Strings
print("Welcome to the tip calculator")
total = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
amount_people = int(input("How many people to split the bil? "))

print(f"Each person should pay: {round(total + ((tip_percentage / 100) * total)) / amount_people}")