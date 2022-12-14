
# - - - - IMPORTS


# - - - - METHODS

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

# - - - - PROGRAM

operators = {
                "+" : add,
                "-" : sub,
                "*" : mul,
                "/" : div
            }


if __name__ == "__main__":

    print("\n\n")
    
    # Get inputs from user
    first_num = float(input("Enter the first number: "))
    given_op = input("Enter the prefered operator [ + , - , * , / ]: ")
    second_num = float(input("Enter the second number: "))

    # Calculate result
    algorithm = operators[given_op]
    result = algorithm(first_num, second_num)

    # Output equation
    equation = "Equation: " + str(first_num) + " " + given_op + " " + str(second_num) + " = " + str(result)
    print(equation)

    print("\n\n")

