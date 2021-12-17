import Art

# Addition
def add(n1, n2):
    return n1 + n2

# Subtraction
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(Art.logo)

    num1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)

    keep_going = True
    while keep_going:
        chosen_operation = input("Pick an operation from the above list: ") 
        num2 = float(input("What is the next number? "))
        calc_function = operations[chosen_operation]
        answer = calc_function(num1, num2)
        print(f"{num1} {chosen_operation} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").strip().lower() == 'y':
            num1 = answer
        else:
            keep_going = False
            calculator()

calculator()