
# ADVANCED PYTHON CALCULATOR
# Developer: Hesam


history = []


def line():
    print("=" * 45)


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Error! Please enter a valid number.")


def add():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    result = a + b
    print("Result:", result)
    history.append(f"{a} + {b} = {result}")


def subtract():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    result = a - b
    print("Result:", result)
    history.append(f"{a} - {b} = {result}")


def multiply():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    result = a * b
    print("Result:", result)
    history.append(f"{a} * {b} = {result}")


def divide():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    if b == 0:
        print("Error: Division by zero!")
        return
    result = a / b
    print("Result:", result)
    history.append(f"{a} / {b} = {result}")


def power():
    a = get_number("Enter base: ")
    b = get_number("Enter exponent: ")
    result = a ** b
    print("Result:", result)
    history.append(f"{a} ** {b} = {result}")


def square_root():
    a = get_number("Enter number: ")
    if a < 0:
        print("Error: Negative number!")
        return
    result = a ** 0.5
    print("Result:", result)
    history.append(f"sqrt({a}) = {result}")


def remainder():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    if b == 0:
        print("Error: Division by zero!")
        return
    result = a % b
    print("Result:", result)
    history.append(f"{a} % {b} = {result}")


def integer_division():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    if b == 0:
        print("Error: Division by zero!")
        return
    result = a // b
    print("Result:", result)
    history.append(f"{a} // {b} = {result}")


def average():
    count = int(get_number("How many numbers? "))
    if count <= 0:
        print("Invalid count!")
        return
    total = 0
    for i in range(count):
        number = get_number(f"Number {i + 1}: ")
        total += number
    result = total / count
    print("Average:", result)
    history.append(f"Average = {result}")


def percentage():
    number = get_number("Enter number: ")
    percent = get_number("Enter percentage: ")
    result = number * percent / 100
    print("Percentage:", result)
    history.append(f"{percent}% of {number} = {result}")


def absolute_value():
    number = get_number("Enter number: ")
    result = abs(number)
    print("Absolute value:", result)
    history.append(f"abs({number}) = {result}")


def even_odd():
    number = int(get_number("Enter integer: "))
    print("Number is EVEN" if number % 2 == 0 else "Number is ODD")


def prime_number():
    number = int(get_number("Enter integer: "))
    if number < 2:
        print("Not a prime number")
        return
    prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            prime = False
            break
    print("Prime number" if prime else "Not a prime number")


def factorial():
    number = int(get_number("Enter a number: "))
    if number < 0:
        print("Factorial is not defined for negative integers.")
        return
    result = 1
    for i in range(1, number + 1):
        result *= i
    print("Factorial:", result)
    history.append(f"{number}! = {result}")


def sum_numbers():
    number = int(get_number("Enter N: "))
    if number < 0:
        print("Please enter a non-negative number.")
        return
    total = 0
    for i in range(1, number + 1):
        total += i
    print("Sum:", total)
    history.append(f"Sum 1 to {number} = {total}")


def square():
    side = get_number("Enter side: ")
    print("Area:", side ** 2)
    print("Perimeter:", side * 4)


def rectangle():
    length = get_number("Enter length: ")
    width = get_number("Enter width: ")
    print("Area:", length * width)
    print("Perimeter:", 2 * (length + width))


def circle():
    radius = get_number("Enter radius: ")
    if radius < 0:
        print("Invalid radius!")
        return
    pi = 3.14159
    print("Area:", pi * radius ** 2)
    print("Perimeter:", 2 * pi * radius)


def show_history():
    line()
    print("CALCULATION HISTORY")
    line()
    if not history:
        print("History is empty.")
    else:
        for item in history:
            print(item)


def clear_history():
    history.clear()
    print("History cleared successfully!")


def menu():
    while True:
        line()
        print("       ADVANCED CALCULATOR")
        line()
        print("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Power
6. Square Root
7. Remainder
8. Integer Division
9. Average
10. Percentage
11. Absolute Value
12. Even or Odd
13. Prime Number
14. Factorial
15. Sum Numbers
16. Square Area
17. Rectangle Area
18. Circle Area
19. Show History
20. Clear History
0. Exit
""")
        line()
        choice = input("Select an option: ")

        if choice == "1":
            add()
        elif choice == "2":
            subtract()
        elif choice == "3":
            multiply()
        elif choice == "4":
            divide()
        elif choice == "5":
            power()
        elif choice == "6":
            square_root()
        elif choice == "7":
            remainder()
        elif choice == "8":
            integer_division()
        elif choice == "9":
            average()
        elif choice == "10":
            percentage()
        elif choice == "11":
            absolute_value()
        elif choice == "12":
            even_odd()
        elif choice == "13":
            prime_number()
        elif choice == "14":
            factorial()
        elif choice == "15":
            sum_numbers()
        elif choice == "16":
            square()
        elif choice == "17":
            rectangle()
        elif choice == "18":
            circle()
        elif choice == "19":
            show_history()
        elif choice == "20":
            clear_history()
        elif choice == "0":
            print("Thank you for using calculator!")
            break
        else:
            print("Invalid choice!")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    menu()
