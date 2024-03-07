from logo import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2



operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}



print(logo)

def calculator():
    first_number = float(input("What's the first number?: "))
    for symbol in operation:
        print(symbol)
    continue_calculation = True
    while continue_calculation:
        operation_symbol = input("Pick an operation from the line above: ")
        second_number = float(input("What's the next number?: "))
        #access the user specified operation from the operation dictionary
        calc_function = operation[operation_symbol]
        first_result = float(calc_function(first_number, second_number))

        print(f"{first_number} {operation_symbol} {second_number} = {first_result}")

        input_continue = input(f"Type 'y' to continue calculating with {first_result}, type 'n' to start a new calculation, or type f to exit: ").lower()

        if input_continue == "y":
            first_number = first_result
        elif input_continue == "n":
            continue_calculation = False
            calculator()
        elif input_continue == "f":
            continue_calculation = False
            print("Goodbye")
        
calculator()
    

