import os


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


operation_dict = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculate():
    first = int(input("Enter first number: "))
    for symbol in operation_dict:
        print(symbol)

    continue_calculate = True
    while continue_calculate:
        operation = input("Pick an operation: ")
        second = int(input("Enter second number: "))

        calculator_function = operation_dict[operation]
        output = round(calculator_function(first, second), 2)
        print(f"{first} {operation} {second} = {output}")

        continue_calculating = input(f"Enter 'y' to continue with {output} or 'n' to start a new calculation or 'x' "
                                     f"to exit: ").lower()

        if continue_calculating == "y":
            first = output
        elif continue_calculating == "n":
            continue_calculate = False
            os.system('cls')
            calculate()
        else:
            continue_calculate = False
            print("Goodbye")


calculate()
