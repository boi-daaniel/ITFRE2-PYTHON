
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter choice: "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * (9/5)) + 32
    print(format(celsius, ".1f"), "°C is equal to ", format(fahrenheit,".1f"), "°F")

elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) / (9/5)
    print(format(fahrenheit,".1f"), "°F is equal to ", format(celsius,".1f"), "°C")

else:
    print("Enter a valid choice!")





