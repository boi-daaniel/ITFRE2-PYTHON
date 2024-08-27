print("Enter 'x' to exit")
while True:
    expression = input('>> ')

    if expression == 'x':
        break
    try:
        if expression != 'x':
            output = eval(expression)
            print(output)
    except:
        print("Error: Invalid Number Format.")