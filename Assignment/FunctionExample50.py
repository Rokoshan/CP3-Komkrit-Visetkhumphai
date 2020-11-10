def doNumber():
    x = int(input("First Number :"))
    y = int(input("Second Number:"))
    print("+ = Plus")
    print("- = Minus")
    print("x = Multiply")
    print("/ = divide")
    op = input("Operator :")
    print("--------------")
    if op == "+":
        print("Result:", x+y)
    elif op == "-":
        print("Result:", x-y)
    elif op == "x":
        print("Result:", x*y)
    elif op == "/":
        print("Result:", x/y)

doNumber()
