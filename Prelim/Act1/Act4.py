import math

pi = math.pi

while True:
    print("Choose a shape to calculate the area: \n"
          "1. Circle \n"
          "2. Rectangle \n"
          "3. Triangle \n"
          "4. Exit")
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        area = pi * (radius * radius)
        print("The area of the circle is: " ,format(area, ".2f"))

    elif choice == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = (length * width)
        print("The area of the rectangle is: " ,format(area, ".2f"))

    elif choice == 3:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 1/2 * base * height
        print("The area of the triangle is: " ,format(area, ".2f"))

    else:
        break







