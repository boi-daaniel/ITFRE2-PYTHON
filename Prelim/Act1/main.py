weight = input("Enter your weight in kilograms:")
height = input("Enter your height in kilograms:")

bmi = float(weight) / (float(height) * float(height))
print("\nYour BMI is: ", format(bmi, ".2f"))

if bmi < 18.5:
    category = "Underweight"
if 18.5 <= bmi < 24.9:
    category = "Normal weight"
if 25 <= bmi < 29.9:
    category = "Overweight"
if bmi >= 30:
    category = "Obesity"

print("Your BMI category is :", category)
