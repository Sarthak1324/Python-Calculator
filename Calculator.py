import math

# --- Operations ---
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def square(x):
    return x * x

def cube(x):
    return x * x * x

def square_root(x):
    if x < 0:
        return "Error: Cannot find square root of negative number"
    return math.sqrt(x)

# --- Main Menu ---
def main():
    print("\n====== Python Calculator ======")
    print("1. Basic Operations (+, -, *, /)")
    print("2. Power Operations (Square, Cube, Square Root)")
    print("3. Trigonometry (Sin, Cos, Tan)")
    print("================================")

    choice = input("Choose a category (1/2/3): ")

    if choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        op = input("Choose operation (1/2/3/4): ")

        if op == "1":
            print(f"Result: {add(num1, num2)}")
        elif op == "2":
            print(f"Result: {subtract(num1, num2)}")
        elif op == "3":
            print(f"Result: {multiply(num1, num2)}")
        elif op == "4":
            print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid choice!")

    elif choice == "2":
        num = float(input("Enter a number: "))
        print("\n1. Square")
        print("2. Cube")
        print("3. Square Root")
        op = input("Choose operation (1/2/3): ")

        if op == "1":
            print(f"Result: {square(num)}")
        elif op == "2":
            print(f"Result: {cube(num)}")
        elif op == "3":
            print(f"Result: {square_root(num)}")
        else:
            print("Invalid choice!")

    elif choice == "3":
        degree = float(input("Enter angle in degrees: "))
        radians = math.radians(degree)
        print("\n1. Sin")
        print("2. Cos")
        print("3. Tan")
        op = input("Choose operation (1/2/3): ")

        if op == "1":
            print(f"Result: {round(math.sin(radians), 6)}")
        elif op == "2":
            print(f"Result: {round(math.cos(radians), 6)}")
        elif op == "3":
            print(f"Result: {round(math.tan(radians), 6)}")
        else:
            print("Invalid choice!")

    else:
        print("Invalid category!")

    again = input("\nCalculate again? (yes/no): ")
    if again.lower() == "yes":
        main()

main()
